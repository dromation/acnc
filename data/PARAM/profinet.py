import pyprofinet

class PROFINETConnection:
    def __init__(self, ip_address, rack=0, slot=1, timeout=5, max_attempts=3):
        self.ip_address = ip_address
        self.rack = rack
        self.slot = slot
        self.timeout = timeout
        self.max_attempts = max_attempts
        self.connection = None

    def connect(self):
        # Connect to the PROFINET device using the specified IP address, rack, and slot
        self.connection = pyprofinet.connect(
            self.ip_address, self.rack, self.slot, timeout=self.timeout, max_attempts=self.max_attempts
        )

    def disconnect(self):
        # Disconnect from the PROFINET device
        self.connection.disconnect()

    def read_data(self, address):
        # Read data from the specified PROFINET address
        return self.connection.read(address)

    def write_data(self, address, data):
        # Write data to the specified PROFINET address
        self.connection.write(address, data)

    def set_parameter(self, parameter, value):
        # Set a parameter on the PROFINET device
        self.connection.set_parameter(parameter, value)

    def get_parameter(self, parameter):
        # Get the current value of a parameter from the PROFINET device
        return self.connection.get_parameter(parameter)

    def set_timeout(self, timeout):
        # Set the connection timeout value
        self.timeout = timeout

    def set_max_attempts(self, max_attempts):
        # Set the maximum number of connection attempts
        self.max_attempts = max_attempts

# Usage example
profinet_connection = PROFINETConnection('192.168.1.100', rack=1, slot=2)  # Replace with the appropriate IP address, rack, and slot
profinet_connection.set_timeout(10)  # Set the connection timeout to 10 seconds
profinet_connection.set_max_attempts(5)  # Set the maximum connection attempts to 5
profinet_connection.connect()

# Set parameters
profinet_connection.set_parameter('param1', 100)
profinet_connection.set_parameter('param2', 'value2')

# Get parameters
param1_value = profinet_connection.get_parameter('param1')
param2_value = profinet_connection.get_parameter('param2')

# Perform data exchange
data = profinet_connection.read_data(0x123)
profinet_connection.write_data(0x456, b'\x01\x02\x03')

# Disconnect from the PROFINET device
profinet_connection.disconnect()
