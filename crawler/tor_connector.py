# crawler/tor_connector.py (improved)
from stem.control import Controller
import requests
import time
import socket

def get_session():
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return session

def check_port_open(host='127.0.0.1', port=9051, timeout=2):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False

def renew_tor_identity(max_retries=3, wait_between=5):
    if not check_port_open():
        print("[!] Tor control port (9051) is not open. Is Tor running?")
        return False

    for attempt in range(1, max_retries + 1):
        try:
            with Controller.from_port(port=9051) as controller:
                controller.authenticate()
                controller.signal('NEWNYM')
                print(f"[+] Tor identity renewed (attempt {attempt})")
                time.sleep(wait_between)
                return True
        except Exception as e:
            print(f"[!] Tor renewal failed (attempt {attempt}): {e}")
            time.sleep(wait_between)

    print("[X] Tor identity renewal failed after multiple attempts.")
    return False
