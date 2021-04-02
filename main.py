from tkinter import *
import random

root=Tk()
root.title("Roll Dice")
root.geometry("500x500")

label=Label(root,font=('helvetica',250,'bold'),text='')
label.pack()


def rolldice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()


button=Button(root,font=('helvetica',25,'bold'),text='roll dice',command=rolldice,bg="skyblue")
button.pack()

root.mainloop()
