class DataConverter:
    def __init__(self):
        pass
    
    def hex_to_binary(self, hex_data):
        binary_data = bin(int(hex_data, 16))[2:].zfill(len(hex_data) * 4)
        return binary_data
    
    def binary_to_hex(self, binary_data):
        hex_data = hex(int(binary_data, 2))[2:]
        return hex_data
    
    def hex_to_string(self, hex_data):
        string_data = bytes.fromhex(hex_data).decode('utf-8')
        return string_data
    
    def string_to_hex(self, string_data):
        hex_data = string_data.encode('utf-8').hex()
        return hex_data
    
    def hex_to_machine_language(self, hex_data):
        machine_language = ''
        for i in range(0, len(hex_data), 2):
            opcode = hex_data[i:i+2]
            machine_language += chr(int(opcode, 16))
        return machine_language
    
    def machine_language_to_hex(self, machine_language):
        hex_data = ''
        for char in machine_language:
            hex_data += hex(ord(char))[2:].zfill(2)
        return hex_data
    
    def hex_to_mips(self, hex_data):
        mips_code = ''
        for i in range(0, len(hex_data), 8):
            instruction = hex_data[i:i+8]
            mips_code += f"0x{instruction}\n"  # Example format: 0x01234567
        return mips_code
    
    def mips_to_hex(self, mips_code):
        hex_data = ''
        instructions = mips_code.split('\n')
        for instruction in instructions:
            if instruction.startswith('0x'):
                hex_data += instruction[2:]
        return hex_data
    
    def hex_to_dec(self, hex_data):
        dec_data = str(int(hex_data, 16))
        return dec_data
    
    def dec_to_hex(self, dec_data):
        hex_data = hex(int(dec_data))[2:]
        return hex_data
    
    def hex_to_motorola(self, hex_data):
        motorola_code = ':02000004' + hex_data + '\n'  # Example format: :020000040123F9
        return motorola_code
    
    def motorola_to_hex(self, motorola_code):
        hex_data = motorola_code[10:-1]
        return hex_data
    
    def hex_to_gcode(self, hex_data):
        gcode = ''
        for i in range(0, len(hex_data), 2):
            byte = hex_data[i:i+2]
            gcode += f"M98 P{byte}\n"  # Example format: M98 P01
        return gcode
    
    def gcode_to_hex(self, gcode):
        hex_data = ''
        lines = gcode.split('\n')
        for line in lines:
            if line.startswith('M98 P'):
                byte = line[6:]
                hex_data += byte
        return hex_data
    
    def hex_to_mazatrol(self, hex_data):
        mazatrol_code = 'PROGRAM\n' + hex_data + ';\n'  # Example format: PROGRAM\n01234567;\n
        return mazatrol_code
    
    def mazatrol_to_hex(self, mazatrol_code):
        hex_data = mazatrol_code[9:-3]
        return hex_data
    
    def hex_to_ladder_logic(self, hex_data):
        ladder_logic = ''
        for i in range(0, len(hex_data), 4):
            rung = hex_data[i:i+4]
            ladder_logic += f"LD {rung}\n"  # Example format: LD 1234
        return ladder_logic
    
    def ladder_logic_to_hex(self, ladder_logic):
        hex_data = ''
        lines = ladder_logic.split('\n')
        for line in lines:
            if line.startswith('LD '):
                rung = line[3:]
                hex_data += rung
        return hex_data
    
    def save_to_file(self, data, file_name):
        with open(file_name, 'w') as file:
            file.write(data)
    
    def read_from_file(self, file_name):
        with open(file_name, 'r') as file:
            data = file.read()
        return data
