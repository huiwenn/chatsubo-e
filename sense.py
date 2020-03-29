import pigpio
from time import sleep
pi = pigpio.pi()

while True:
	a = pi.read(23)
	print(a)
	sleep(0.5)