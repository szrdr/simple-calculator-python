from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    myLabel = Label(root, text=f'Hello {e.get()}')
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", padx=50, pady=50, command=myClick, fg="blue")
myButton.pack()


root.mainloop()