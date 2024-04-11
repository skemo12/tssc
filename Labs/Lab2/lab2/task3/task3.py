import re
use_nltk = True
try:
    import nltk
    from nltk.corpus import words
except:
    print("nltk is not installed")
    use_nltk = False


def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
    return plaintext

def custom_tokenizer(text):
    pattern = r"[-+_=<>,./ {}'\s]+"  # Matches your delimiters or whitespace
    return re.split(pattern, text)

def has_sense(text):
    word_list = custom_tokenizer(text)
    known_words = set(words.words())  # Basic English word set

    percent_known = (len([word for word in word_list if word in known_words]) / len(word_list)) * 100

    # You can add more checks and thresholds here
    if percent_known > 60:
        return True
    else:
        return False

ciphertext = "wAyk{mmAwjAuwpz AwmAqjn"


try:
    nltk.download('punkt')
    nltk.download('words')
except:
    use_nltk = False

print()
print("SOLVING:")
if not use_nltk:
    print("Manually searching the text")

# Iterate over all possible keys
for i in range(256):
    key = chr(i) * len(ciphertext)
    decrypted_text = decrypt(ciphertext, key)
    if use_nltk:
        if decrypted_text.isprintable() and has_sense(decrypted_text):
            print(decrypted_text)
    else:
        if decrypted_text.isprintable():
            # Manually find the decrypted string, result should be i_guess_it_kind>_is_otp
            print(decrypted_text)

if not use_nltk:
    print("Decrypted text should be i_guess_it_kind>_is_otp")
