"""
Client program to be executed on the PiSquare through MicroPython
"""

from machine import UART, Pin, SPI, I2C
from ssd1306 import SSD1306_I2C
import time, utime
import gpio_config
import random
import vga1_bold_16x32 as font

WiFi_SSID=''  # Wifi_SSID TODO
WiFi_password = ''      # WiFi Password TODO

"""
TODO
Setting here will hardlink PiHats to a corresponding Pi

Might need to figure out how to make this user-friendly. 
Physical connection between pi and pihat during a config session?
"""
TCP_ServerIP = ''   # IP of Computer on which TCP server is running TODO


Port = ''  # 12420 TCP Server Port TODO

uart = UART(1, 115200)           # Default Baud rate

WIDTH  = 128                                            # oled display width
HEIGHT = 32                                             # oled display height

i2c = I2C(1,freq=200000,sda=Pin(6),scl=Pin(7))
print(i2c)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
oled.fill(0)
oled.text("Client",30,0)
oled.show()
######## Function to send or receive commands and data

lst = []
 
def sendCMD(cmd,ack,timeout=2000):
    uart.write(cmd+'\r\n')
    t = utime.ticks_ms()
    while (utime.ticks_ms() - t) < timeout:
        s=uart.read()
        if(s != None):
            s=s.decode()
            print(s)
            
            if(s.find(ack) >= 0):
                return True
    return False
#####################################################

uart.write('+++')
time.sleep(1)
if(uart.any()>0):uart.read()
sendCMD("AT","OK")
sendCMD("AT+CWMODE=3","OK")
sendCMD("AT+CWJAP=\""+WiFi_SSID+"\",\""+WiFi_password+"\"","OK",20000)
sendCMD("AT+CIFSR","OK")

while True:
    sendCMD("AT+CIPSTART=\"TCP\",\""+TCP_ServerIP+"\","+Port,"OK",10000)
    sendCMD("AT+CIPMODE=1","OK")
    a = sendCMD("AT+CIPSEND",">")
    if a == True:
        break
 
while True:
    s=uart.read()   # receive data from server
    if(s != None):
            s =s.decode('utf-8','ignore')
            print(type(s))
            print("data = ",s)
            print(len(s))
            print(s)

            lst = list(s)
            l = ''.join(lst)
            p = l.split(',')
            print(p)
            pin_mode = p[0]
            oled.text(pin_mode,40,20)
            oled.show()

            if pin_mode == 'GPIO':
                gpio_pin   = p[1]
                mode     = p[2]
                if mode == 'R':
                   d = gpio_config.Digital_Pin_Read(gpio_pin)
                   print(d)
                   uart.write(str(d))
                if mode == 'W':
                   state    = p[3]
                   d = gpio_config.Digital_Pin_Write(gpio_pin,state)
                   uart.write('write done')                
            
            if pin_mode == 'UART':
                pin_mode = p[0]
                Mode     = p[1]
                device     = p[2]
                
                if Mode == 'R':
                    uart_1 = gpio_config.UART_Pin_Read(device)
                    print(uart_1)
                    if uart_1 is None:
                        uart.write("try again")
                    else:
                        uart.write(uart_1)
                
                if Mode == 'W':
                    Data = p[3]
                    uart_1 = gpio_config.UART_Pin_Write(Data)
                    if uart_1 is None:
                        uart.write("try again")
                    else:
                        uart.write(uart_1)
                    
            if pin_mode == 'I2C':
                pin_mode = p[0]
                Mode     = p[1]
                device     = p[2]
                
                if Mode == 'R':
                    i2c_1 = gpio_config.I2C_Pin_Read(device) 
                    print(i2c_1)
                    #uart.write(str(i2c_1))  # Send data to TCP server
                    '''
                    if len(i2c_1) == 0:
                          print("No i2c device !")
                          uart.write('No i2c device')
                    else:
                         print('i2c devices found:',len(i2c_1))
                    '''
                    if i2c_1 is None:
                        uart.write("try again")
                    else:
                        uart.write(str(i2c_1))
                                         

                    
                if Mode == 'W':
                    device = p[2]
                    Data     = p[3]
                    i2c_1 = gpio_config.I2C_Pin_Write(device,Data)
                    if i2c_1 is None:
                        uart.write("try again")
                    else:
                        uart.write('done')
                    
            if pin_mode == 'SPI':
                Mode     = p[1]
                device   = p[2]
                
                if Mode == 'R':
                    spi_1 = gpio_config.SPI_Pin_Read(device)
                    print(spi_1)
                    if spi_1 is None:
                        uart.write("try again")
                    else:
                        uart.write(spi_1)

                
                if Mode == 'W':
                    Data = str(p[3])
                    spi_1 = gpio_config.SPI_Pin_Write(device,Data)
                    print(spi_1)
                    if spi_1 is None:
                        uart.write("try again")
                    else:
                        uart.write(spi_1)
                    