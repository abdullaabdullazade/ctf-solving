"""
Şifrələnmə üç üsülu var.

Encode: Xüsusi alqoritmlə şifrələnir oxumaq və şifrələmək üçün keyə ehtiyac yoxdur.


Encryption: Keylə şifrələnir və Keylə oxunur.

Demək, iki hissəyə bölünür.

Symmetric

Alqoritm, public key olur. Onunla şifrələnir, və açılanda da o keylə açılır.


Asymmetric:
Alqoritm, public key və private key olur. public keylə şifrələnir,
və açılanda da o private key açılır.



Hashing:

Şifrələnir recovery mümkün deyil.(Bruteforce bəlkə)


"""

"""

Encryption Symmentic encryption

"""


import base64


data = "salam"

print(data.encode())

encoded = base64.b64encode(data.encode())
decoded = base64.b64decode(encoded).decode()

print("Encoded:", encoded)
print("Decoded:", decoded)

"""

Hashing


"""

import hashlib

message = "abdulla"
hash_object = hashlib.sha256(message.encode())
print("SHA-256:", hash_object.hexdigest())  # sha256 encoding edir.


"""

Encryption AES - public key

"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16)

data = b"abdullaxows"  # -> encode data
cipher = AES.new(key, AES.MODE_CBC)
iv = cipher.iv  # important for decypting - key
ct_bytes = cipher.encrypt(pad(data, AES.block_size))

print("Pass: ", ct_bytes.hex())


cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher_decrypt.decrypt(ct_bytes), AES.block_size)

print(pt.decode())


"""

RSA Testing - Asymmentic public and private


"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

message = b"abdullaxows"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

print("Şifrələnmiş:", ciphertext.hex())
print("Açılmış:", plaintext.decode())


"""

RSA - Dignature
Ahahah jwt kimi check edir
"""


from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

message = b"abdullaxows"

signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256(),
)

try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )
    print("✅ İmza DOĞRUDUR!")
except Exception as e:
    print("❌ İmza YALANDIR!", str(e))




"""
Hydra syntax:

hydra -l admin -P passwords.txt ftp://10.10.10.10



JohntoRipper syntax:

john --wordlist=rockyou.txt hash.txt



hashcat -m 0 -a 0 hash.txt rockyou.txt

-m - mode-u hashin hashcat examplesdən baxa bilərəm



1. Dictionary Attack üçün

rockyou.txt-i esasdir

rainbow tables hazir hash listidir


sosial engineering:
Phishing, Pretexting
"""

