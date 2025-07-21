from rich.console import Console
from rich.table import Table
from time import sleep
import json
import os

LOG_FILE = "intrusion_log.txt"

def load_logs():
    logs = []
    if not os.path.exists(LOG_FILE):
        return logs

    with open(LOG_FILE, "r") as f:
        for line in f:
            try:
                entry = json.loads(line)
                ip = entry["intrusion_from"].get("ip", "Unknown")
                time = entry["timestamp"]
                status = entry.get("status", "Triggered")
                logs.append((ip, time, status))
            except json.JSONDecodeError:
                continue
    return logs

def display_dashboard():
    console = Console()
    prev_count = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.rule("[bold red]Chakravyuh SOC Dashboard 🛡️")
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("IP Address", width=20)
        table.add_column("Time of Attack", width=30)
        table.add_column("Status", style="green")

        logs = load_logs()
        for log in logs:
            table.add_row(*log)

        console.print(table)
        print(f"\n[Updated: {len(logs)} events loaded]")
        sleep(3)  # Refresh every 3 seconds

if __name__ == "__main__":
    display_dashboard()
