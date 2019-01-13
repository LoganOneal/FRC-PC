from tkinter import *
from networktables import NetworkTables

NetworkTables.initialize(server='10.39.66.2')
smartdashboard = NetworkTables.getTable('SmartDashboard')

#Tkinter Code
root = Tk()
var = StringVar()
a_label = Label(root,textvariable = var ).pack()

history = []

def send(data) :
        #check for W
        if 87 in data:
                smartdashboard.putBoolean('W', True)
                print('W pressed')
        else: 
                smartdashboard.putBoolean('W', False)
                print('W released')
        #check for A
        if 65 in data:
                smartdashboard.putBoolean('A', True)
                print('A pressed')
        else: 
                smartdashboard.putBoolean('A', False)
                print('A released')
        #check for S
        if 83 in data:
                smartdashboard.putBoolean('S', True)
                print('S pressed')
        else: 
                smartdashboard.putBoolean('S', False)
                print('S released')
        #check for D
        if 68 in data:
                smartdashboard.putBoolean('D', True)
                print('D pressed')
        else: 
                smartdashboard.putBoolean('D', False)
                print('D released')

def send_mouse(data) :
        smartdashboard.putNumber('mouse', data)
        print('mouse', data)

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    send_mouse(x)


def keyup(e):
    print(e.keycode)
    if  e.keycode in history :
        history.pop(history.index(e.keycode))
        var.set(str(history))
        send(history)

def keydown(e):
    if not e.keycode in history :
        history.append(e.keycode)
        var.set(str(history))
        send(history)

frame = Frame(root, width=200, height=200)
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
frame.bind('<Motion>', motion)
frame.pack()
frame.focus_set()
root.mainloop()