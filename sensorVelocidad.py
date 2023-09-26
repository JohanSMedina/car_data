#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import time, math
from dataBase import changeOdometry

dist_meas = 0.00
km_per_hour = 0
rpm = 0
elapse = 0
sensor = 17
pulse = 0
pulseBefore = 0
start_timer = time.time()

def init_GPIO():					# initialize GPIO
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(sensor,GPIO.IN,GPIO.PUD_UP)

def calculate_elapse(channel):				# callback function
	global pulse,pulseBefore, start_timer, elapse
	pulseBefore = pulse
	pulse+=1							# increase pulse by 1 whenever interrupt occurred
	elapse = time.time() - start_timer		# elapse for every 1 complete rotation made!
	start_timer = time.time()				# let current time equals to start_timer

def calculate_speed(r_cm):
	global pulse,elapse,rpm,dist_km,dist_meas,km_per_sec,km_per_hour
	if elapse !=0 and elapse2 < 2:							# to avoid DivisionByZero error
		rpm = (1/elapse * 60)/4
		circ_cm = (2*math.pi)*r_cm			# calculate wheel circumference in CM
		dist_km = circ_cm/100000 			# convert cm to km
		km_per_sec = dist_km / elapse		# calculate KM/sec
		km_per_hour = (km_per_sec * 3600)/4	# calculate KM/h
		dist_meas = (dist_km*pulse)*250	# measure distance traverse in meter
		#return km_per_hour
	else:
		rpm=0
		km_per_hour=0

def init_interrupt():
	GPIO.add_event_detect(sensor, GPIO.FALLING, callback = calculate_elapse, bouncetime = 20)

init_GPIO()
init_interrupt()


while True:
	elapse2 = time.time() - start_timer
	calculate_speed(26)	# call this function with wheel radius as parameter
	#print("Velocidad: {:.3f}  RPMs: {:.3f}   Dist: {:.3f}".format(km_per_hour, rpm, dist_meas))
	#print("--------")
	changeOdometry(f"{km_per_hour:.3f}",f"{rpm:.3f}" ,f"{dist_meas:.3f}")