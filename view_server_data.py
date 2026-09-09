import json


with open("server_history.json", "r") as file:
    old_data = json.load(file)

server_list = old_data

for server in server_list:
    if 'id' in server:
        print(server['id'] ,"|", server['name'] ,"|", server['cpu'])