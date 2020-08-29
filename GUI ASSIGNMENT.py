from tkinter import *
root = Tk()
root.geometry('300x300')
textlabel = Label(root, text='Account Holder: ', fg='black', bg='white')
textlabel.grid(row=1, column=0)
text_box = Entry(root)
text_box.grid(row=1, column=1, columnspan=4, ipadx=70)

def enter_1():
    a = text_box.get()
    print(a)
button_enter= Button(root, text='ENTER', fg='white', bg='black', command=enter_1, height=1, width=7)
button_enter.grid(row=2, column=2)

root.mainloop()