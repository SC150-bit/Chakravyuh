import os
import platform

def scramble_vpn():
    os_type = platform.system()

    if os_type == "Windows":
        # Kill OpenVPN and WireGuard processes
        os.system("taskkill /F /IM openvpn.exe >nul 2>&1")
        os.system("taskkill /F /IM wireguard.exe >nul 2>&1")
        print("[+] VPN processes terminated on Windows.")

    elif os_type in ["Linux", "Darwin"]:
        # Linux or macOS: kill by process name
        os.system("pkill openvpn")
        os.system("pkill wg-quick")
        print("[+] VPN processes terminated on Linux/macOS.")

    else:
        print("[!] OS not recognized. Cannot scramble VPN.")
