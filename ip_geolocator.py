import requests

def get_ip_info(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        return r.json()
    except requests.RequestException as e:
        return {"error": str(e)}