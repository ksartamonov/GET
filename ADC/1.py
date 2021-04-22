import RPi.GPIO as GPIO
import time

num_bits = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

D = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.output(17, 1)
GPIO.output(D[:], 0)



def decToBinList(decNumber):
    decNumber = decNumber % 256
    N = num_bits - 1
    bits = []
    while N > 0:
        if ( int(decNumber/(2**N)) == 1 ):
            bits.append(1)
            decNumber -= 2**N
        else:
            bits.append(0)
        N -= 1
    bits.append(decNumber)
    return bits

def num2dac(value):
    bits = decToBinList(value)
    for i in range (0, num_bits):
        GPIO.output(D[i], bits[num_bits - (i + 1)])

def transfer(value):
	return ((value % 256) * 3.3 / 255)

try:
	while True:
		num = int(input("Enter value (-1 to exit) > "))
		if(num < 0):
			if(num == -1):
				exit()
			print("You entered the incorrect number! Quiting the progtam!")
			exit()
		else:
			num2dac(num)
			print(num ,"=", transfer(num))
except ValueError:
		print("You entered incorrect data type! Quiting the progtam!")
		exit()
except KeyboardInterrupt:
	print("\n############################################")
	print("# The program is stopped by the user! #")
	print("############################################\n")
	exit()
finally:
	GPIO.cleanup()
