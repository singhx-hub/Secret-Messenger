from tkinter import *  # for GUI
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

# GUI Interface Design
root = Tk()
root.title("Secret Messenger - Hide Secret in an Image")
root.geometry("1000x700+500+200")
root.resizable(False, False)
root.configure(bg="#2C3539")


def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),

                                          title="Select Image File",
                                          filetypes=(("PNG file", "*.png"),
                                                     ("JPG file", "*.jpg"), ("All file", "*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lb1.configure(image=img, width=430, height=340)
    lb1.image = img


def hide():
    global secret
    msg = txt.get(1.0, END)
    secret = lsb.hide(str(filename), msg)
    print_text = "Data Hide Successfully!"
    result_label.configure(text=print_text)


result_label = Label(root, text="", font="Arial 14", bg="#2C3539", fg="white")
result_label.place(x=400, y=610)


def show():
    clear_msg = lsb.reveal(filename)
    txt.delete(1.0, END)
    txt.insert(END, clear_msg)


def save():
    secret.save("Hidden.png")
    txt.delete(1.0, END)  # Clear the text in txt
    lb1.configure(image='', width=0, height=0)  # Reset the image in lb1
    print_text = "Image Saved Successfully!"
    result_label.configure(text=print_text)


result_label = Label(root, text="", font="Arial 14", bg="#2C3539", fg="white")
result_label.place(x=400, y=620)

# Icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(True, image_icon)

# Logo
logo = PhotoImage(file="logo(1).png")
Label(root, image=logo, bg="#2C3539").place(x=10, y=0)
Label(root, text="Secret Blend", bg="#2C3539", fg="#52D017", font="arial 25 bold").place(x=100, y=20)

# First_Frame
f = Frame(root, bd=3, bg="black", width=490, height=350, relief=SUNKEN)
f.place(x=5, y=100)

lb1 = Label(f, bg="black")
lb1.place(x=40, y=10)

# Second_Frame
f2 = Frame(root, bd=3, width=490, height=350, bg="white", relief=SUNKEN)
f2.place(x=500, y=100)

txt = Text(f2, font="Robot 20", bg="white", fg="black", relief=SUNKEN, wrap=WORD)
txt.place(x=0, y=0, width=475, height=350)

scrollbar1 = Scrollbar(f2)
scrollbar1.place(x=470, y=0, height=350)

scrollbar1.configure(command=txt.yview)
txt.configure(yscrollcommand=scrollbar1.set)

# Third_Frame
f3 = Frame(root, bd=3, bg="#2C3539", width=490, height=100, relief=SUNKEN)
f3.place(x=5, y=470)

Button(f3, text="Open Image", width=10, height=2, bg="yellow", font="arial 14 bold", command=showimage).place(x=20,
                                                                                                              y=30)
Button(f3, text="Save Image", width=10, height=2, bg="green", font="arial 14 bold", command=save).place(x=340, y=30)
Label(f3, text="Picture, Image, Photo File", bg="#2C3539", fg="yellow").place(x=170, y=5)

# Fourth_Frame
f4 = Frame(root, bd=3, bg="#2C3539", width=490, height=100, relief=SUNKEN)
f4.place(x=500, y=470)

Button(f4, text="Hide Data", width=10, height=2, bg="yellow", font="arial 14 bold", command=hide).place(x=20, y=30)
Button(f4, text="Show Data", width=10, height=2, bg="green", font="arial 14 bold", command=show).place(x=340, y=30)
Label(f4, text="Picture, Image, Photo File", bg="#2C3539", fg="yellow").place(x=170, y=5)

root.mainloop()
