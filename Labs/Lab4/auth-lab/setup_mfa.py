#!/usr/bin/python3

import pyotp
import pyqrcode


TOTP_SECRET = pyotp.random_base32()
print(TOTP_SECRET)
totp_auth = pyotp.totp.TOTP(TOTP_SECRET).provisioning_uri(
    name="Nicolae Guta", issuer_name="Lab ISC"
)

# TODO(2): Generate and display the setup QR code.
# Generate the QR code
qr_code = pyqrcode.create(totp_auth)

# Display in the terminal (simplistic)
print(qr_code.terminal(quiet_zone=1))