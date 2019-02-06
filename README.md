# sk-plugin-python-epsolar
## This work is based on several other peoples work
https://github.com/riptideio/pymodbus

https://github.com/kasbert/epsolar-tracer

https://github.com/pelom/tenergy-api

https://github.com/SignalK/sk-plugin-python-demo

![Epsolar Tracer](/img/epsolar_tracer_bn.jpg)

![epsolar tracer BN](url)

It is designed to send and recive data from epsolar charge controllers several versions to a SignalK server.
### The xr_usb_serial_common_1a driver needs to be installed as per instutions in folder.
Test by plugging in the USB cable from epsolartracer
* 'ls /dev/tty*' 

You should see.

* '/dev/ttyXRUSB0' to 3 depending on the number of controlers. 

Install the Modbus python module
 * pip install  -U pymodbus 

I need some feed back to make this all work for other people.. 

Install all needed python modules. It been a while so give me feed back on this.
I belive pymodbus, pluse what ever is included in the pulgin.py.
Demonstration of a SK server plugin in Python
Follow instructions below to install
## Development

- clone the plugin from GitHub
- `npm link` in the plugin directory
- `npm link sk-plugin-python-epsolar` in your server directory

