import serial

ser = serial.Serial('COM3', 9600)  # Change 'COM3' to the correct port number and 9600 to the correct baud rate
ser.open()

ser.write(b'MACHINE_INFO\n')  # Change 'MACHINE_INFO' to the correct command for your CNC control driver

response = ser.readline()

if 'DRIVER_NAME' in response:
    print('CNC control driver connected!')
else:
    print('CNC control driver not detected.')

ser.close()
