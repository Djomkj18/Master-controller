import math
import network
from esp import espnow
from machine import Pin
from time import sleep

# Function gives sensors specific names on the basis of their converted integer addresses
def name_sensor(int_val):
    
    if (int_val == 162988747986800):
        temp_sensor_name = "Sensor 1"

    if (int_val == 162988747987816):
        temp_sensor_name = "Sensor 2"
        
    if (int_val == 162988747990804):
        temp_sensor_name = "Sensor 3"
    
    """
    if (int_val == ):
        temp_sensor_name = "Sensor 4"
        
    if (int_val == ):
        temp_sensor_name = "Sensor 5"
        
    if (int_val == ):
        temp_sensor_name = "Sensor 6"
    """
    return temp_sensor_name   



#Adding components to master's communication protocol
def add_peer(comp_list):
    
    for peers in comp_list:
        e.add_peer(comp_list[peers])



# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)
w0.active(True)

# ESP protocol initalization
e = espnow.ESPNow()
e.init()

# MAC addresses of temperature sensors' wifi interfaces
temp_sensors = { 'temp_sensor_1' : b'\x94\x3c\xc6\x6d\x17\x70', 'temp_sensor_2' : b'\x94\x3c\xc6\x6d\x1b\x68',
                 'temp_sensor_3' : b'\x94\x3c\xc6\x6d\x27\x14'
                 }
                 
""", 'temp_sensor_4' : b'\x94\x3c\xc6\x6d',
'temp_sensor_5' : b'\x94\x3c\xc6\x6d', 'temp_sensor_6' : b'\x94\x3c\xc6\x6d'} """

# MAC addresses of relays' wifi interfaces
relays = {'relay_1' : b'\x94\x3c\xc6\x6d\x15\x40' } #, 'relay_2' : b'\x94\x3c\xc6\x6d', 'relay_3' : b'\x94\x3c\xc6\x6d', 'relay_4' : b'\x94\x3c\xc6\x6d' }

#Adding temperature sensors and relays to master's communication protocol
add_peer(temp_sensors)
add_peer(relays)

relay_conection = 0

while True:
    
    relay_conection += 1
    host, msg = e.irecv()     # Available on ESP32 and ESP8266
    
    if msg:                   # msg == None if timeout in irecv()
        
        host_conv_val = int.from_bytes(host, "big")
        sensor_name = name_sensor(host_conv_val)
        
        sensor_data = int(msg.decode("utf-8"))
        print(str(sensor_name) + ":")
        print("Current temperature =", sensor_data, "\n\n")
        
    if relay_conection == 20:
        
        e.send(relay, str(relay_conection), True)
        relay_conection = 0
        print("Relay signal sent")
        



