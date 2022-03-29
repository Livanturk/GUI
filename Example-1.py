#Importing required libraries
from tkinter import *

def UserLogin(username,password):
    print("Username: ",username.get())
    print("Password: ",password.get())
    return

root = Tk()
root.title("User Login")
root.geometry("200x200")

unlabel=Label(root,text="Username")
unlabel.grid(row=0,column=0)
username = StringVar()
unentry=Entry(root,textvariable=username)
unentry.grid(row=0,column=1)

pwlabel=Label(root,text="Password")
pwlabel.grid(row=1,column=0)
password = StringVar()
pwentry=Entry(root,textvariable=password, show="*")
pwentry.grid(row=1,column=1)

button = Button(root,text="Login",command=lambda:UserLogin(username,password))
button.grid(row=4,column=0)

label = Label(root,text="Welcome!")
label.grid(row=5,column=0)

root.mainloop()



