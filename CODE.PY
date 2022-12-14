from tkinter import *
import tkinter.font
import time
import RPi.GPIO as GPIO
from gpiozero import LED
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Code = {
'A' : '.-' ,
'B' : '-...' ,
'C' : '-.-.' ,
'D' : '-..' ,
'E' : '.' ,
'F' : '..-.' ,
'G' : '--.' ,
'H' : '....' ,
'I' : '..' ,
'J' : '.---' ,
'K' : '-.-' ,
'L' : '.-..' ,
'M' : '--' ,
'N' : '-.' ,
'O' : '---' ,
'P' : '.--.' ,
'Q' : '--.-' ,
'R' : '.-.' ,
'S' : '...' ,
'T' : '-' ,
'U' : '..-' ,
'V' : '...-' ,
'W' : '.--' ,
'X' : '-..-' ,
'Y' : '-.--' ,
'Z' : '--..'
}

LED = 24
GPIO.setup(LED, GPIO.OUT)

win = Tk()
win.title("Morse Converter")
Font_style = tkinter.font.Font( family = 'Cambaria', size = 20, weight = "bold")

def Dash_func():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.6)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.13)
    
def Dot_func():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.13)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.13)

def morse_code():
    TEXT = string_input.get() 
    for alphabet in TEXT:
        for dot_dash in Code[alphabet.upper()]:
            if dot_dash == '-':
                Dash_func()
            elif dot_dash == '.':
                Dot_func()
            else:
                time.sleep(0.13)
        time.sleep(1) 

def func(string_input):
    TEXT = string_input.get()
    if len(TEXT)>12: string_input.set(TEXT[:12])
     
def close():
    GPIO.cleanup()
    win.destroy()

string_input = Entry(win, font = Font_style, width = 20)
string_input.grid(row = 0, column = 0)

button = Button(win, text = 'MORSE-CODE-CONVERT', font = Font_style, command = morse_code, height = 1, width = 20)
button.grid( row =0, column = 3)

exitButton = Button(win, text = 'Exit', font = Font_style, command = close, bg = 'red', height = 1, width = 10)
exitButton.grid(row = 1, column = 1)

win.mainloop()
win.protocol("WM_DELETE_WINDOW", close)
