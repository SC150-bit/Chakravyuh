import datetime

def secure_log(message: str):
    try:
        with open("secure_log.txt", "a") as f:
            f.write(f"[{datetime.datetime.now()}] {message}\n")
    except Exception as e:
        print(f"Log failed: {e}")