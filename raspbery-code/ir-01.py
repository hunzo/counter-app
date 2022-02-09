#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import requests

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

GPIO_SENSOR_1 = 4
GPIO.setup(GPIO_SENSOR_1, GPIO.IN)

GPIO_SENSOR_2 = 27
GPIO.setup(GPIO_SENSOR_2, GPIO.IN)

GPIO_LED_1 = 2
GPIO.setup(GPIO_LED_1, GPIO.OUT)
GPIO.output(GPIO_LED_1, False)

GPIO_LED_2 = 22
GPIO.setup(GPIO_LED_2, GPIO.OUT)
GPIO.output(GPIO_LED_2, False)


GPIO_RELAY = 17
GPIO.setup(GPIO_RELAY, GPIO.OUT)


DELAY = 1

def CallApi():
    print('Call Api Counter')
    r = requests.get('http://hcloud.nida.ac.th:8082/api/inc?key=123456')
    print(r.json())

def OpenRelay():
    GPIO.output(GPIO_RELAY, True)
    print('Relay Open')

def CloseRelay():
    GPIO.output(GPIO_RELAY, False)
    print('Closed Relay')

def OnLED1():
    GPIO.output(GPIO_LED_1, True)
def OffLED1():
    GPIO.output(GPIO_LED_1, False)

def OnLED2():
    GPIO.output(GPIO_LED_2, True)
def OffLED2():
    GPIO.output(GPIO_LED_2, False)

CHK_SS1 = 1
CHK_SS2 = 1

def SetSS1():
    global CHK_SS1
    CHK_SS1 = 0

def SetSS2():
    global CHK_SS2
    CHK_SS2 = 0

def ClearSS():
    global CHK_SS1
    global CHK_SS2
    CHK_SS1 = 1
    CHK_SS2 = 1

def WaitLoop():
    wait = True
    while wait:
        SENSOR_1 = GPIO.input(GPIO_SENSOR_1)
        # print('Wait Loop')
        if SENSOR_1 == 1:
            wait = False
            CallApi()
            CloseRelay()

if __name__ == '__main__':
    print('Start')
    try:
        while True:
            SENSOR_1 = GPIO.input(GPIO_SENSOR_1)
            # print('Main Loop')
            if SENSOR_1 == 1:
                OffLED1()

            if SENSOR_1 == 0:
                OnLED1()
                OpenRelay()
                print('CHECK !!')
                WaitLoop()

            time.sleep(0.01)

    except KeyBoardInterrupt:
        print('Stop')
    finally:
        GPIO.cleanup()
