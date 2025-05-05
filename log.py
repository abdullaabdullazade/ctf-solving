cipher = "rcckuizufzxhznod"
cipher_bytes = cipher.encode()

print("Possible XOR decryptions:\n")
for key in range(1, 256):
    decrypted = ''.join(chr(b ^ key) for b in cipher_bytes)
    
    # Yalnız oxunaqlı ASCII olanları göstər
    if all(32 <= ord(c) < 127 for c in decrypted):
        print(f"Key {key:3}: {decrypted}")
