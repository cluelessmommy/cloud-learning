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
    #health status check
    print("================================")
    print("       SERVER HEALTH STATUS")
    print("================================")

    if cpu < 80:
        print("CPU is healthy")
    else:
        print("CPU need attention")

    if memory < 80:
        print("Memory is healthy")
    else:
        print("Memory need attention")

    if disk < 80:
      print("Disk is healthy")
    else:
      print("Disk need attention") 
    
    

for i in range(3):
    cpu, memory, disk = get_server_info()
    get_server_health_status(cpu, memory, disk)
    time.sleep(5)



    