

def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)

def xor_bytes(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

def main():
    c1_hex = "200d1d2014071e152b1c1e022d2615100617112a0804"
    c2_hex = "20000035191102062C1016091334110B1703182A020D"

    c1 = hex_to_bytes(c1_hex)
    c2 = hex_to_bytes(c2_hex)

    crib = b"texsaw{"
    key = xor_bytes(c1[:len(crib)], crib)

    p1 = xor_bytes(c1[:len(key)], key)
    p2 = xor_bytes(c2[:len(key)], key)

    print("[+] Key (hex):", key.hex())
    print("[+] Decrypted P1:", p1.decode(errors='replace'))
    print("[+] Decrypted P2:", p2.decode(errors='replace'))

    if p1.startswith(b"texsaw{"):
        print("\n✅ FLAG:", p1.decode(errors='replace'))
    else:
        print("\n❌ Flag not found in P1.")

main()


"""
i use theflag chip
"""





def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)

def xor_bytes(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

def printable(b):
    return ''.join([chr(x) if 32 <= x <= 126 else '.' for x in b])

def crib_drag(xor_result, crib):
    crib_bytes = crib.encode()
    print(f"\n[*] Trying crib: {crib}")
    for i in range(len(xor_result) - len(crib_bytes) + 1):
        segment = xor_result[i:i+len(crib_bytes)]
        result = xor_bytes(segment, crib_bytes)
        print(f"Offset {i:02}: {result} -> {printable(result)}")

c1_hex = "200d1d2014071e152b1c1e022d2615100617112a0804"
c2_hex = "20000035191102062C1016091334110B1703182A020D"

c1 = hex_to_bytes(c1_hex)
c2 = hex_to_bytes(c2_hex)

xor_result = xor_bytes(c1, c2)

cribs = ["texsaw{", "theflag", "stream", "crypto", "plaintext", "message", "xor", "secret", "flag", "hidden"]
for crib in cribs:
    crib_drag(xor_result, crib)

"""
[*] Trying crib: theflag
Offset 00: b'texsaw{' -> texsaw{
Offset 01: b'yupkz}t' -> yupkz}t
Offset 02: b'i}hppr`' -> i}hppr`
Offset 03: b'aesz\x7ffk' -> aesz.fk
Offset 04: b'y~yukmo' -> y~yukmo
Offset 05: b'btva`il' -> btva`il
Offset 06: b'h{bjdjY' -> h{bjdjY
Offset 07: b'going_u' -> going_u
Offset 08: b'sdmmRsc' -> sdmmRsc
Offset 09: b'x`nX~e|' -> x`nX~e|
Offset 10: b'|c[thzv' -> |c[thzv
Offset 11: b'\x7fVwbwps' -> .Vwbwps
Offset 12: b'Jza}}un' -> Jza}}un
Offset 13: b'fl~wxhg' -> fl~wxhg
Offset 14: b'pstream' -> pstream
Offset 15: b'oyqolkn' -> oyqolkn

thesaw{going_upstream}


your link:

https://chatgpt.com/share/67fb71a4-fb50-8013-a3fe-92aadf587555
"""