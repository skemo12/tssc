from Crypto.Cipher import AES

BLOCK_SIZE = 32
PADDING = b'#'
iv = b"\x00" * 16

def decrypt_data(key, iv, data):
    aes = AES.new(key, AES.MODE_CBC, iv)
    data = aes.decrypt(data)
    return data

with open('isc-lab02-secret.enc', 'rb') as f:
    data = f.read()

key = data[:BLOCK_SIZE]
enc = data[BLOCK_SIZE:]
dec_data = decrypt_data(key, iv, enc).rstrip(PADDING)

with open('isc-lab02-secret.jpg', 'wb') as out:
    out.write(dec_data)