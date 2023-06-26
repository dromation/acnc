import socket
import usb.core
import usb.util
import serial
from scipy.signal import find_peaks
from pymodbus.client.sync import ModbusSerialClient
import serial.tools.list_ports



class signaltcp(self):

    # Define the CNC's IP address and port number
    cnc_ip = '192.168.0.100'
    cnc_port = 1234

    # Create a socket object and connect to the CNC
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((cnc_ip, cnc_port))
        print("Connected to CNC")
    except socket.error:
        print("Failed to connect to CNC")

    # Receive data from the CNC
    data = s.recv(1024)

    # Detect if the connection is established by finding peaks in the received data
    peaks, _ = find_peaks(data, height=1)

    if len(peaks) > 0:
        print("Connection established")
    else:
        print("Connection failed")


class signalusb(self):

    # Define the USB vendor and product IDs for the CNC
    vendor_id = 0x1234
    product_id = 0x5678

    # Find the USB device with the specified vendor and product IDs
    device = usb.core.find(idVendor=vendor_id, idProduct=product_id)

    # If the device is found, attempt to connect to it
    if device is not None:
        try:
            # Get an interface to the device
            interface = 0
            if device.is_kernel_driver_active(interface):
                device.detach_kernel_driver(interface)
            device.set_configuration()
            endpoint = device[0][(0,0)][0]
            
            # Receive data from the device
            data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)

            # Detect if the connection is established by finding peaks in the received data
            peaks, _ = find_peaks(data, height=1)

            if len(peaks) > 0:
                print("Connection established")
            else:
                print("Connection failed")
        
        except usb.core.USBError as e:
            print("USB communication error:", str(e))
        
    else:
        print("USB device not found")

class signalRS232(self):


    # Define the serial port settings for the CNC
    port = '/dev/ttyUSB0'
    baudrate = 9600
    parity = serial.PARITY_NONE
    stopbits = serial.STOPBITS_ONE
    bytesize = serial.EIGHTBITS

    # Open the serial port and establish a connection with the CNC
    ser = serial.Serial(port=port, baudrate=baudrate, parity=parity, stopbits=stopbits, bytesize=bytesize)
    ser.flushInput()

    # Receive data from the CNC
    data = ser.readline().strip()

    # Detect if the connection is established by finding peaks in the received data
    peaks, _ = find_peaks(data, height=1)

    if len(peaks) > 0:
        print("Connection established")
    else:
        print("Connection failed")


class USBSignalDetector:
    def __init__(self):
        self.device_found = False

    def detect_signal(self):
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            if "USB" in port.description:
                self.device_found = True
                print("USB device found on port:", port.device)
                break
        if not self.device_found:
            print("No USB device found.")


class ModbusSignalDetector:
    def __init__(self, port):
        self.client = ModbusSerialClient(method='rtu', port=port, baudrate=9600, timeout=1)

    def detect_signal(self):
        try:
            if self.client.connect():
                response = self.client.read_coils(address=0, count=1)
                if response.isError():
                    print("Error reading Modbus signal:", response)
                else:
                    print("Modbus signal detected.")
            else:
                print("Connection to Modbus device failed.")
        except Exception as e:
            print("Error while reading Modbus signal:", e)
        finally:
            self.client.close()
