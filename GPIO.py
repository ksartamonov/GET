import time
from string import zfill
import RPi.GPIO as GPIO 

#---------------------------------------------------

GPIO.setmode(GPIO.BCM)  
chan_list = [24, 25, 8, 7, 12, 16, 20, 21]
GPIO.setup(chan_list, GPIO.OUT)

#---------------------------------------------------
    
def PIN_to_number(ledNumber):
    return chan_list[ledNumber]

#---------------------------------------------------

def OffLight():
    for i in range (0, 8):
        GPIO.output(PIN_to_number(i), 0)
    
#---------------------------------------------------

def lightUp(ledNumber, period):
    ledNumber = PIN_to_number(ledNumber)
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    GPIO.output(ledNumber, 0)

#---------------------------------------------------

def darkUp(ledNumber, period):
    ledNumber = PIN_to_number(ledNumber)
    GPIO.output(ledNumber, 0)
    time.sleep(period)
    GPIO.output(ledNumber, 1)

#---------------------------------------------------

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range (0, blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)

#---------------------------------------------------

def runningLight(count, period):
    for i in range(0, count):
        for j in range(0, 8):
            lightUp(j, period)

#---------------------------------------------------

def runningDark(count, period):
    for i in range(0, 8):
        GPIO.output(PIN_to_number(i), 1)
    for i in range(0, count):
        for j in range(0, 8):
            darkUp(j, period)

#---------------------------------------------------

def decToBinList(decNumber):
    b = 1
    a = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, 8):
        if (b & (decNumber >> i) == 1):
            a[7 - i] = 1

    return a

#---------------------------------------------------

def lightNumber(number):
    bin_list = decToBinList(number)
    for i in range (0, 8):
        GPIO.output(PIN_to_number(i), bin_list[7 - i]) 
    time.sleep(0.1)
    OffLight()

#---------------------------------------------------

def runningPattern(pattern, direction):
    lightNumber(pattern)
    for i in range (0, abs(direction)):
        lightNumber(pattern)
        time.sleep(0.1)
        if (direction > 0):
            b = pattern % 2
            pattern = pattern >> 1
            pattern = pattern + b * 128
        if (direction < 0):
            b = pattern % 128
            pattern = pattern << 1
            pattern = pattern + b * 2


OffLight()
#---------------------------------------------------
# BLINK FUNCTION

# print("ENTER LED NUMBER")
# ledNumber = int(input())
# #direction = int(input())
# #decToBinList(ledNumber)
# print("ENTER BLINK COUNT")
# blinkCount = int(input())
# print("PERIOD")
# blinkPeriod = int(input())
# blink(ledNumber, blinkCount, blinkPeriod)

#-----------------------------------------------------
#RUNNING FUNCTION

# print("ENTER THE AMOUNT OF RUNNING CYCLES")
# count = int(input())
# print("PERIOD")
# period = int(input())
# runningLight(count, period)
# runningDark(count, period)

#-----------------------------------------------------

#LIGHT NUMBER

# print("ENTER THE NUMBER")
# number = int(input())
# lightNumber(number)

#-----------------------------------------------------

#RUNNING PATTERN
print("ENTER THE PATTERN")
pattern = int(input())
print("ENTER THE DIRECTION")
direction = int(input())

runningPattern(pattern, direction)

#-----------------------------------------------------

OffLight()

