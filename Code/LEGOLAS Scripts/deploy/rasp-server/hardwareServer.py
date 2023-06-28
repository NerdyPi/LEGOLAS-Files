"""
This program will act as the software responsible for managing autonomous functionality of LEGOLAS

RPyC sessions will attach to this server, which will expose various functions to be accessed by a client

Major difference between this software architechture and the previous version will be that LEGOLAS software
can continue operation, even without an active RPyC connection. RPyC connections can access the "API" provided
by this server, but hardware operation will not be dependent upon it.

For the purposes of safety, the client will retain the ability to reset the hardware server manually, and
motor-controlling halts can be implemented programmatically through the provided API
"""

import connectionManager
import fiducialSystem
import serialGateway


import rpyc
from rpyc.utils.server import ThreadedServer

RPYC_PORT = 0 # TODO


"""
This class defines a 'service' for RPyC, which allows for explicit definition of
exposed functionality to the client
"""
class HardwareService(rpyc.Service):
    def test():
        print("test")

def main():
    instanceService = HardwareService()
    server = ThreadedServer(instanceService, port=RPYC_PORT)
    server.start() # Blocking, later structure should not rely on RPyC persistence 
                   # (though service should stay open ideally) TODO

if __name__ == "__main__":
    main()