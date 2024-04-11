#!/usr/bin/python3

import grp
import hashlib
import os
import pyotp
import sys


PASSWORD_HASH = "13412ffd6149204f40e546ffa9fbd7124b410198a6ba3924f788622b929c8eb2"
TOTP_SECRET = "3TJOD4F55FKIFKNICO2NDWDPSLYCC4ZN" # TODO(7.1): Choose a secret!
# poochiedontsurf


def login():
    user = os.environ.get("PAM_USER")

    user_groups = [g.gr_name for g in grp.getgrall() if user in g.gr_mem]

    # TODO(6.1): We want this script to be used only for our special group of users.
    if "dani.mocanu" not in user_groups and not "top_10_manelisti" in user_groups:
        return False

    user_secret = input()
    user_password = user_secret

    # TODO(7.2): Extract the password and the TOTP. Hint: you know the length of the TOTP.
    TOTP_LENGTH = 6  # Standard TOTP length
    user_password = user_secret[:-TOTP_LENGTH]
    user_totp = user_secret[-TOTP_LENGTH:]


    # TODO(6.2): Calculate the hash of the provided password.
    user_hash = hashlib.sha256(user_password.encode('utf-8')).hexdigest()

    if user_hash != PASSWORD_HASH:
        print("Ai gresit buzunarul!")
        return False

    # TODO(7.3): Check the TOTP from the user and uncomment the code below.
    totp = pyotp.TOTP(TOTP_SECRET)
    totp_correct = totp.verify(user_totp)  # Verify the provided TOTP
    if not totp_correct:
        print("S-a rezolvat, nu se poate!")
        return False

    print("Ma distrez si bine fac!")
    return True


if __name__ == "__main__":
    sys.tracebacklimit = 0

    if not login():
        raise Exception("Python script rejected login: trying default authentication")
