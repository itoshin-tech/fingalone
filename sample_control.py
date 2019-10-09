# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import numpy as np
import cv2

A1_GPIO = 23
A2_GPIO = 24
A3_GPIO = 25

RNG_DIG = np.array([-90, 90])
RNG_RATE = np.array([2.5, 12])

def mapping(x, rx, ry):
    a = (ry[0] - ry[1]) / (rx[0] - rx[1])
    b = ry[0] - a * rx[0]
    y = a * x + b
    return y

A1 = 0
dA1 = 10
A2 = 0
dA2 = 10
A3 = 0
dA3 = 10

GPIO.setmode(GPIO.BCM)

GPIO.setup(A1_GPIO, GPIO.OUT)
p1 = GPIO.PWM(A1_GPIO, 50)

GPIO.setup(A2_GPIO, GPIO.OUT)
p2 = GPIO.PWM(A2_GPIO, 50)

GPIO.setup(A3_GPIO, GPIO.OUT)
p3 = GPIO.PWM(A3_GPIO, 50)
p1.start(0)
p2.start(0)
p3.start(0)

img = np.zeros((100, 100, 3), dtype = np.uint8)

while True:
    d1 = mapping(A1, RNG_DIG, RNG_RATE)
    d2 = mapping(A2, RNG_DIG, RNG_RATE)
    d3 = mapping(A3, RNG_DIG, RNG_RATE)
    cv2.imshow('img', img)
    p1.ChangeDutyCycle(d1)
    p2.ChangeDutyCycle(d2)
    p3.ChangeDutyCycle(d3)
    
    INPUT = cv2.waitKey(100) & 0xFF
    if INPUT == ord('q'):
        break
    if INPUT == ord('u'):
        A1 += dA1
        if A1 > RNG_DIG[1]:
            A1 = RNG_DIG[1]
        print('A1', A1)
    if INPUT == ord('j'):
        A1 -= dA1
        if A1 < RNG_DIG[0]:
            A1 = RNG_DIG[0]
        print('A1', A1)
        
    if INPUT == ord('i'):
        A2 += dA2
        if A2 > RNG_DIG[1]:
            A2 = RNG_DIG[1]
        print('A2', A2)
    if INPUT == ord('k'):
        A2 -= dA2
        if A2 < RNG_DIG[0]:
            A2 = RNG_DIG[0]
        print('A2', A2)
        
    if INPUT == ord('o'):
        A3 += dA3
        if A3 > RNG_DIG[1]:
            A3 = RNG_DIG[1]
        print('A3', A3)
    if INPUT == ord('l'):
        A3 -= dA3
        if A3 < RNG_DIG[0]:
            A3 = RNG_DIG[0]
        print('A3', A3)

p1.stop()
p2.stop()
p3.stop()
GPIO.cleanup()
