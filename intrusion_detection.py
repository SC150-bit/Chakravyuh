import platform
import uuid
import socket
import os
import datetime
import json
import webbrowser

DECOY_FILE = "decoy.html"

def get_fingerprint():
    return {
        "os": platform.system(),
        "mac": hex(uuid.getnode()),
        "cpu": platform.processor(),
        "hostname": socket.gethostname()
    }

def log_intrusion():
    try:
        fingerprint = get_fingerprint()
        log_entry = {
            "timestamp": str(datetime.datetime.now()),
            "intrusion_from": fingerprint
        }

        with open("intrusion_log.txt", "a") as f:
            f.write(json.dumps(log_entry, indent=2) + "\n")
        print("[+] Intrusion logged.")

        if os.path.exists(DECOY_FILE):
            webbrowser.open(DECOY_FILE)
            print(f"[+] Decoy launched: {DECOY_FILE}")
        else:
            print(f"[!] Decoy file not found: {DECOY_FILE}")

    except Exception as e:
        print(f"[!] Error in intrusion logging or decoy launch: {e}")
