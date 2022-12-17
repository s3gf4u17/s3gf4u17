from machine import Pin
from time import sleep

pin0=Pin(6,Pin.OUT)
pin1=Pin(7,Pin.OUT)
pin2=Pin(8,Pin.OUT)
pin3=Pin(9,Pin.OUT)
pin4=Pin(10,Pin.OUT)
pin5=Pin(11,Pin.OUT)
pin6=Pin(12,Pin.OUT)
pin7=Pin(13,Pin.OUT)

pins=[pin0,pin1,pin2,pin3,pin4,pin5,pin6,pin7]

for pin in pins:
    pin.low()
    
i=0

while True:
    binary=bin(i)
    binary=binary.split("b")[1]
    a=len(binary)-1
    for b in binary:
        pins[a].value(int(b))
        a-=1
    print(binary)
    i+=1
    sleep(0.5)
