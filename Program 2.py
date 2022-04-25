from tkinter import *
window = Tk()

window.geometry("600x500+30+20")
window.title("Midterm in OOP")

lbl = Label(window, text="Enter your fullname:", fg="red")
lbl.place(x=80, y=100)

txtfld = Entry(window, bd=3, font=("Arial", 16))
txtfld.place(x=300, y=100)

def click():
    value=txtfld.get()
    txtfld2.delete(0,END)
    txtfld2.insert(0, str(value))
btn = Button(window, text = "Click to display your Fullname", fg="red", command=click)
btn.place(x=80, y=150)

txtfld2 = Entry(window, bd=3, font=("Arial", 16))
txtfld2.place(x=300, y=150)

window.mainloop()