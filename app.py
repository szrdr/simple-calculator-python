from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=1)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    myLabel = Label(root, text=f'Hello {e.get()}')
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", padx=50, pady=50, command=myClick, fg="blue")
myButton.pack()


root.mainloop()