import psutil
import time
from datetime import datetime
import json

THRESHOLD = 80

def get_server_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    server = {
        "name" : "Codespace Server",
        "cpu" : cpu,
        "memory" : memory,
        "disk" : disk
    }
    return server

def get_server_health_status(server):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("================================")
    print("       SERVER HEALTH CHECK")
    print("       Time:", current_time)
    print("================================")

    print(f"NAME: {server['name']}")
    print(f"CPU: {server['cpu']}")
    print(f"MEMORY: {server['memory']}")
    print(f"DISK: {server['disk']}")





    if server['cpu'] < THRESHOLD and server['memory'] < THRESHOLD and server['disk'] < THRESHOLD:
       # print("SERVER HEALTH STATUS: HEALTHY")
        return "HEALTHY"
    else:
        #print("SERVER HEALTH STATUS: CRITICAL")
        return "CRITICAL"   

with open("server_history.json", "r") as file:
    old_data = json.load(file)

server_list = old_data
print(f"Length of Server List:", len(server_list))

for i in range(3):
    server = get_server_info()

    #server_python = json.loads(server_json)
    #print(server_python)


    status = get_server_health_status(server)

    server.update({"status": status})
    server_json = json.dumps(server)
    print(f"Server Health: {server['status']}")
    server_list.append(server)

    print(server_json)
    time.sleep(5)

print(f"Length of Server List:", len(server_list))

with open("server_history.json", "w") as file:
    json.dump(server_list, file, indent=4)

