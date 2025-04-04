from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields are required !!!')
    elif usernameEntry.get()=='Admin' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login is Successful')
        root.destroy()
        import ems
    else:
        messagebox.show('error','Wrong Credentials')

root = CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('Login Page')

image = CTkImage(Image.open('cover.png'),size = (930,478))
imageLabel = CTkLabel(root,image = image)
imageLabel.place(x=0,y=0)

headingLabel = CTkLabel(root,text='Employee Management System',bg_color='#FAFAFA',font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headingLabel.place(x=20,y=50)

usernameEntry = CTkEntry(root,placeholder_text='Enter Your UserName',width = 180)
usernameEntry.place(x=50,y=130)

passwordEntry = CTkEntry(root,placeholder_text='Enter Your Password',width = 180)
passwordEntry.place(x=50,y=180)

loginButton = CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=70,y=230)

root.mainloop()