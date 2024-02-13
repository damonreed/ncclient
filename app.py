#
# netswarm app.py
#
import xmltodict
import json
from ncclient import manager


# get_all : get all state data from device
def get_state(device):
    # Establishing a NETCONF session
    with manager.connect(**device) as m:
        print("Connected to the device")
        state = m.get()
        state_dict = xmltodict.parse(state.xml)
        return state_dict


def get_config(device):
    # Establishing a NETCONF session
    with manager.connect(**device) as m:
        print("Connected to the device")
        config = m.get_config(source="running")
        config_dict = xmltodict.parse(config.xml)
        return config_dict


## Recursively print all keys in a dictionary, represent MIB-style =P
def print_keys(d, p=""):
    for k, v in d.items():
        if isinstance(v, dict):
            print(p + k)
            p += k + "."
            print_keys(v, p)
            p = ""
        else:
            print(p + k + " : " + str(v))
            p = ""


device = {
    "host": "172.20.20.3",
    "port": 830,  # Default Netconf port
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "default"},
    "allow_agent": False,
    "look_for_keys": False,
}

state = get_state(device)["rpc-reply"]["data"]["network-instances"]["network-instance"]

# print(state.keys())
# print_keys(state)
print(json.dumps(state, indent=2))

# print_keys(get_config(device))
