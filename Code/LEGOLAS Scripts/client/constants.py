"""
Constants moved to dedicated file, QoL for end-user modification
"""

import numpy as np

PI1_MAP = {
    "motor" : {
        "y" : "C",
    },
    "force_sensor": {
        "x" : "D",
        "y" : "B",
    }
}

PI2_MAP = {
    "motor" : {
        "x" : "C",
        "syringe_plunger" : "D",
        "syringe_z" : "B",
        "pH_z" : "A"
    }
}

# use "python -m serial.tools.list_ports -v" to check connected port
# or "ls /dev/tty*" and find anything end with ACM
PH_SERIAL = "/dev/ttyACM0"

