"""
API to be used by applications running on the Hive middleware.
"""

import zmq

from util import printt

class Hive(object):
    def __init__(self, app_name, ipc_addr):
        """Boots up and connects a Hive provider instance"""
        self.name = app_name
        self.ctx = zmq.Context()
        self.socket = self.ctx.socket(zmq.DEALER)
        self.socket.identity = app_name
        self.socket.connect(ipc_addr)

    def ping(self, msg):
        """Sends a short message to the provider.
        Mostly for debugging."""
        printt("Sending `%s` to provider." % msg)
        self.socket.send(msg)
        printt("Message back from provider: `%s`" % self.socket.recv())

def boot(app_name, ipc_addr):
    """Boot up a Hive instance"""
    return Hive(app_name, ipc_addr)
