import psutil
import time
from datetime import datetime

THRESHOLD = 80

def get_server_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    server = {
        "cpu" : cpu,
        "memory" : memory,
        "disk" : disk
    }
    return server

def get_server_health_status(server):


    print(f"CPU: {server['cpu']}")
    print(f"MEMORY: {server['memory']}")
    print(f"DISK: {server['disk']}")


    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("================================")
    print("       SERVER HEALTH CHECK")
    print("       Time:", current_time)
    print("================================")


    if server['cpu'] < THRESHOLD and server['memory'] < THRESHOLD and server['disk'] < THRESHOLD:
       # print("SERVER HEALTH STATUS: HEALTHY")
        return "HEALTHY"
    else:
        #print("SERVER HEALTH STATUS: CRITICAL")
        return "CRITICAL"   

for i in range(3):
    server = get_server_info()


    status = get_server_health_status(server)

    server.update({"status": status})
    print(f"Server Health Status: {server['status']}")
    time.sleep(5)



    