import binascii

plaintext = "FIRE_NUKES_MELA!"
target = "SEND_NUDES_MELA!"
b_plaintext = plaintext.encode('utf-8')
b_target = target.encode('utf-8')

difference = bytearray()
for i in range(len(b_plaintext)):
    difference.append(b_plaintext[i] ^ b_target[i])

iv_hex = "7ec00bc6fd663984c1b6c6fd95ceeef1"
b_iv = binascii.unhexlify(iv_hex)

target_iv = bytearray()
for i in range(len(b_iv)):
    target_iv.append(b_iv[i] ^ difference[i])

result = binascii.hexlify(target_iv).decode('utf-8')

print("Result:", result)
