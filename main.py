#!/usr/bin/python3
"""
Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Kian Li Wan Po 
Student Number: LWNKIA001
Prac: 1
Date: 28/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO

#initialize variables
max=0b111
num=0

#Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #Output pin mode
#Output
LED = [17,27,22] #Pins for the LEDs
GPIO.setup(LED[0], GPIO.OUT) #LED 1
GPIO.setup(LED[1], GPIO.OUT) #LED 2
GPIO.setup(LED[2], GPIO.OUT) #LED 3
#Input
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #btn 1
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #btn 2

def button_click(pin):
    global num
    global max 
    if pin==23: #if the click came from button 1
        if num<max: #ensures the number stays below 0b111
            num+=1
        else:
            num=0
    if pin==24: #if the click came from button 2
        if num>0:  #ensures the number stays +ve
            num-=1
        else:
            num=max
    temp=num
   
    counter=0
    for x in LED:   #sets all LEDs off, number runs=number of elements in the array
        GPIO.output(LED[counter], GPIO.LOW)
        counter+=1
    
    counter=0
    while temp!=0: #converts number to 1s and 0s
        if temp%2==1:
            GPIO.output(LED[counter], GPIO.HIGH) #Light on=1
        else:
            GPIO.output(LED[counter], GPIO.LOW) #Light off=0
        counter+=1
        temp=temp//2     
        
#Edge detection
GPIO.add_event_detect(23, GPIO.RISING, button_click,bouncetime=300)
GPIO.add_event_detect(24, GPIO.RISING, button_click, bouncetime=300)

def main():
    pass
    
# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        counter=0
        for x in LED:   #sets all LEDs off
            GPIO.output(LED[counter], GPIO.LOW)
            counter+=1
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
