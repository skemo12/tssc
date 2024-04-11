#!/usr/bin/python3

import crypt


password = "nustiu"

salt = "1234"

hash = crypt.crypt(password, salt)

print(hash)
