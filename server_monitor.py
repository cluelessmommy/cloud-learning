import psutil
import time
from datetime import datetime

def get_server_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    return cpu, memory, disk

def get_server_health_status(server):


    print(f"CPU: {cpu}")
    print(f"MEMORY: {memory}")
    print(f"DISK: {disk}")


    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("================================")
    print("       SERVER HEALTH CHECK")
    print("       Time:", current_time)
    print("================================")

    THRESHOLD = 80
    if cpu < THRESHOLD and memory < THRESHOLD and disk < THRESHOLD:
       # print("SERVER HEALTH STATUS: HEALTHY")
        return "HEALTHY"
    else:
        #print("SERVER HEALTH STATUS: CRITICAL")
        return "CRITICAL"   

for i in range(3):
    cpu, memory, disk = get_server_info()
    server = {
        "cpu" : cpu,
        "memory" : memory,
        "disk" : disk
    }

    status = get_server_health_status(server)

    server.update({"status": status})
    print(f"Server Health Status: {server['status']}")
    time.sleep(5)



    