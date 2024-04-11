import gmpy2
import requests

def factorize_with_factordb(n):
    url = f"http://factordb.com/api?query={n}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'FF':  # 'FF' indicates Fully Factored
            factors = [int(factor[0]) for factor in data['factors']]
            return factors
    else:
        print(f"FactorDB request failed (status code: {response.status_code})")

    return None

c = 28822365203577929536184039125870638440692316100772583657817939349051546473185
n = 70736025239265239976315088690174594021646654881626421461009089480870633400973
e = 3

p, q = factorize_with_factordb(n)

if p and q:
    print(f"Factors of {n}: p is {p} and q is {q}")
else:
    # Manual result from factorDB (in case of no internet/random error)
    p = 238324208831434331628131715304428889871
    q = 296805874594538235115008173244022912163


phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
message = gmpy2.powmod(c, d, n)

print()
print("RESULT:")
# NOTE: it should be bytearray(b'small_numbers_are_not_safe')

print(bytearray.fromhex(hex(message)[2:]))

