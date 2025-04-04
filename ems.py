from customtkinter import *
from PIL import Image
import database
from tkinter import ttk,messagebox

#Functions

def delete_all():
    result=messagebox.askyesno('Confirm','Do you really want to delete all the records?')
    if result:
        database.deleteall_records()
    else:
        pass

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')

def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Enter Value to search')
    elif searchBox.get()=='Search By':
        messagebox.showerror('Error','Please Select an Option')
    else:
        searched_data=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('',END,values=employee)


def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to Update delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('ERROR','Data is Deleted')

def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to update')

    else:
        database.update(idEntry.get(),NameEntry.get(),PhoneEntry.get(),roleBox.get(),GenderBox.get(),SalaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is updated')

def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        NameEntry.insert(0,row[1])
        PhoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        GenderBox.set(row[4])
        SalaryEntry.insert(0,row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    NameEntry.delete(0,END)
    PhoneEntry.delete(0,END)
    roleBox.set('Web Developer')
    GenderBox.set('Male')
    SalaryEntry.delete(0,END)

def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)

def Add_Employee():
    if idEntry.get()=='' or PhoneEntry.get()=='' or NameEntry.get()=='' or SalaryEntry.get()=='':
        messagebox.showerror('Error','All Fields are Required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','ID already exists')
    else:
        database.insert(idEntry.get(),NameEntry.get(),PhoneEntry.get(),roleBox.get(),GenderBox.get(),SalaryEntry.get())
        treeview_data()
        messagebox.showinfo('SUCCESS','Data is ADDED')

#GUI
window=CTk()
window.geometry('940x580')
window.resizable(False,False)
window.title('Employee Management System')
logo = CTkImage(Image.open('logo.png'),size=(930,158))
logoLabel=CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(window)
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame,text='Id',font=('arial',18,'bold'))
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')

idEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)

NameLabel=CTkLabel(leftFrame,text='Name',font=('arial',18,'bold'))
NameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

NameEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
NameEntry.grid(row=1,column=1)

PhoneLabel=CTkLabel(leftFrame,text='Phone',font=('arial',18,'bold'))
PhoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')

PhoneEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
PhoneEntry.grid(row=2,column=1)

RoleLabel=CTkLabel(leftFrame,text='Role',font=('arial',18,'bold'))
RoleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')
role_options=['Web Developer', 'Cloud Architect','Technical Writer','Network Engineer','Dev Ops Engineer','Data Scientist','Business Analyst','IT Consultant','UI/UX Developer']
roleBox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',15,'bold'))
roleBox.grid(row=3,column=1)

GenderLabel=CTkLabel(leftFrame,text='Gender',font=('arial',18,'bold'))
GenderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')
Gender_options=['Male', 'Female']
GenderBox=CTkComboBox(leftFrame,values=Gender_options,width=180,font=('arial',15,'bold'))
GenderBox.grid(row=4,column=1)

SalaryLabel=CTkLabel(leftFrame,text='Salary',font=('arial',18,'bold'))
SalaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

SalaryEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
SalaryEntry.grid(row=5,column=1)

rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)
search_options = ['Id','Name','Phone','role','Gender','Salary']
searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightFrame,width=180)
searchEntry.grid(row=0,column=1)

searchButton = CTkButton(rightFrame,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2)

showAllButton = CTkButton(rightFrame,text='Show All',width=100,command=show_all)
showAllButton.grid(row=0,column=3)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4,padx=25,pady=20)

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')

tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')

tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')

tree.column('Id',width=100)
tree.column('Name',width=140)
tree.column('Phone',width=130)
tree.column('Role',width=160)
tree.column('Gender',width=80)
tree.column('Salary',width=140)

style = ttk.Style()

style.configure('Treeview.Heading',font=('arial',12,'bold'))
style.configure('Treeview',font=('arial',12,'bold'),background='#161C30',foreground='white')

scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns',pady=5)

tree.config(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(window,fg_color='#161C30')
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton = CTkButton(buttonFrame,text='New Employee',font=('arial',12,'bold'),width=160,corner_radius=150,command=lambda:clear(True))
newButton.grid(row=0,column=0,pady=25)

addButton = CTkButton(buttonFrame,text='Add Employee',font=('arial',12,'bold'),width=160,corner_radius=150,command=Add_Employee)
addButton.grid(row=0,column=1,padx=5,pady=25)

UpdateButton = CTkButton(buttonFrame,text='Update Employee',font=('arial',12,'bold'),width=160,corner_radius=150,command=update_employee)
UpdateButton.grid(row=0,column=2,padx=5,pady=25)

DeleteButton = CTkButton(buttonFrame,text='Delete Employee',font=('arial',12,'bold'),width=160,corner_radius=150,command=delete_employee)
DeleteButton.grid(row=0,column=3,padx=5,pady=25)

DeleteAllButton = CTkButton(buttonFrame,text='Delete All',font=('arial',12,'bold'),width=160,corner_radius=150,command=delete_all)
DeleteAllButton.grid(row=0,column=4,padx=5,pady=25)

treeview_data()

window.bind('<ButtonRelease>',selection)

window.mainloop()