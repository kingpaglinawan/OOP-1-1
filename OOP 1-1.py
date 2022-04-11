from tkinter import *
window = Tk()

window.geometry("500x500+30+20")
window.title("Welcome to Python Programming")

#add Button widget

btn = Button(window, text = "What is your name?", fg="blue")
btn.place(x=35, y=100)

#Add label widget
lbl = Label(window, text="Student Personal Information", fg="white", bg="black")
lbl.place(relx=.5, y=50, anchor='center')
lbl2 = Label(window, text="Gender", fg="white", bg="black")
lbl2.place(x=80, y=160)

#Add text field widget

txtfld = Entry(window, bd=3, font=("verdana", 16))
txtfld.place(x=150, y=100)

#add radio button

v1 = StringVar()
v2 = StringVar()

v1.set(1)
r1 = Radiobutton(window, text="Male", variable=v1, value=1)
r1.place(x=80, y=200)
r2 = Radiobutton(window, text="Female", variable=v2, value=2)
r2.place(x=150, y=200)
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
v7 = IntVar()
chkbox = Checkbutton(window, text="basketball", variable=v3)
chkbox2 = Checkbutton(window, text="swimming", variable=v4)
chkbox3 = Checkbutton(window, text="soccer", variable=v5)
chkbox4 = Checkbutton(window, text="chess", variable=v6)
chkbox5 = Checkbutton(window, text="badminton", variable=v7)

chkbox.place(x=50, y=300)
chkbox2.place(x=100, y=350)
chkbox3.place(x=150, y=300)
chkbox4.place(x=200, y=350)
chkbox5.place(x=250, y=300)

lbl3 = Label(window, text="Sports",fg="white", bg="black")
lbl3.place(x=80, y=260)

lbl4 = Label(window, text="Subject",fg="white", bg="black")
lbl4.place(x=80, y=380)
var = StringVar()
var.set("Student1")
data1 = "Calculus"
data2 = "Reading"
data3 = "Writing"
data4 = "Science"
data5 = "History"
lstbox = Listbox(window, height=5, selectmode="multiple")
lstbox.insert(END, data1, data2, data3, data4, data5)
lstbox.place(x=80, y=410)

window.mainloop()

