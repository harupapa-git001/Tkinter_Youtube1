from tkinter import *

root = Tk()

myLabel1 = Label(root, text = "Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text = "My Name Is John Elder").grid(row=1, column=2)
myLabel3 = Label(root, text = "I          am          student   ")
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=2)
myLabel3.grid(row=1, column=1)
root.mainloop()