"""
Utility functions for Hive Seekers.
"""

from util import printt

def handle_app_ping(socket):
    """Short function to handle an app ping.
    Mostly for debugging."""
    identity = socket.recv()
    msg = socket.recv()
    printt("Message from %s:" % identity)
    printt("`%s`" % msg)
    socket.send_multipart([identity, msg])

