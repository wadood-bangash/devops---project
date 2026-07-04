import psutil
import datetime

def monitor():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    log = f"[{datetime.datetime.now()}] CPU: {cpu}% | RAM: {ram}% | DISK: {disk}%\n"
    
    with open("health.log", "a") as f:
        f.write(log)
    
    if cpu > 80 or ram > 80 or disk > 80:
        print("⚠️ ALERT: System overloaded!")
    
    print("✅ Script ran successfully!")
    print(log)

if __name__ == "__main__":
    monitor()
