#!/usr/bin/python
import sys
import json
import random
import time

# Configuration mode: return the custom metrics data should be defined
def config():
    settings = {
        "maxruntime": 5000,  # How long the script is allowed to run
        "period": 60,  # The period the script will run, in this case it will run every 60 seconds
        "metrics": [
            {
                "id": 0,
                "datatype": "DOUBLE",
                "name": "Server load",
                "description": "Calculated number showing load of environment",
                "groups": "Statistics",
                "unit": "",
                "tags": "",
                "calctype": "Instant"
            },
            {
                "id": 1,
                "datatype": "DOUBLE",
                "name": "Number of active connections",
                "description": "Number of active connections",
                "groups": "Statistics",
                "unit": "",
                "tags": "",
                "calctype": "Instant"
            },
            {
                "id": 2,
                "datatype": "DOUBLE",
                "name": "Application memory usage",
                "description": "Current application memory usage",
                "groups": "Statistics",
                "unit": "",
                "tags": "",
                "calctype": "Instant"
            }
        ]
    }

    print json.dumps(settings)

# Data retrieval mode: return the data for the custom metrics
def data():
    offset = 1487691852
    now = int(time.time()) - offset

    print "M1 %s" % (abs(
        1800 - (now % 3600)
    ) + random.randint(-50, 50)
    + (
        int(
            now / 3600
        ) * 100
    ))

    print "M2 %s" % ((now / 2) + random.randint(-5000, 5000))

    print "M3 %s" % (now % 172800 + random.randint(-1000, 1000))

# Switch to check in which mode the script is running
if __name__ == "__main__":
    if sys.argv[1] == '-c':
        config()
    if sys.argv[1] == '-d':
        data()
