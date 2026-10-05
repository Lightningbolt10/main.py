from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination counter")
root.configure(bg="Light Blue")
root.geometry("650x400")

upload = Image.open("app_img.jpg")
upload = upload.resize((300,300))
image1 = ImageTk,PhotoImage(upload)

label = Label(root, image=image1, bg="Light blue")
label.place(x=180, y =20)

label1=Label(
    root,
    text = "Welcome to Denomination Counter",
    bg="Light Blue",
    
)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?"
    
    )
    if MsgBox == "ok":
        topwin()
    

button1 = Button(
    root,
    text="Press",
    command=msg,
    bg="brown",
    fg="white"

)
button1.place(x=260,y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="light grey")
    top.geometry("600x450")

    label = Label(top,text="Enter total paisa", bg="light grey")
    entry= Entry(top)

    lbl = Label(
        top,
        text="Here are the number of notes for each denomination",
        bg="Light grey"
    )

    l1 = Label(top, text="500", bg="llight grey")
    l2 = Label(top, text="200", bg="llight grey")
    l3 = Label(top, text="100", bg="llight grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    

    def calculator():
        try:
            amount = int(entry.get())

            note500 = amount // 500
            amount %=500
            note200 = amount // 200
            amount %=200
            note100 = amount // 100 

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note500))
            t2.insert(END, str(note200))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error","Please enter a sidha sada number.")

    btn = Button(
        top,
        text="calculate",
        command=calculator,
        bg="brown",
        fg="white"
    )
    label.place(x=230,y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)

    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()
root.mainloop()


    


        

        