import serial

class COMPortConnection:
    def __init__(self, port, baudrate, timeout=1, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.parity = parity
        self.stopbits = stopbits
        self.bytesize = bytesize
        self.serial_port = None

    def connect(self):
        self.serial_port = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=self.timeout,
            parity=self.parity,
            stopbits=self.stopbits,
            bytesize=self.bytesize
        )

    def send_data(self, data):
        if self.serial_port is None:
            raise Exception("Not connected to the COM port.")
        self.serial_port.write(data)

    def receive_data(self, num_bytes):
        if self.serial_port is None:
            raise Exception("Not connected to the COM port.")
        return self.serial_port.read(num_bytes)

    def close_connection(self):
        if self.serial_port is not None:
            self.serial_port.close()
            self.serial_port = Nonepi

if __name__ == '__main__':
    # Create an instance of the COMPortConnection class with custom settings
    com_connection = COMPortConnection('COM1', 9600, timeout=2, parity=serial.PARITY_EVEN)

    # Connect to the COM port
    com_connection.connect()

    # Send data through the COM port
    data = b'Hello, COM port!'
    com_connection.send_data(data)

    # Receive data from the COM port
    received_data = com_connection.receive_data(10)
    print("Received Data:", received_data.decode())

    # Close the connection
    com_connection.close_connection()
