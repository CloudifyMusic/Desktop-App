from tkinter import *

root = Tk()

root.title("Cloudify Music")
root['bg'] = "#2f3540"
root.geometry('480x320')
root.maxsize(480, 320)
root.minsize(480, 320)

lab1 = Label(root, text="Username:", fg="white", bg="#2f3540")
lab1.pack()
lab1.place(anchor="c", relx=.5, rely=.4)

username = Entry(root, bg="#4f5a70", fg="white")
username.pack()
username.place(anchor="c", relx=.5, rely=.5)

lab2 = Label(root, text="Password:", fg="white", bg="#2f3540")
lab2.pack()
lab2.place(anchor="c", relx=.5, rely=.6)

Password = Entry(root, bg="#4f5a70", fg="white")
Password.pack()
Password.place(anchor="c", relx=.5, rely=.7)

def LogIn():
    print("LogIn")


LogIn = Button(root, text="Log in", command=LogIn)
LogIn.pack()
LogIn.place(anchor="c", relx=.5, rely=.8)



root.mainloop()

