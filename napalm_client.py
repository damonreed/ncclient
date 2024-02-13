#
#
#

from napalm import get_network_driver

driver = get_network_driver("eos")

device = driver(
    hostname="172.20.20.3",
    username="admin",
    password="admin",
)

device.open()

commands = ["show ip route | json"]

results = device.cli(commands)

for result in results:
    print(result)
    print(results[result])
