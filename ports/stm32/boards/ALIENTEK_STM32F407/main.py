# main.py
# test script

import pyb
import time

# turn on an LED
led_red = pyb.LED(1)
led_green = pyb.LED(2)
led_red.on()
led_green.off()

loop = 1;
while loop < 10:
    led_red.toggle()
    led_green.toggle()
    time.sleep_ms(200)
    loop+=1

    # print some text to the serial console
    print('Hello MicroPython!')

led_red.off()
led_green.off()


####
from pyb import Pin, Timer, time

p = Pin('PF_9') # TIM14, CH1
tim = Timer(14, freq=1000)
ch = tim.channel(1, Timer.PWM, pin=p)
per = 0;
while 1:
    per += 1
    ch.pulse_width_percent(per)
    time.sleep_ms(10)
    if per == 100:
        per = 0
    

####
from pyb import Pin, Timer, time

p = Pin('PF_9') # TIM14, CH1
tim = Timer(14, freq=1000)
ch = tim.channel(1, Timer.PWM, pin=p)
adj = 1
per = 0
while 1:
    per += adj
    ch.pulse_width_percent(per)
    time.sleep_ms(10)
    if per == 100:
        adj = -1
    if per == 0:
        adj = 1


####
import time
from pyb import Pin, Timer

p = Pin('PA_6') # TIM3, CH1
tim = Timer(3, freq=50)
ch = tim.channel(1, Timer.PWM, pin=p)
adj = 1
per = 0
while 1:
    per += adj
    ch.pulse_width_percent(per)
    time.sleep_ms(40)
    if per == 25:
        adj = -1
    if per == 0:
        adj = 1


from pyb import Servo;
s2 = Servo(2)

    
