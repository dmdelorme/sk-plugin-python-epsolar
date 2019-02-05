# -*- coding: iso-8859-15 -*-

from datetime import datetime

# import the server implementation
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.mei_message import *
from pyepsolartracer.registers2 import registerByName

# ---------------------------------------------------------------------------#
# Logging
# ---------------------------------------------------------------------------#
import logging

_logger = logging.getLogger(__name__)


class EPsolarTracerClient:
    ''' EPsolar Tracer client
    '''

    def __init__(self, unit=1, serialclient=None, **kwargs):
        ''' Initialize a serial client instance
        '''
        self.unit = unit
        if serialclient == None:
            port = kwargs.get('port', '/dev/ttyXRUSB0')
            baudrate = kwargs.get('baudrate', 115200)
            self.client = ModbusClient(method='rtu', port=port, baudrate=baudrate, kwargs=kwargs)
        else:
            self.client = serialclient

    def connect(self):
        ''' Connect to the serial
        :returns: True if connection succeeded, False otherwise
        '''
        return self.client.connect()

    def close(self):
        ''' Closes the underlying connection
        '''
        return self.client.close()

    def read_device_info(self):
        request = ReadDeviceInformationRequest(unit=self.unit)
        response = self.client.execute(request)
        return response

    def read_input(self, name):
        register = registerByName(name)
        if register.is_coil():
            response = self.client.read_coils(register.address, register.size, unit=self.unit)
        elif register.is_discrete_input():
            response = self.client.read_discrete_inputs(register.address, register.size, unit=self.unit)
        elif register.is_input_register():
            response = self.client.read_input_registers(register.address, register.size, unit=self.unit)
        else:
            response = self.client.read_holding_registers(register.address, register.size, unit=self.unit)
        return register.decode(response)

    def write_output(self, name, value):
        register = registerByName(name)
        values = register.encode(value)
        response = False
        if register.is_coil():
            self.client.write_coil(register.address, values, unit=self.unit)
            response = True
        elif register.is_discrete_input():
            _logger.error("Cannot write discrete input " + repr(name))
            pass
        elif register.is_input_register():
            _logger.error("Cannot write input register " + repr(name))
            pass
        else:
            self.client.write_registers(register.address, values, unit=self.unit)
            response = True
        return response

    def read_rtc(self):
        register = registerByName('Real time clock 1')
        size_address = 3
        result = self.client.read_holding_registers(register.address, size_address, unit=self.unit)
        return self.decode_rtc(result.registers)

    def write_rtc(self, datetime):
        register = registerByName('Real time clock 1')
        values = self.encode_rtc(datetime)
        self.client.write_registers(register.address, values, unit=self.unit)
        return True

    def decode_rtc(self, rtc):
        s = 2000
        sec_min = rtc[0]
        hour_day = rtc[1]
        month_year = rtc[2]
        secs = (sec_min & 0xff)
        hour = (hour_day & 0xff)
        month = (month_year & 0xff)
        minut = sec_min >> 8
        day = hour_day >> 8
        year = month_year >> 8
        return datetime(s + year, month, day, hour, minut, secs)

    def encode_rtc(self, datetime):
        s = 2000
        rtc1 = int((datetime.minute << 8) | datetime.second)
        rtc2 = int((datetime.day << 8) | datetime.hour)
        rtc3 = int((datetime.year - s << 8) | datetime.month)
        return [rtc1, rtc2, rtc3]

    def encode(self, value):
        # FIXME handle 2 word registers
        rawvalue = int(value * self.times)
        if rawvalue < 0:
            rawvalue = (-rawvalue - 1) ^ 0xffff
            # print rawvalue
        return rawvalue


__all__ = [
    "EPsolarTracerClient",
]
