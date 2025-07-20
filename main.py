import json
import json
import os
from chaotic_keygen import chaotic_key
from aes_cfb_encryptor import encrypt, decrypt
from time_lock import time_lock_decrypt
from intrusion_detection import log_intrusion
from file_integrity_checker import file_hash
from reverse_shell import launch_reverse_shell
from vpn_scrambler import scramble_vpn
from ip_geolocator import get_ip_info
from logger import secure_log

try:
    with open("config.json") as f:
        config = json.load(f)
except FileNotFoundError:
    secure_log("Missing config.json. Exiting.")
    exit(1)

key = chaotic_key(0.7219)

# Encrypt a file
try:
    with open("input.txt", "rb") as f:
        data = f.read()
    enc = encrypt(data, key)
    with open(config["encrypted_output"], "wb") as f:
        f.write(enc)
except Exception as e:
    secure_log(f"Encryption failed: {e}")

# Simulate intrusion
log_intrusion()

# Optional: scramble VPN if enabled
if os.getenv("ENABLE_VPN_SCRAMBLE") == "1":
    scramble_vpn()

# Optional: launch reverse shell
if os.getenv("ENABLE_SHELL") == "1":
    launch_reverse_shell()

secure_log("Intrusion response triggered")
