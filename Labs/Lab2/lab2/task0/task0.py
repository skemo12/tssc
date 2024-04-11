output_file="fixed.bmp"
new_header_hex = '424D66CAD700000000003600000028000000D007000035090000010018000000000030CAD70074120000741200000000000000000000'
file_path = 'isc-lab02-encrypted.bmp'

# Convert the hex string into a byte array
new_header_bytes = bytes.fromhex(new_header_hex)

# Read the file's contents (make sure to do this in binary mode)
with open(file_path, 'rb') as f:
    data = f.read()

# Find the start of the existing header (assuming it starts with "BM")
header_start = 0

# Calculate the end of the existing header
header_end = header_start + len(new_header_bytes)

# Replace the header
new_data = data[:header_start] + new_header_bytes + data[header_end:]

# Save the modified file
with open(output_file, 'wb') as f:
    f.write(new_data)


