from tkinter import *
import random
import string
import pyperclip


def copyPass():
    pyperclip.copy(pass_str.get())
    # print('pass copied', pyperclip.paste())


def Generator():
    password = ""

#    The loop will generate a random string of length entered by the user – 4 and add to the password variable. Here we minus 4 to the length of the user because we already generate the string of length 4.

    for y in range(pass_len.get()):
        password += random.choice(string.ascii_uppercase +
                                  string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


root = Tk()  # initialized tkinter which means window created
root.geometry("400x400")  # set the width and height of the window
root.resizable(0, 0)  # set the fixed size of the window
root.title("PASSWORD GENERATOR")  # set the title of the window
pass_str = StringVar()  # stores the generated password
# is an integer type variable that stores the length of a password.To select the password length we use Spinbox() widget.
pass_len = IntVar()

Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()

Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack()

# widget is used to select from a fixed number of values. Here the value from 8 to 32
Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

Button(root, text="GENERATE PASSWORD", command=Generator).pack(pady=9)

Entry(root, textvariable=pass_str).pack()

Button(root, text='COPY TO CLIPBOARD', command=copyPass).pack(pady=6)

root.mainloop()
