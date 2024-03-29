import atexit
import os
import re
import readline
import rlcompleter
import socket
import _socket
import sys
import time
import timeit

history = os.path.expanduser('~/.python_history')
readline.read_history_file(history)
readline.parse_and_bind('tab: complete')
atexit.register(readline.write_history_file, history)

def t(*args):
       return timeit.Timer(*args).timeit()
