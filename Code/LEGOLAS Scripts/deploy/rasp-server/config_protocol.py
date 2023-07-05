"""
Found at 
https://github.com/sbcshop/PiSquare/blob/main/Run%20RaspberryPi%20HATs%20On%20PiSquare%20Using%20Sockets/Multiple%20Sockets/config_protocol.py
"""
    

class UART_Socket():
    def UART_Read(device):
        ur = 'UART'+','  + 'R' + ',' + device
        return ur
        
    def UART_Write(baud,data):
        uw = 'UART'+ ',' + 'W' + ','  + baud + ',' + data
        return uw

