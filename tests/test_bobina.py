import pigpio
import time

PIN = 17

pi = pigpio.pi()

pi.set_PWM_frequency(PIN, 10000)
pi.set_PWM_dutycycle(PIN, 128)

try:
	while True:
		time.sleep(1)
	
except KeyboardInterrupt:
	print("Saliendo...")
finally:
	 pi.set_PWM_dutycycle(PIN, 0)
	 pi.stop()
			
