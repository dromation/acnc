import can

def check_cnc_connection():
    # Specify the CAN bus interface and its baud rate
    bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=250000)
    
    # Define the CAN message to send to the CNC machine
    can_msg = can.Message(arbitration_id=0x123, is_extended_id=False, data=[0x01, 0x02, 0x03])
    
    try:
        # Send the CAN message to the CNC machine
        bus.send(can_msg)
        
        # Wait for a response from the CNC machine
        response = bus.recv(timeout=1)
        
        if response is not None:
            # If a response is received, the CNC machine is connected
            print("CNC machine is connected")
        else:
            # If no response is received, the CNC machine is not connected
            print("CNC machine is not connected")
            
    except can.CanError:
        # If there is an error sending or receiving the CAN message, the CNC machine is not connected
        print("CNC machine is not connected")
