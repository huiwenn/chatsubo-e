import pigpio
pi = pigpio.pi()

while True:
	a = pi.read(23)
	print(a)
	sleep(1)