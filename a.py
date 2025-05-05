from sage.all import *

# Verilənləri yerləşdir:
n = 0x46dbd0780b618c8dea0dc6b13a47a5b40bca30b96ed5b15e1be1ffad2fbab901bd0e26c8f3e2fa80cf208e3ba936acb3eef98002459833f96901e1fedb5e97432e05d5ad892beea06a96c059b5c6652a2241bcdaf91ccb4320298868ed3e0929778030e0cce2316b7677cc5574676545aacdef446f078fc08b56415315750ce659fc61db73f633b47a1c874145dd8676e70079ab40587be81c4a9673ded5e61e11c705e45fb4a910a7a1be2b3c3d0af8555a7d9a7aa90d4e4ec0bceb14cdbb1e4c91e379fa6961411139306b6add555734feeb77d51b40e568185b20c141bb4d07b96a1944d187cf8b6019dcdcb27a7309839393e6a63cfaffb9f11d26b503df
e = 0x10001
c = 0x389d979c400a145704d5685bce1f65f642e66c2778e62a7d0519addef8c92d9df42677df805a4e99962b14fb5acd512a7ab65f811842547a1a6670f73b6232e8790887584884caa66dad345c6aeb559402c16990eed47212f0794e11972a1e92030b84663de7cd472ed85c98a6cc42f79f02f7243755f0950894c741740400d0c2c84c6bc1c0380a4ca16eab0ad7ccc3314174c96ecad28bbd364c4ea56e3bc8a7e62c3351307fd1ebe18d3f6e82d778d77e75677a858c4993e4df53ff4d38ce69427b5170631ded7c34d1cc907681a3252d159105891348b4ca84e811611f2f04e6fa2ef6e006e0855f939f41bddcb585777d14942c7f10b2fdd979515cba5f
partial_pxq = 0x643e09f2948d2df7b16ffe591ac61e2a57b4cca7ead6a49e10b52593e5f9eb28be9d17eec9f04b6295221968d8bbfb698f87fe6f64b243b5cfd8fcf428b2599bc7fe54dcc695e3fad9

BITS = 1024
EXTRA = 75
SHIFT = (BITS // 2 - EXTRA)
known_upper = partial_pxq << SHIFT
X = 2^EXTRA  # Axtarılan kökün maksimal dəyəri

# Polinom hazırlığı
PR.<x> = PolynomialRing(Zmod(n))
f = x + known_upper

# Coppersmith tətbiqi (kiçik köklərin axtarışı)
print("[*] Trying Coppersmith...")
roots = f.small_roots(X=X, beta=0.4)

if not roots:
    print("[-] No root found. Coppersmith failed.")
    exit()

for root in roots:
    pxq = known_upper + int(root)
    print(f"[+] Found p^q: {hex(pxq)}")

    # pxq = p ^ q, n = p * q → p və q üçün kvadrat tənlik qururuq:
    # x^2 - (pxq + n) * x + n = 0

    R.<y> = PolynomialRing(Zmod(n))
    g = y^2 - (pxq + n) * y + n
    sol = g.roots()

    for r, _ in sol:
        p = int(r)
        q = n // p
        if p * q == n:
            print(f"[+] Success!\np = {p}\nq = {q}")

            # RSA decryption
            phi = (p - 1)*(q - 1)
            d = inverse_mod(e, phi)
            m = power_mod(c, d, n)
            flag = bytes.fromhex(hex(m)[2:])
            print(f"[+] FLAG: {flag.decode(errors='ignore')}")
            break
