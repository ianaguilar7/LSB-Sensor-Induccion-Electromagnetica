import RPi.GPIO as GPIO
import time

PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:
	while True:
		print(1)
		GPIO.output(PIN, GPIO.HIGH)
		time.sleep(1)
		print(4)
		GPIO.output(PIN, GPIO.LOW)
		time.sleep(3)
	
except KeyboardInterrupt:
	print(1)
finally:
	 GPIO.cleanup()
			
