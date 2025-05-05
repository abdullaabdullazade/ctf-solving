"""
Paramikonun istifadəsi maraqlıdır. CTF-də ssh ilə qoşularaq istənilən commandi
yerinə yetirə bilirik
"""


import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh.connect("47.237.14.185",username="root",password="AbdullaX1_3")
# stdin, stdout, stderr = ssh.exec_command("ls -la") 
# print(stdout.read().decode())


"""
Çox əla işləyir sadəcə bunları yazmaqla istənilən commandi etmək olur
"""


# from pwn import *

# conn = remote("example.ctf.site", 1234)
# conn.sendline(b"hello")
# print(conn.recvline())
# conn.close()

"""
tcp serverleri ucundur
"""
from scapy.all import *

packet = IP(dst="8.8.8.8")/ICMP()
response = sr1(packet, timeout=1)

if response:
    print("Cavab gəldi:", response.summary())
else:
    print("Cavab gəlmədi")


from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(Raw):
        payload = packet[Raw].load
        if b".pdf" in payload or b".exe" in payload:
            print("[!] Fayl ötürülməsi aşkarlandı!")
            print(payload)

sniff(filter="tcp port 80", prn=packet_callback, store=0)

