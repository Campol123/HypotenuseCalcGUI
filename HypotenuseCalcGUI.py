import PySimpleGUI as sg
import math

layout = [[sg.Text("Welcome to Cameron's Hypotenuse calculator")], [sg.Text("Enter 'A' and 'B'")], [sg.In(size=(25, 1), enable_events=True, key="-A-")], [sg.In(size=(25, 1), enable_events=True, key="-B-")], [sg.Button("  NEXT  ")]]

# Create the window
window = sg.Window("Enter Parameters:", layout, margins=(300, 300))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "  NEXT  " or event == sg.WIN_CLOSED:
        break
window.close()
A = values["-A-"]
B = values["-B-"]
A=int(A)
B=int(B)

hyp_len = math.sqrt(A**2 + B**2)
hyp_len=str(hyp_len)

layout = [[sg.Text("The Hypotenuse: " + hyp_len)], [sg.Button("  DONE  ")]]
window = sg.Window("Enter Parameters:", layout, margins=(300, 300))
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "  DONE  " or event == sg.WIN_CLOSED:
        break
window.close()
