from tkinter import *
root =Tk()
root.geometry('300x300')
INPUT_1 = Label(root, text='INPUT_1: ', fg='black', bg='white')
INPUT_1.grid(row=1, column=0)
text_box = Entry(root)
text_box.grid(row=1, column=1, ipadx=1)
INPUT_2 = Label(root, text='INPUT_2: ', fg='black', bg='white')
INPUT_2.grid(row=2, column=0)
text_box_2 = Entry(root)
text_box_2.grid(row=2, column=1, ipadx=1)
OUTPUT = Label(root, text='OUTPUT: ', fg='black', bg='white')
OUTPUT.grid(row=3, column=0)
text_box_3 = Entry(root)
text_box_3.grid(row=3, column=1, ipadx=1)

cal=StringVar()


def calculate():
    a = int(text_box.get())
    b = int(text_box_2.get())
    c = a + b
    cal.set(c)
    text_box_3.insert(0, c)



button_enter= Button(root, text='CALCULATE', command=calculate , fg='white', bg='black', height=1, width=15)
button_enter.grid(row=4, column=1)




root.mainloop()
