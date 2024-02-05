#
# ncclient
#
import xmltodict
import json
from ncclient import manager

device = {
    "host": "clab-ceos-eos01",
    "port": 830,  # Default Netconf port
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "default"},
    "allow_agent": False,
    "look_for_keys": False,
}

# Establishing a NETCONF session
with manager.connect(**device) as m:
    print("Connected to the device")
    config = m.get_config(source="running")
    # print(config.xml)
    config_dict = xmltodict.parse(config.xml)
    # print(config_dict)
    print(json.dumps(config_dict, indent=2))
