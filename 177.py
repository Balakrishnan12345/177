from tkinter import*

root=Tk()
root.title("Private Variable Login page")
root.geometry("600x900")

name_ibl = Label(root,text ="Name")
name_ibl(relx=0.4,rely=0.1,anchor=CENTER)

name_entry =Entry(root)
name_entry.place(relx=0.6,rely=0.1,anchor=CENTER)


pw_label =Label(root,text="Password")
pw_ibl.place(relx=0.4,rely=0.2,anchor=CENTER )

pw_entry =Entry(root)
pw_entry.place(relx= 0.6,rely=0.2,anchor=CENTER)


captcha_label =Label(root,text="Captcha")
captcha_ibl.place(relx=0.4,rely=0.3,anchor=CENTER )

captcha_entry =Entry(root)
captcha_entry.place(relx= 0.6,rely=0.3,anchor=CENTER)
