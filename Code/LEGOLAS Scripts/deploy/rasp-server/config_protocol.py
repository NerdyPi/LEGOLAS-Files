"""
Found at 
https://github.com/sbcshop/PiSquare/blob/main/Run%20RaspberryPi%20HATs%20On%20PiSquare%20Using%20Sockets/Multiple%20Sockets/config_protocol.py
"""


class I2C_Socket():
    def I2C_Read(freq):
        ir = 'I2C'+ ','  + 'R' + ',' + freq
        return ir        
        

    def I2C_Write(freq,addr,data):
        wr = 'I2C' + ','  + 'W' + ',' + freq + ',' + addr + ',' + data
        return wr
    

class UART_Socket():
    def UART_Read(device):
        ur = 'UART'+','  + 'R' + ',' + device
        return ur
        
    def UART_Write(baud,data):
        uw = 'UART'+ ',' + baud + ','  + 'W' + ',' + data
        return uw


class GPIO_Socket():
    def GPIO_Read(gpio):
        gr = 'GPIO'+ ',' + gpio + ',' + 'R' 
        return gr
      

    def GPIO_Write(gpio,state):
        gw = 'GPIO'+ ',' + gpio + ',' + 'W' + ',' + state
        return gw
        
class SPI_Socket():
 
    def SPI_Read(device):
        sr = 'SPI'+','  + 'R' + ',' + device
        return sr
        
    def SPI_Write(device,data):
        sw = 'SPI'+ ',' + 'W' + ',' + device + ','  + data
        return sw