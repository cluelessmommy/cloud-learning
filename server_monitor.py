import psutil
import time
from datetime import datetime



for i in range(3):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Time:", current_time)
    print("================================")
    print("       SERVER HEALTH CHECK")
    print("================================")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    cpu_count = psutil.cpu_count(logical=True)
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    print(f"Number of CPU: {cpu_count}")
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
    
    time.sleep(5)

