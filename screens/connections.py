import kivy
from kivymd.uix.widget import MDWidget
from kivymd.uix.boxlayout import MDBoxLayout
from pymodbus.client.sync import ModbusTcpClient
import serial
from pymodbus.client.sync import ModbusSerialClient

# Set the IP address and port number of the Modbus server
SERVER_IP = '192.168.1.100'
SERVER_PORT = 502

# Create a Modbus TCP client instance
client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT)

# Connect to the Modbus server
client.connect()

# Now you can send Modbus requests using the client instance, for example:
# response = client.read_holding_registers(address=0, count=1, unit=1)

# Remember to close the connection when you're done
client.close()

class Connections(self):
    pass

    def cmodbus(self):
        # Set the IP address and port number of the Modbus server
        SERVER_IP = '192.168.1.100'
        SERVER_PORT = 502

        # Create a Modbus TCP client instance
        client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT)

        # Connect to the Modbus server
        client.connect()

        # Now you can send Modbus requests using the client instance, for example:
        # response = client.read_holding_registers(address=0, count=1, unit=1)

        # Remember to close the connection when you're done
        client.close()

    def rs232(self):
        # Configure the serial port
        ser = serial.Serial(
            port='/dev/ttyUSB0',  # or COM1 on Windows
            baudrate=9600,
            bytesize=8,
            parity='N',
            stopbits=1
        )

        # Create a Modbus RTU client
        client = ModbusSerialClient(method='rtu', port=ser, timeout=1, baudrate=9600)

        # Open the connection
        if not client.connect():
            print("Failed to connect to Modbus device")

        # Perform Modbus operations here...

        # Close the connection
        client.close()
        
class modbusc(self):
    from modbus_tk import modbus_tcp
    from modbus_tk.defines import ModbusMasterException
    import time

    # Define the IP address and port of the CNC machine
    HOST = "192.168.1.100"
    PORT = 502

    # Initialize the Modbus TCP client
    client = modbus_tcp.TcpMaster(host=HOST, port=PORT)

    # Connect to the CNC machine
    try:
        client.open()
        print("Connected to CNC machine at {}:{}".format(HOST, PORT))
    except ModbusMasterException as e:
        print("Error connecting to CNC machine:", e)

    # Read holding registers from the CNC machine
    try:
        # Define the starting address and number of registers to read
        start_address = 0
        num_registers = 10
        
        # Read the holding registers and print the values
        response = client.read_holding_registers(start_address, num_registers)
        values = response[:num_registers]
        print("Read {} holding registers starting at address {}: {}".format(num_registers, start_address, values))
    except ModbusMasterException as e:
        print("Error reading holding registers:", e)

    # Write to holding registers on the CNC machine
    try:
        # Define the starting address and values to write
        start_address = 10
        values = [1, 2, 3, 4]
        
        # Write the values to the holding registers
        client.write_multiple_registers(start_address, values)
        print("Wrote {} values to holding registers starting at address {}".format(len(values), start_address))
    except ModbusMasterException as e:
        print("Error writing to holding registers:", e)

    # Disconnect from the CNC machine
    try:
        client.close()
        print("Disconnected from CNC machine at {}:{}".format(HOST, PORT))
    except ModbusMasterException as e:
        print("Error disconnecting from CNC machine:", e)

