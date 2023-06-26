converter = DataConverter()

hex_data = '1A2B3C'
binary_data = converter.hex_to_binary(hex_data)
print(binary_data)  # Output: 000110100010101100111100

converted_hex_data = converter.binary_to_hex(binary_data)
print(converted_hex_data)  # Output: 1a2b3c

string_data = converter.hex_to_string(hex_data)
print(string_data)  # Output: '��<'

converted_hex_data = converter.string_to_hex(string_data)
print(converted_hex_data)  # Output: 1a2b3c

machine_language = converter.hex_to_machine_language(hex_data)
print(machine_language)  # Output: '\x1a+<'

converted_hex_data = converter.machine_language_to_hex(machine_language)
print(converted_hex_data)  # Output: 1a2b3c

mips_code = converter.hex_to_mips(hex_data)
print(mips_code)  # Output: 0x1A2B3C

converted_hex_data = converter.mips_to_hex(mips_code)
print(converted_hex_data)  # Output: 1a2b3c

dec_data = converter.hex_to_dec(hex_data)
print(dec_data)  # Output: 17150076

converted_hex_data = converter.dec_to_hex(dec_data)
print(converted_hex_data)  # Output: 1a2b3c

motorola_code = converter.hex_to_motorola(hex_data)
print(motorola_code)  # Output: :020000041A2B3C

converted_hex_data = converter.motorola_to_hex(motorola_code)
print(converted_hex_data)  # Output: 1A2B3C

gcode = converter.hex_to_gcode(hex_data)
print(gcode)  # Output: M98 P1A\nM98 P2B\nM98 P3C\n

converted_hex_data = converter.gcode_to_hex(gcode)
print(converted_hex_data)  # Output: 1A2B3C

mazatrol_code = converter.hex_to_mazatrol(hex_data)
print(mazatrol_code)
# Output: PROGRAM\n01234567;\n

converted_hex_data = converter.mazatrol_to_hex(mazatrol_code)
print(converted_hex_data)
# Output: 01234567

data = 'Hello, World!'
file_name = 'data.txt'
converter.save_to_file(data, file_name)

read_data = converter.read_from_file(file_name)
print(read_data)  # Output: 'Hello, World!'
