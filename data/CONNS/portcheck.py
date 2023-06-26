import serial.tools.list_ports
import pycnc
from pymodbus.client.sync import ModbusSerialClient


"""
# List the available serial ports on the system
ports = list(serial.tools.list_ports.comports())

# Print the available ports to the console
for port in ports:
    print(port.device)

# Set the serial port for the CNC
cnc_port = '/dev/ttyUSB0'

# Establish a connection with the CNC using pycnc
cnc = pycnc.controller.CNC(cnc_port)

# Send a command to the CNC
cnc.write_command('G0 X0 Y0 Z0')

# Close the connection with the CNC
cnc.close()
"""

class cnc_check:
    def __init__(self):
        self.cnc_port = None
        self.cnc = None

    def detect_cnc_port(self):
        # List the available serial ports on the system
        ports = list(serial.tools.list_ports.comports())

        # Look for the CNC port in the available ports
        for port in ports:
            if 'CNC' in port.description:
                self.cnc_port = port.device
                break
        
        if self.cnc_port is None:
            print('No CNC port found!')
        else:
            print(f'CNC port found: {self.cnc_port}')

    def connect_to_cnc(self):
        if self.cnc_port is None:
            print('No CNC port detected!')
            return
        
        try:
            # Establish a connection with the CNC using pycnc
            self.cnc = pycnc.controller.CNC(self.cnc_port)
            print('Connected to CNC')
        except:
            print('Failed to connect to CNC')

    def send_command(self, command):
        if self.cnc is None:
            print('No CNC connection established!')
            return
        
        try:
            # Send a command to the CNC
            self.cnc.write_command(command)
            print(f'Sent command: {command}')
        except:
            print(f'Failed to send command: {command}')

    def disconnect_from_cnc(self):
        if self.cnc is None:
            print('No CNC connection established!')
            return
        
        # Close the connection with the CNC
        self.cnc.close()
        print('Disconnected from CNC')


class PymodbusPortDetector:
    def __init__(self, port_list):
        self.port_list = port_list
    
    def detect(self):
        available_ports = []
        for port in self.port_list:
            client = ModbusSerialClient(method='rtu', port=port, baudrate=9600, stopbits=1, bytesize=8, parity='N')
            try:
                client.connect()
                available_ports.append(port)
                client.close()
            except:
                pass
        return available_ports
