class ConnectionDetector:
    def __init__(self):
        self.connection_modules = {
            'USB': ['usb_module1', 'usb_module2', 'usb_module3'],
            'Ethernet': ['ethernet_module1', 'ethernet_module2'],
            'RS232': ['rs232_module1', 'rs232_module2'],
            'RS485': ['rs485_module1'],
            'CAN': ['can_module1', 'can_module2'],
            'TCP/IP': ['tcpip_module1', 'tcpip_module2']
            # Add more connection protocols and their corresponding modules as needed
        }

    def check_modules(self):
        missing_modules = {}
        for connection_protocol, modules in self.connection_modules.items():
            missing = []
            for module in modules:
                if not self.is_module_present(module):
                    missing.append(module)
            if missing:
                missing_modules[connection_protocol] = missing
        return missing_modules

    def is_module_present(self, module):
        # Implement the logic to check if the module is present
        # Return True if the module is present, False otherwise
        # Replace the following line with your specific implementation
        return module in installed_modules

    def report_missing_modules(self, missing_modules):
        if not missing_modules:
            print("All modules are present.")
        else:
            print("Missing modules:")
            for connection_protocol, modules in missing_modules.items():
                print(f"Connection Protocol: {connection_protocol}")
                print("Modules:")
                for module in modules:
                    print(f"- {module}")


connection_detector = ConnectionDetector()
missing_modules = connection_detector.check_modules()
connection_detector.report_missing_modules(missing_modules)
