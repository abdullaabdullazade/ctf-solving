from pwn import *

def recover_key(xored_hex, known_plaintext):
    xored_bytes = bytes.fromhex(xored_hex)
    key = [''] * 5
    for i in range(len(known_plaintext)):
        key_index = i % 5
        xor_value = xored_bytes[i] ^ ord(known_plaintext[i])
        key[key_index] = chr(xor_value)
    return ''.join(key)

# 1. Serverə qoşul
conn = remote("10.10.28.125", 1337)

# 2. Gələn banneri oxu
banner = conn.recvuntil(b"What is the encryption key?").decode()
print(banner)

# 3. Flag 1-in HEX dəyərini ayır
import re
match = re.search(r"flag 1: ([0-9a-f]+)", banner)
hex_flag = match.group(1)

# 4. XOR açarını bərpa et
known_plaintext = "THM{thisisafakeflag}"
key = recover_key(hex_flag, known_plaintext)
print(f"🔑 Tapılan açar: {key}")

# 5. Açarı göndər
conn.sendline(key.encode())

# 6. Cavabı oxu
final = conn.recvall(timeout=3).decode()
print(f"\n🎉 Server cavabı:\n{final}")
