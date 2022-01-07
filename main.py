#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create objects.
ev3 = EV3Brick()
us1 = UltrasonicSensor(Port.S4)
us2 = UltrasonicSensor(Port.S3)
motor = Motor(Port.B)
sw = StopWatch()
StopWatch.pause(sw)
StopWatch.reset(sw)
print('Ready to go....')
ev3.light.on(Color.ORANGE)
wait(1000)
ev3.speaker.say('Ready to go!')
# Check for US1 to be triggered. Loop ends when US1 is triggered
while us1.distance() > 300:
    wait(1)    

StopWatch.resume(sw)

print('Sensor 1 crossed')
# Check for US2 to be triggered. Loop ends when US2 is triggered.
while us2.distance() > 300:
    wait(1)
    ts2 = StopWatch.time(sw)
print('Sensor 2 crossed')

# Define time.
difftime = ts2
print('difftime = ', difftime)

# Calculate and read out speed.
speed = ((11.25/12) / difftime) * (3600*1000/5280)
print('speed = ', speed, 'mph')
new_speed = round(speed, 2)
str_new_speed = str(new_speed)+'miles per hour'
print(new_speed)
ev3.speaker.say(str_new_speed)
wait(1000)

# Wave flag.
motor.run(180)
wait(900)
motor.run(-180)
wait(900)
motor.run(180)
wait(900)
motor.run(-180)
wait(675)
motor.hold()
