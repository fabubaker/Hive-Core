"""
Common utilities for Hive runtimes.
"""

from datetime import datetime

def printt(string):
    '''
    print function that always prefixes current datetime.
    '''
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print "[%s] %s" % (now, string)
