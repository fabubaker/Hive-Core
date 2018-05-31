"""
Executable runtime for a Hive Seeker.
Run this on hardware devices that wish to access the
collection of sensors on the Hive network.

Reads network and application information from a user-defined
.yaml file on startup.
"""


import argparse
import zmq
import yaml


from util import printt

DESCRIPTION = """Starts the Hive Seeker, using network
               info from user-defined .yaml files."""

USAGE = "seeker.py <network.yaml> <my_name> <ipc_port> <tcp_port>"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESCRIPTION,
                                     usage=USAGE)
    parser.add_argument("network_yaml", help="Network config .yaml file.")
    parser.add_argument("my_name", help="The name of this provider. \
                                        Must be a name from network.yaml")
    parser.add_argument("ipc_port", help="Port used to communicate with Hive apps.")
    parser.add_argument("tcp_port", help="Port used to communicate with Hive devices.")
    args = parser.parse_args()

    ctx = zmq.Context()
    devices = yaml.load(open(args.network_yaml))

    # Setup application server.
    app_socket = ctx.socket(zmq.ROUTER)
    app_socket.bind(args.ipc_port)
    poller = zmq.Poller()
    poll_sockets = [app_socket]

    # Setup device clients.
    for device in devices:
        # Ignore self.
        if device["name"] == args.my_name:
            continue

        if device["type"] == "QUEEN" or device["type"] == "PROVIDER":
            socket = ctx.socket(zmq.DEALER)
            socket.identity = args.my_name
            socket.connect("tcp://%s:%s" % (device["ip"], str(device["port"])))
            device["socket"] = socket

    printt ("Sockets ready. Listening...")
    while True:
        # Register sockets
        [poller.register(s, flags=zmq.POLLIN) for s in poll_sockets]

        read_sockets = dict(poller.poll())
