from tkinter import *
import tkinter as tk
import time
import playsound

def display_time():
	current_time = time.strftime("%H:%M:%S")
	textyText.configure(text=current_time)
	application.after(1000, display_time)
	min = time.strftime('%M')
	sec = time.strftime('%S')
	if (int(min)==0 and int(sec)<4):
		playsound.playsound('birds.mp3', True)	

application = tk.Tk()
application.title("Clock")
application.geometry("300x50")
application.configure(background="black")

textyText = tk.Label(application, text="", font=("Helverica", 30), bg="black", fg="purple",)

textyText.pack()
display_time()
application.mainloop()

