from Tkinter import *
import pickle
import socket

#Connect To Server
HOST = 'localhost'
PORT = 5800

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST , PORT))


root = Tk()
var = StringVar()
a_label = Label(root,textvariable = var ).pack()

history = []

def send(data) :
    data=pickle.dumps(data)
    client.send(data)

def keyup(e):
    print e.keycode
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
frame.pack()
frame.focus_set()
root.mainloop()