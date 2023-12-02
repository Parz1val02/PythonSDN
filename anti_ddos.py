import requests
import json
ip_to_switch_map = {}
controller_ip = "localhost"
controller_port = "8080"
controller_url = f"http://{controller_ip}:{controller_port}"

# Function to update the global dictionary
def update_ip_to_switch_mapping():
    global ip_to_switch_map

    sw_dpid_ip= 'wm/core/controller/switches/json' 
    api = f"{controller_url}/{sw_dpid_ip}"
    headers = {'Content-type': 'application/json','Accept': 'application/json'}
    response = requests.get(url=api, headers=headers)

    if response.status_code == 200:
        print('SUCCESSFUL REQUEST | STATUS: 200')
        json_data = response.json()
        # Iterate through each item in the list
        for item in json_data:
            # Access values using keys
            inet_address = item['inetAddress']
            connected_since = item['connectedSince']
            switch_dpid = item['switchDPID']
            print(f"InetAddress: {inet_address}, Connected Since: {connected_since}, Switch DPID: {switch_dpid}")
    else:
        print(f"Error: {response.status_code}")
        ip_to_switch_map[ip_address] = switch_id

# Function to retrieve switch ID for a given IP address
def get_switch_id_for_ip(ip_address):
    global ip_to_switch_map
    return ip_to_switch_map.get(ip_address, None)


if __name__ == '__main__':
    update_ip_to_switch_mapping()