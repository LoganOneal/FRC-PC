from tkinter import *
from networktables import NetworkTables

NetworkTables.initialize(server='10.39.66.2')
smartdashboard = NetworkTables.getTable('SmartDashboard')

#Tkinter Code
root = Tk()
root.title("Mouse Input")

def send_mouse(data) :
        smartdashboard.putNumber('mouse', data)


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    send_mouse(x)

frame = Frame(root, width=500, height=400)
frame.bind('<Motion>', motion)
frame.pack()
frame.focus_set()
root.mainloop()