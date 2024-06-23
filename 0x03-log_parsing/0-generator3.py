#!/usr/bin/python3
"""Generator module that will be used to test the 0-stats script
"""


import random
import sys
from time import sleep
import datetime

sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" 401 724\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
    ))
sys.stdout.flush()
