#!/usr/bin/env python3
# Script to f3tch t3h fl4gz0rx

import base64
import json
import socket
from Crypto.Cipher import AES
from Crypto.Util import number
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import pad, unpad

AES_BLOCK_SIZE = 32
AES_KEY_SIZE = 32

HOST = "isc2023.1337.cx"
PORT = 11008


def get_aes_key(shared_num, salt):
    bnum = shared_num.to_bytes((shared_num.bit_length() + 7) // 8, byteorder="big")
    return scrypt(bnum, salt, AES_BLOCK_SIZE, N=2**14, r=8, p=1)


def decrypt_aes(msg, key):
    aes = AES.new(key, AES.MODE_ECB)
    data = aes.decrypt(msg)
    return data


def get_dict(data, begin=True):
    """Function to extract the dict from the data

    Args:
        data (bytes): bytes to extract the dict from begin (bool, optional):
        Whether it's the first string byte (the hello/welcome) or the response
        after sending the number. Defaults to True.

    Returns:
        Dict: Dictionary with the received data
    """
    if not isinstance(data, str):
        decoded_data = data.decode()
    else:
        decoded_data = data

    if begin:
        extracted_data = (
            (decoded_data.split("BEGIN_HANDSHAKE"))[1]
            .split("INPUT_YOUR_NUMBER: ")[0]
            .replace("\n", "")
        )
    else:
        extracted_data = (
            (decoded_data.split("OKAY! BEGIN_MESSAGE"))[1]
            .split("Connection closed by foreign host.")[0]
            .replace("\n", "")
        )
    print(extracted_data)
    message = base64.b64decode(extracted_data)
    return json.loads(message)


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(4096)

        kwargs = get_dict(data)
        print(kwargs)

        b = number.getRandomInteger(16)

        print(b)
        B = kwargs["g"] ** b % kwargs["p"]

        snd = str(B) + "\n"
        print("\nB is\n" + snd)
        s.send(snd.encode())

        response = s.recv(4096)
        resp_kwargs = get_dict(response, begin=False)

        for k in resp_kwargs:
            resp_kwargs[k] = base64.b64decode(resp_kwargs[k])

        print("\nObtained dict:")
        print(resp_kwargs)

        shared_num = kwargs["A"] ** b % kwargs["p"]
        print("\nShared num:")
        print(shared_num)


        aes_key = get_aes_key(shared_num, resp_kwargs["salt"])
        decrypted_message = decrypt_aes(resp_kwargs["msg"], aes_key)

        print("\nDecrypted message:")
        print(decrypted_message.decode())
