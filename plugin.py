# from __future__ import print_function
import datetime
import enum
import glob
import multiprocessing
import os
import socket
from time import gmtime, sleep, strftime
import ujson
import sys
import signal
from pyepsolartracer.client import EPsolarTracerClient
from pyepsolartracer.registers2 import (coils, registersChargingEquipment,
                                        registersChargingEquipmentRealTime,
                                        registersChargingEquipmentRealTimeStatics,
                                        registersChargingEquipmentRealTimeStatus,
                                        registersChargingEquipmentSettingParameter)

# create list of devices
ports = []
clients = []
jobs =[]
# devices = []
global running
running = True 
datafile = 'sk-plugin-python-epsolar.json'
def sigterm_handler(signal, frame):
    running = False
    sleep(1)
    # processes[-1].terminate()
    # sleep(1)
    # for item in processes:
      
    #   item.join() 
    sys.stderr.write("exitsignals")
    # sys.stderr.write('\n')
    sys.stderr.flush()
    sys.exit(0)
signal.signal(signal.SIGTERM, sigterm_handler)

# from pprint import pprint                                        
class battype (enum.Enum):
  userdefined = 0
  sealed = 1
  GEL = 2
  Flooded = 3
class chgmode (enum.Enum):
 off = 0
 PWM = 1
 MPPT = 2

def getports ():
  ports = list(glob.glob(os.path.join('/dev/','ttyXRUSB*')))
  return ports

def createclient(port):
  # print 'creating client for',port
  # creates a client and appends to clients list
  try:
    client = EPsolarTracerClient(method = 'rtu', port = port, baudrate = 115200, timeout = 0.2 )
    #need to do a check to make sure device is on as it fails if unit is not on or conected to cable
    # print client
    client.connect()
    sleep(1)
    unitid = getunitid(client)
    # print client, unitid
    clients.append(client)
    return client
  except AssertionError as error:
    # print 'error connecting',error
    return

def readclientconfig(client):
  try:
    unitid = getunitid(client)
    # Ignore this registers as ints
    registersignorelist = [36883, 36884, 36885, 36894, 36894, 36895, 36896, 36897, 36925, 36926, 36927,
     36930, 36931, 36932, 36933, 36934, 36935, 36936, 36937, 36938, 36939, 36940, 36941, 36965, 36969] 
    #read Config registers from Registers2.
    clientconfig = {}
    #print registersignorelistt
    # Read each current register settings form client
    for reg in registersChargingEquipmentSettingParameter:
      if ( reg.address in registersignorelist):
        #print reg.address, reg.name
        continue
      #print reg.address, reg.name
      tmp1={}
      tmp1.update({reg.name : int(client.read_input(reg.name))})
      clientconfig.update(tmp1)
      #print(tmp1)
    # sync_date = datetime.datetime.now()
    # print (unitid)
    clientconfig.update({'id': unitid})
    return clientconfig
    
  except AttributeError:
    return

def setupclient(client,data):
  devicelist = (data['devices'])
  # print 'devicelist' ,devicelist
  unitid = getunitid(client) 
  # print unitid
  #client.write_rtc(sync_date)
  newunitid = True
  
  for item in data['devices']:
    
    for id in item.values():
      if id == unitid:
        # print
        # print 'sending config to',unitid
        # print
        name = item
        for item in name.items():
          if item[0] == 'id':
            # print item[0],item[1]
            newunitid = False
            continue
          name = item
          # print name[0], name[1]
          client.write_output(name[0], name[1])
      
  # no unit id found in config lets create one
  if newunitid == True:
    newconfig = readclientconfig(client)
    #open oldconfig
    with open(datafile) as json_file:
      oldconfig = ujson.load(json_file)
    #append newconfig to oldconfig
    oldconfig['configuration']['devices'].append(newconfig)
    # sends units config to data file 
    with open(datafile, 'w') as outfile:  
      ujson.dump(oldconfig, outfile, indent=4, sort_keys=True)

def getunitid(client):
  response = client.read_device_info()
  unitid = repr(response.information[1])
  unitid = unitid.strip('\'')
  return unitid

