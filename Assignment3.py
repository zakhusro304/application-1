# Program Name: Assignment3.py
# Course: IT3883/Section 01
# Student Name: Zara
# Assignment Number: Assignment 3
# Due Date: 03/06/2026
# Purpose: This program creates a GUI application that converts Miles Per Gallon (MPG)
#          to Kilometers Per Liter (KM/L). The result automatically updates each time
#          the user types a value in the MPG input box. The program also prevents
#          crashes by handling invalid input such as letters or blank fields.
# Resources: Python documentation, class notes, and assistance from ChatGPT for guidance.

from tkinter import *

# conversion constant
MPG_TO_KML = 0.425143707


# function that performs the conversion
def convert_value(*args):
    try:
        # get value typed by user
        mpg = float(mpg_var.get())

        # perform conversion
        kml = mpg * MPG_TO_KML

        # display result (rounded for readability)
        result_var.set(round(kml, 4))

    except:
        # if input is invalid (letters or blank), clear result
        result_var.set("")


# create main window
window = Tk()
window.title("MPG to KM/L Converter")
window.geometry("300x150")

# variables to store input and output
mpg_var = StringVar()
result_var = StringVar()

# whenever the user types, run the conversion function
mpg_var.trace("w", convert_value)

# label for MPG input
Label(window, text="Miles Per Gallon (MPG):").pack(pady=5)

# entry box for MPG
Entry(window, textvariable=mpg_var).pack()

# label for result
Label(window, text="Kilometers Per Liter (KM/L):").pack(pady=5)

# output label
Label(window, textvariable=result_var, font=("Arial", 14)).pack()

# start GUI loop
window.mainloop()
