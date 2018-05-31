"""
Utilities for Hive runtimes.
"""

from datetime import datetime

def printt(string):
    '''
    print function that always prefixes current datetime.
    '''
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print "[%s] %s" % (now, string)
