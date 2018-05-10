    # use Tkinter to show a digital clock
    # tested with Python24    vegaseat    10sep2006
from tkinter import *
import tkinter as tk
import time

def display_time():
	current_time = time.strftime("%H:%M:%S")
	textyText.configure(text=current_time)
	application.after(1000, display_time)

application = tk.Tk()
application.title("Clock")
application.geometry("300x100")
application.configure(background="black")

textyText = tk.Label(application, text="", font=("Helverica", 30), bg="black", fg="purple",)


textyText.pack()
display_time()
B1 = tk.Button(application, text ="just a random button", relief=RAISED, cursor="heart")
B1.pack()
application.mainloop()

