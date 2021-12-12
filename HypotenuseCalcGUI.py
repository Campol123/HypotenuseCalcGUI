import PySimpleGUI as sg # imports PySimpleGUI module
import math # imports python math module

layout = [[sg.Text("Welcome to Cameron's Hypotenuse calculator")], [sg.Text("Enter 'A' and 'B'")], [sg.In(size=(25, 1), enable_events=True, key="-A-")], [sg.In(size=(25, 1), enable_events=True, key="-B-")], [sg.Button("  NEXT  ")]] # defines primary page layout


window = sg.Window("Enter Parameters:", layout, margins=(300, 300)) # opens primary window


while True:
    event, values = window.read() # sets the 'event' and 'values' variables to information from the page
    if event == "  NEXT  " or event == sg.WIN_CLOSED:# ends while loop when user presses 'NEXT' button
        break
window.close()# closes primary window

A = values["-A-"] # sets 'A' to appropriate value from 'values'
B = values["-B-"] # sets 'B' to appropriate value from 'values'
try: # tries to perform hypotenuse calculation
    A=float(A)
    B=float(B)
    hyp_len = math.sqrt(A**2 + B**2)
    hyp_len=str(hyp_len)
except: # sets error to display if the 'A' or 'B' values are incorrect
    hyp_len=("ERROR- The A or B value was incorrect")

layout = [[sg.Text("The Hypotenuse: " + hyp_len)], [sg.Button("  DONE  ")]] # sets layout of secondary page
window = sg.Window("Hypotenuse: ", layout, margins=(300, 300)) # opens secondary window
while True:
    event, values = window.read() # sets the 'event' and 'values' variables to information from the page
    if event == "  DONE  " or event == sg.WIN_CLOSED:# ends while loop when user presses 'DONE' button
        break
window.close()# closes secondary window
