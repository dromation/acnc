import serial
import socket

# Check USB Connection
def check_usb_connection(port):
    try:
        ser = serial.Serial(port)
        ser.close()
        return True
    except:
        return False

# Check RS232 Connection
def check_rs232_connection(port, baudrate):
    try:
        ser = serial.Serial(port, baudrate)
        ser.close()
        return True
    except:
        return False

# Check TCP Connection
def check_tcp_connection(ip_address, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip_address, port))
        s.close()
        return True
    except:
        return False

# Test Signal
def test_signal(port, baudrate, signal):
    try:
        ser = serial.Serial(port, baudrate)
        ser.write(signal)
        ser.close()
        return True
    except:
        return False

# Test TCP Signal
def test_tcp_signal(ip_address, port, signal):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip_address, port))
        s.sendall(signal)
        s.close()
        return True
    except:
        return False

# Example usage
usb_port = '/dev/ttyUSB0'
rs232_port = '/dev/ttyS0'
baudrate = 9600
tcp_ip = '192.168.0.1'
tcp_port = 8080

# Check USB Connection
if check_usb_connection(usb_port):
    print("USB Connection established")
else:
    print("USB Connection failed")

# Check RS232 Connection
if check_rs232_connection(rs232_port, baudrate):
    print("RS232 Connection established")
else:
    print("RS232 Connection failed")

# Check TCP Connection
if check_tcp_connection(tcp_ip, tcp_port):
    print("TCP Connection established")
else:
    print("TCP Connection failed")

# Test Signal
signal = b'\x01\x02\x03'
if test_signal(rs232_port, baudrate, signal):
    print("RS232 Signal tested successfully")
else:
    print("RS232 Signal test failed")

# Test TCP Signal
if test_tcp_signal(tcp_ip, tcp_port, signal):
    print("TCP Signal tested successfully")
else:
    print("TCP Signal test failed")
