from tkinter import *
import calendar

text = calendar.calendar(1)
root = Tk()
root = geometry("500x600")
root.title("Crop Planner")
label1 = label(root,text = "Calendar",bg = 'dark gray', font = ("times",28,'bold'))
label1.grid(row=1,column=1)
root.config(background="white")
l1 = Label(root,text=text,font="Consoles 10")
l1.grid(row=2,column=1,padx=20)
root.mainloop()