def readunit(client):
#read epsolar and write sk update to local host. 
  while running == True:
    try:
      timestamp = strftime("%Y-%m-%dT%H:%M:%S.000Z", gmtime())
      unitid = getunitid(client)
      batwarnupperTemp = int(client.read_input("Battery temperature warning upper limit")) + 273
      batwarnlowerTemp = int(client.read_input("Battery temperature warning lower limit")) + 273
      pvVolts = client.read_input("Charging equipment input voltage")
      pvAmps = client.read_input("Charging equipment input current")
      pvpower = client.read_input("Charging equipment input power")
      batVolts = client.read_input("Charging equipment output voltage")
      batchgAmps = client.read_input("Charging equipment output current")
      batchgpower = client.read_input("Charging equipment output power")
      #ldVolts = client.read_input("Discharging equipment output voltage")
      ldAmps = client.read_input("Discharging equipment output current")
      ldpower = client.read_input("Discharging equipment output power")
      ldnetAmps = client.read_input("Battery Current")
      batTemp = int(client.read_input("Battery Temp.")) + 273
      soc = float(client.read_input("Battery SOC"))/100
      chgmodeint = int(client.read_input("Charging mode"))
      #result = client.read_input_registers(0x3201,1,unit =1)
      chgeqstat = client.read_input("Charging equipment status")
      # mask = (1)
      # chgrunning = int(chgeqstat) & mask
      # #print 'running:', bool(chgrunning)
      # mask  = (1 << 2)
      # chgfault = int(chgeqstat) & mask
      # #print 'chargerfault:',bool(chgfault)
      mask = (3 << 2)
      chgstat = int(chgeqstat) & mask
      chgstat = chgstat >> 2
      class chgstate(enum.Enum):
        other = 0
        float = 1
        bulk = 2
        equalize = 3
          
      # SK = {}
      SK = {'updates':[{'$source':'OPserial.epsolar','timestamp':timestamp,'values':[
      {'path':'electrical.solar.'+unitid+'.voltage','value':round(batVolts, 2)}
      ,{'path':'electrical.solar.'+unitid+'.current','value':round(batchgAmps,2)}
      ,{'path':'electrical.solar.'+unitid+'.power','value':round(batchgpower,2)}
      ,{'path':'electrical.solar.'+unitid+'.panelVoltage','value':round(pvVolts,2)}
      ,{'path':'electrical.solar.'+unitid+'.panelCurrent','value':round(pvAmps,2)}
      ,{'path':'electrical.solar.'+unitid+'.panelpower','value':round(pvpower,2)}
      ,{'path':'electrical.solar.'+unitid+'.loadCurrent','value':round(ldAmps,2)}
      ,{'path':'electrical.solar.'+unitid+'.loadPower','value':round(ldpower,2)}
      ,{'path':'electrical.solar.'+unitid+'.loadnet.current','value':round(ldnetAmps,2)}
      ,{'path':'electrical.solar.'+unitid+'.chargingMode','value':chgstate(chgstat).name}
      ,{'path':'electrical.solar.'+unitid+'.controllerMode','value':chgmode(chgmodeint).name}
      ,{'path':'electrical.batteries.'+unitid+'.temperature','value':batTemp}
      ,{'path':'electrical.batteries.'+unitid+'.temperature.faultUpper','value':round(batwarnupperTemp,2)}
      ,{'path':'electrical.batteries.'+unitid+'.temperature.faultLower','value':round(batwarnlowerTemp,2)}
      ,{'path':'electrical.batteries.'+unitid+'.capacity.stateOfCharge','value':soc}
      ]}]}
      
      # print (SK)
      sys.stdout.write(ujson.dumps(SK))
      sys.stdout.write('\n')
      sys.stdout.flush()
      # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      # sock.sendto(ujson.dumps(SK), ('localhost', 55559))
      
      # sock.close()
      sleep(5)
    except KeyboardInterrupt:
      raise SystemExit
  else:
    return

def startjob(client):
  process = multiprocessing.Process(target=readunit, args=(client,))
  process.daemon = True
  jobs.append(process)
  process.start() 

def stopjobs(jobs):
  for job in jobs:
    job.terminate()
    job.join()
    jobs.remove(job)

ports = getports()
#ports = ['/dev/ttyXRUSB0']
# main Loop
while True:
  try:
    for line in iter(sys.stdin.readline, b''):
      try:
        data = ujson.loads(line)
        with open('datadump.txt', 'w') as outfile:  
          ujson.dumps(data, outfile, indent=4, sort_keys=True)
        # print 'data udumps',data
        if jobs:
          stopjobs(jobs)
          for client in clients:
            client.close
            clients=[]
        else:
          for port in ports:
            client = createclient(port)
            setupclient(client,data)
            startjob(client)
              
      except AssertionError as error:
        sys.stderr.write(error)
        sys.stderr.write('error parsing json\n')
        sys.stderr.write(line)
        sleep(1)
        # print 'no line'
  except KeyboardInterrupt:
    running = False
    sys.stderr.write("exit")
    sys.stderr.write('\n')
    sys.stderr.flush()
    if jobs:
          stopjobs(jobs)
          for client in clients:
            client.close
          clients=[] 
    sys.exit()
  
