import psutil
import time
from datetime import datetime

def get_server_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    return cpu, memory, disk

def get_server_health_status(cpu, memory, disk):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("================================")
    print("       SERVER HEALTH CHECK")
    print("       Time:", current_time)
    print("================================")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    #print(f"Number of CPU: {cpu_count}")
    THRESHOLD = 20
    if cpu < THRESHOLD and memory < THRESHOLD and disk < THRESHOLD:
       # print("SERVER HEALTH STATUS: HEALTHY")
        return "HEALTHY"
    else:
        #print("SERVER HEALTH STATUS: CRITICAL")
        return "CRITICAL"   

for i in range(3):
    cpu, memory, disk = get_server_info()
    status= get_server_health_status(cpu, memory, disk)
    print(f"Server Health Status: {status}")
    time.sleep(5)



    