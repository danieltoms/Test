from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
from datetime import datetime
from my_classes import *
from see_database import *

# Initialise variables:
response1 = "I am afraid not. Please try again."
response2 = "That is a good password but not my password. Keep guessing."
response3 = "That is not my password. It really is easy to guess my password."
my_staff = {}
my_student = {}
my_user = {}
my_appointments = []
PrintData()

#username DST Password %Password1 

class loginWindow:


    def __init__(self):
        self.root=Tk()
        self.createWidgets()


    def createWidgets(self):

        self.root.title("Login Window")
        self.output = Text(self.root, width=40, height=2, wrap=WORD, background='white', foreground = "red")
        self.output.grid(row=0, column=2, sticky=W)

        Label(self.root, text='Username:').grid(row=1, column=0, sticky=W)
        self.username_entry = Entry(self.root, width=20, bg='grey')
        self.username_entry.grid(row=1, column=2, sticky=W)

        Label(self.root, text='Password:').grid(row=2, column=0, sticky=W)
        self.password_entry = Entry(self.root, width=20, bg='grey')
        self.password_entry.grid(row=2, column=2,sticky=W)

        #Add a submit button
        Button(self.root, text='SUBMIT', width=7, command=self.click).grid(row=3, column=2, sticky=W)


    def click(self):
        array = []
        LoadStaff(my_staff)
        LoadStudents(my_student)
        LoadUsers(my_user)
        username = self.username_entry.get() #collect text from text entry box

        for key in my_staff.keys():
            array.append(key)

        array = quicksort(array)
        inStaff = BinarySearch(array, 0, len(array)-1, username)


        for key in my_student.keys():
            array.append(key)
        array = quicksort(array)

        inStudent = BinarySearch(array, 0, len(array)-1, username)

        if inStaff == False and inStudent == FALSE:
                self.output.delete(0.0, END)
                self.output.insert(END, "No Such User")
        elif inStaff == TRUE:
            password = self.password_entry.get() #collect text from text entry box
            true_or_false = my_staff[username].login(password)
                #Run the game until the user is correct:
            if true_or_false == FALSE:
                computer_response = random.randint(1, 3)
                if computer_response == 1:
                    self.output.delete(0.0, END)
                    self.output.insert(END, response1)
                elif computer_response == 2:
                    self.output.delete(0.0, END)
                    self.output.insert(END, response2)
                else:
                    self.output.delete(0.0, END)
                    self.output.insert(END, response3)
            else:
                self.root.destroy()
                window = mainMenu(username,my_staff[username].get_access())

        elif inStudent == TRUE:
            password = self.password_entry.get() #collect text from text entry box
            true_or_false = my_student[username].login(password)
                #Run the game until the user is correct:
            if true_or_false == FALSE:
                computer_response = random.randint(1, 3)
                if computer_response == 1:
                    self.output.delete(0.0, END)
                    self.output.insert(END, response1)
                elif computer_response == 2:
                    self.output.delete(0.0, END)
                    self.output.insert(END, response2)
                else:
                    self.output.delete(0.0, END)
                    self.output.insert(END, response3)
            else:
                self.root.destroy()
                window = mainMenu(username, my_student[username].get_access())


##====================================================

class adminMenu:

    def __init__(self, username, access):

        self.root=Tk()
        self.username = username
        self.access = access
        self.createWidgets()
        self.display()

        
    def createWidgets(self):
        
        self.root.title("Admin")
        Label(self.root, text='ADMIN MENU:').grid(row=0, column=0, columnspan=5, sticky=W+E)
        Button(self.root, text='Menu', width=7, command=self.mainMenu).grid(row=0, column=4, sticky=E)

        self.output2 = Frame(self.root, width=65, height=20, padx=20, pady=20, background='grey')
        self.output2.grid(row=1, column=0, columnspan=5, sticky=W)

        Label(self.root, text='Username:').grid(row=2, column=1, sticky=W)
        self.user_username_entry = Entry(self.root, width=20, bg='grey')
        self.user_username_entry.grid(row=2, column=2, sticky=W)

        Label(self.root, text='Password:').grid(row=3, column=1, sticky=W)
        self.user_password_entry = Entry(self.root, width=20, bg='grey')
        self.user_password_entry.grid(row=3, column=2, sticky=W)

        Label(self.root, text='Access:').grid(row=4, column=1, sticky=W)
        self.user_access_entry = Entry(self.root, width=20, bg='grey')
        self.user_access_entry.grid(row=4, column=2, sticky=W)

        Label(self.root, text='Search Users').grid(row=2, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.search).grid(row=2, column=4, sticky=W)

        Label(self.root, text='Change Password').grid(row=3, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.password).grid(row=3, column=4, sticky=W)

        Label(self.root, text='Search Access').grid(row=4, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.search_access).grid(row=4, column=4, sticky=W)


        
    #key press function

    def display(self):
        self.output2.destroy()
        self.output2 = Frame(self.root, width=65, height=20, padx=20, pady=20, background='grey')
        self.output2.grid(row=1, column=0, columnspan=5, sticky=W)

        Label(self.output2, anchor=W, text='Username', width=20, background='grey', font='default 12 bold').grid(row=0, column=0)
        Label(self.output2, anchor=W, text='Access Level', width=20, background='grey', font='Default 12 bold').grid(row=0, column=1)
        Label(self.output2, anchor=W, text='Last Login', width=20, background='grey', font='Default 12 bold').grid(row=0, column=2)

        array =[]
        for key in my_user.keys():
            array.append(key)
        array = quicksort(array)

        r = 1

        for key in array:
            Label(self.output2, anchor=W, text=key, width=20, background='grey', font="Default 12").grid(row=r, column=0)
            Label(self.output2, anchor=W, text=str(my_user[key].get_access()), width=20, background='grey', font="Default 12").grid(row=r, column=1)
            Label(self.output2, anchor=W, text=str(my_user[key].get_login()), width=20, background='grey', font="Default 12").grid(row=r, column=2)
            r = r + 1


    def search(self):
        array = []
        searchUsername = self.user_username_entry.get()

        for key in my_user.keys():
            array.append(key)

        array = quicksort(array)
        true_or_false = BinarySearch(array, 0, len(array)-1, searchUsername)

        if true_or_false == True:
            self.output2.destroy()
            self.output2 = Frame(self.root, width=65, height=20, padx=20,pady=20, background='grey')
            self.output2.grid(row=1, column=0, columnspan=5, sticky=W)
            Label(self.output2, anchor=W, text='Username', width=20, background='grey', font='default 12 bold').grid(row=0, column=0)
            Label(self.output2, anchor=W, text='Full Name', width=20, background='grey', font='Default 12 bold').grid(row=0, column=1)
            Label(self.output2, anchor=W, text='Last Login', width=20, background='grey', font='Default 12 bold').grid(row=0, column=2)
            Label(self.output2, anchor=W, text=searchUsername, width=20, background='grey', font="Default 12").grid(row=1, column=0)
            Label(self.output2, anchor=W, text=str(my_user[searchUsername].get_access()), width=20, background='grey', font="Default 12").grid(row=1, column=1)
            Label(self.output2, anchor=W, text=str(my_user[searchUsername].get_login()), width=20, background='grey', font="Default 12").grid(row=1, column=2)
        else:
            messagebox.showwarning("Error", "User does not exist")

    def password(self):
        username = self.user_username_entry.get()
        new_password = self.user_password_entry.get()

        array=[]
        for key in my_staff.keys():
            array.append(key)

        array = quicksort(array)
        in_staff = BinarySearch(array, 0, len(array)-1, username)

        array=[]
        for key in my_student.keys():
            array.append(key)

        array = quicksort(array)
        in_student = BinarySearch(array, 0, len(array)-1, username)

        if in_staff == TRUE:

            if new_password != "":
                if RegularExpressions(new_password):
                    my_staff[username].edit_password(HashPassword(new_password))
                    SaveData(my_staff, my_student, my_user)#saves the login to file
                    messagebox.showwarning("Success", "You're password has been updated")
                else:
                     messagebox.showwarning("Error", "I'm sorry, your password must contain a number etc.")
            else:
                messagebox.showwarning("Error", "I'm sorry, you need to add a new password")

        elif in_student == TRUE:

            if new_password != "":
                if RegularExpressions(new_password):
                    my_student[username].edit_password(HashPassword(new_password))
                    SaveData(my_staff, my_student, my_user)#saves the login to file
                    messagebox.showwarning("Success", "You're password has been updated")
                else:
                     messagebox.showwarning("Error", "I'm sorry, your password must contain a number etc.")
            else:
                messagebox.showwarning("Error", "I'm sorry, you need to add a new password")
        else:
            messagebox.showwarning("Error", "User does not exist")

    def search_access(self):
        access = self.user_access_entry.get()
        r = 1
        self.output2.destroy()
        self.output2 = Frame(self.root, width=65, height=20, padx=20,pady=20, background='grey')
        self.output2.grid(row=1, column=0, columnspan=5, sticky=W)
        Label(self.output2, anchor=W, text='Username', width=20, background='grey', font='default 12 bold').grid(row=0, column=0)
        Label(self.output2, anchor=W, text='Full Name', width=20, background='grey', font='Default 12 bold').grid(row=0, column=1)
        Label(self.output2, anchor=W, text='Last Login', width=20, background='grey', font='Default 12 bold').grid(row=0, column=2)

        for key in my_user.keys():
            if my_user[key].get_access() == access:
                Label(self.output2, anchor=W, text=key, width=20, background='grey', font="Default 12").grid(row=r, column=0)
                Label(self.output2, anchor=W, text=str(my_user[key].get_access()), width=20, background='grey', font="Default 12").grid(row=r, column=1)
                Label(self.output2, anchor=W, text=str(my_user[key].get_login()), width=20, background='grey', font="Default 12").grid(row=r, column=2)
                r = r + 1

        if r == 1:
            messagebox.showwarning("Error", "No one with this level of access")


    def mainMenu(self):
        self.root.destroy()
        window = mainMenu(self.username, self.access)


class mainMenu:
    def __init__(self, username, access):

        self.root=Tk()
        self.username = username
        self.access = access
        self.createWidgets()

    def createWidgets(self):

        self.root.title("Menu")
        Label(self.root, text='MAIN MENU:').grid(row=0, column=0, columnspan=5, sticky=W+E)
        Button(self.root, text='Log Out', width=7, command=self.logout).grid(row=0, column=4, sticky=E)

        self.main_output = Text(self.root, width=65, height=20, padx=20,pady=20, wrap=WORD, background='grey', foreground = "red")
        self.main_output.grid(row=1, column=0, columnspan=5, sticky=W)

        if self.access == 'Student':
            response4 = "Well done! You last logged in " + str(my_student[self.username].get_login())
            self.main_output.delete(0.0, END)
            self.main_output.insert(END, response4)
            my_student[self.username].edit_login()#records the time of your last login
            SaveData(my_staff, my_student,my_user)#saves the login to file

        elif self.access == 'Staff':
            response4 = "Well done! You last logged in " + str(my_staff[self.username].get_login())
            self.main_output.delete(0.0, END)
            self.main_output.insert(END, response4)
            my_staff[self.username].edit_login()#records the time of your last login
            SaveData(my_staff, my_student,my_user)#saves the login to file

            Label(self.root, text='Admin').grid(row=4, column=1, sticky=W)
            Button(self.root, text='OK', width=7, command=self.admin).grid(row=4, column=2, sticky=W)

            Label(self.root, text='Staff').grid(row=5, column=1, sticky=W)
            Button(self.root, text='OK', width=7, command=self.staff).grid(row=5, column=2, sticky=W)

            Label(self.root, text='Students').grid(row=6, column=1, sticky=W)
            Button(self.root, text='OK', width=7, command=self.student).grid(row=6, column=2, sticky=W)

            Label(self.root, text='Appointments').grid(row=7, column=1, sticky=W)
            Button(self.root, text='OK', width=7, command=self.appointments).grid(row=7, column=2, sticky=W)



    def admin(self):
        self.root.destroy()
        window = adminMenu(self.username, self.access)

    def staff(self):
        self.root.destroy()
        window = staffMenu(self.username, self.access)

    def student(self):
        self.root.destroy()
        window = studentMenu(self.username, self.access)

    def logout(self):
        self.root.destroy()
        window = loginWindow()

    def appointments(self):
        self.root.destroy()
        window = appointmentsMenu(self.username, self.access)


class staffMenu:

    def __init__(self, username, access):
        self.root=Tk()
        self.username = username
        self.access = access
        self.createWidgets()
        self.displayStaff()


    def createWidgets(self):
        self.root.title("Staff")
        Label(self.root, text='STAFF MENU:').grid(row=0, column=0, columnspan=5, sticky=W+E)
        Button(self.root, text='Menu', width=7, command=self.mainMenu).grid(row=0, column=4, sticky=E)
        self.output2 = Frame(self.root, width=65, height=20, padx=20,pady=20, background='grey')
        self.output2.grid(row=1, column=0, columnspan=5, sticky=W)

# Text Boxes
        Label(self.root, text='Username:').grid(row=2, column=1, sticky=W)
        self.staff_username_entry = Entry(self.root, width=20, bg='grey')
        self.staff_username_entry.grid(row=2, column=2, sticky=W)

        Label(self.root, text='First Name:').grid(row=3, column=1, sticky=W)
        self.staff_firstName_entry = Entry(self.root, width=20, bg='grey')
        self.staff_firstName_entry.grid(row=3, column=2, sticky=W)

        Label(self.root, text='Surname:').grid(row=4, column=1, sticky=W)
        self.staff_surname_entry = Entry(self.root, width=20, bg='grey')
        self.staff_surname_entry.grid(row=4, column=2, sticky=W)


# Labels and Buttons

        Label(self.root, text='Search Staff').grid(row=2, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.searchStaff).grid(row=2, column=4, sticky=W)

        Label(self.root, text='Edit Staff').grid(row=3, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.editStaff).grid(row=3, column=4, sticky=W)

        Label(self.root, text='Add Staff').grid(row=4, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.addStaff).grid(row=4, column=4, sticky=W)

        Label(self.root, text='Delete Staff').grid(row=5, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.deleteStaff).grid(row=5, column=4, sticky=W)


    def mainMenu(self):
        self.root.destroy()
        window = mainMenu(self.username, self.access)

    def addStaff(self):
        array = []
        newUsername = self.staff_username_entry.get()
        newPassword = HashPassword("Password1")
        newFirstName = self.staff_firstName_entry.get()
        newSurname = self.staff_surname_entry.get()
        newAccess = "Staff"

        for key in my_staff.keys():
            array.append(key)

        array = quicksort(array)
        true_or_false = BinarySearch(array, 0, len(array)-1, newUsername)

        if true_or_false == False:
            d = datetime.now()
            my_staff[newUsername] = Staff(newFirstName, newSurname, newPassword, str(d.strftime("%A %B %d")), newAccess)
            self.displayStaff()
            SaveData(my_staff, my_student,my_user)  # saves the login to file
        else:
            messagebox.showwarning("User already exists")

    def displayStaff(self):
        self.output2.destroy()
        self.output2 = Frame(self.root, width=65, height=20, padx=20,pady=20, background='grey')
        self.output2.grid(row=1, column=0, columnspan=5, sticky=W)

        Label(self.output2, anchor=W, text='Username', width=20, background='grey', font='default 12 bold').grid(row=0, column=0)
        Label(self.output2, anchor=W, text='Full Name', width=20, background='grey', font='Default 12 bold').grid(row=0, column=1)
        Label(self.output2, anchor=W, text='Last Login', width=20, background='grey', font='Default 12 bold').grid(row=0, column=2)

        array =[]
        for key in my_staff.keys():
            array.append(key)
            array = quicksort(array)
        r = 1

        for key in array:
            Label(self.output2, anchor=W, text=key, width=20, background='grey', font="Default 12").grid(row=r, column=0)
            Label(self.output2, anchor=W, text=str(my_staff[key].get_fullname()), width=20, background='grey', font="Default 12").grid(row=r, column=1)
            Label(self.output2, anchor=W, text=str(my_staff[key].get_login()), width=20, background='grey', font="Default 12").grid(row=r, column=2)
            r = r + 1

    def deleteStaff(self):
        deleteUsername = self.staff_username_entry.get()
        del my_staff[deleteUsername]
        SaveData(my_staff, my_student,my_user)#saves the login to file
        self.displayStaff()

    def searchStaff(self):
        array = []
        searchUsername = self.staff_username_entry.get()

        for key in my_staff.keys():
            array.append(key)

        array = quicksort(array)
        true_or_false = BinarySearch(array, 0, len(array)-1, searchUsername)

        if true_or_false == True:
            self.output2.destroy()
            self.output2 = Frame(self.root, width=65, height=20, padx=20,pady=20, background='grey')
            self.output2.grid(row=1, column=0, columnspan=5, sticky=W)
            Label(self.output2, anchor=W, text='Username', width=20, background='grey', font='default 12 bold').grid(row=0, column=0)
            Label(self.output2, anchor=W, text='Full Name', width=20, background='grey', font='Default 12 bold').grid(row=0, column=1)
            Label(self.output2, anchor=W, text='Last Login', width=20, background='grey', font='Default 12 bold').grid(row=0, column=2)
            Label(self.output2, anchor=W, text=searchUsername, width=20, background='grey', font="Default 12").grid(row=1, column=0)
            Label(self.output2, anchor=W, text=str(my_staff[searchUsername].get_fullname()), width=20, background='grey', font="Default 12").grid(row=1, column=1)
            Label(self.output2, anchor=W, text=str(my_staff[searchUsername].get_login()), width=20, background='grey', font="Default 12").grid(row=1, column=2)
        else:
            messagebox.showwarning("Error", "User does not exist")

    def editStaff(self):
        username = self.staff_username_entry.get()
        firstname = self.staff_firstName_entry.get()
        surname = self.staff_surname_entry.get()
        array=[]

        for key in my_staff.keys():
            array.append(key)



        array = quicksort(array)
        true_or_false = BinarySearch(array, 0, len(array)-1, username)


        if true_or_false == TRUE:

            if firstname != "" and surname != "":

                my_staff[username].edit_firstname(firstname)
                my_staff[username].edit_surname(surname)
                SaveData(my_staff, my_student,my_user)#saves the login to file

            elif firstname != "":

                my_staff[username].edit_firstname(firstname)
                SaveData(my_staff, my_student,my_user)#saves the login to file

            elif surname != "":

                my_staff[username].edit_surname(surname)
                SaveData(my_staff, my_student,my_user)#saves the login to file

            else:
                messagebox.showwarning("Error", "I'm sorry, there's nothing to update")

        else:
            messagebox.showwarning("Error", "User does not exist")

        self.displayStaff()

class studentMenu:

    def __init__(self, username, access):
        self.root=Tk()
        self.username = username
        self.access = access
        self.createWidgets()
        self.displayStudent()


    def createWidgets(self):
        self.root.title("Students")
        Label(self.root, text='STUDENT MENU:').grid(row=0, column=0, columnspan=5, sticky=W+E)
        Button(self.root, text='Menu', width=7, command=self.mainMenu).grid(row=0, column=4, sticky=E)
        self.student_output = Frame(self.root, width=65, height=20, padx=20,pady=20, background='grey')
        self.student_output.grid(row=1, column=0, columnspan=5, sticky=W)

# Text Boxes
        Label(self.root, text='Username:').grid(row=2, column=1, sticky=W)
        self.student_username_entry = Entry(self.root, width=20, bg='grey')
        self.student_username_entry.grid(row=2, column=2, sticky=W)

        Label(self.root, text='First Name:').grid(row=3, column=1, sticky=W)
        self.student_firstname_entry = Entry(self.root, width=20, bg='grey')
        self.student_firstname_entry.grid(row=3, column=2, sticky=W)

        Label(self.root, text='Surname:').grid(row=4, column=1, sticky=W)
        self.student_surname_entry = Entry(self.root, width=20, bg='grey')
        self.student_surname_entry.grid(row=4, column=2, sticky=W)


# Labels and Buttons

        Label(self.root, text='Search Student').grid(row=2, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.searchStudent).grid(row=2, column=4, sticky=W)

        Label(self.root, text='Edit Student').grid(row=3, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.editStudent).grid(row=3, column=4, sticky=W)

        Label(self.root, text='Add Student').grid(row=4, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.addStudent).grid(row=4, column=4, sticky=W)

        Label(self.root, text='Delete Student').grid(row=5, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.deleteStudent).grid(row=5, column=4, sticky=W)


    def mainMenu(self):
        self.root.destroy()
        window = mainMenu(self.username, self.access)

    def addStudent(self):
        array = []
        newUsername = self.student_username_entry.get()
        newPassword = HashPassword("Password1")
        newFirstName = self.student_firstname_entry.get()
        newSurname = self.student_surname_entry.get()
        newAccess = "Student"

        for key in my_student.keys():
            array.append(key)

        array = quicksort(array)
        true_or_false = BinarySearch(array, 0, len(array)-1, newUsername)

        if true_or_false == False:
            d = datetime.now()
            my_student[newUsername] = Student(newFirstName, newSurname, newPassword, str(d.strftime("%A %B %d")), newAccess)
            self.displayStudent()
            SaveData(my_staff, my_student,my_user)  # saves the login to file
        else:
            messagebox.showwarning("User already exists")

    def displayStudent(self):
        self.student_output.destroy()
        self.student_output = Frame(self.root, width=65, height=20, padx=20,pady=20, background='grey')
        self.student_output.grid(row=1, column=0, columnspan=5, sticky=W)

        Label(self.student_output, anchor=W, text='Username', width=20, background='grey', font='default 12 bold').grid(row=0, column=0)
        Label(self.student_output, anchor=W, text='Full Name', width=20, background='grey', font='Default 12 bold').grid(row=0, column=1)
        Label(self.student_output, anchor=W, text='Last Login', width=20, background='grey', font='Default 12 bold').grid(row=0, column=2)

        array =[]
        for key in my_student.keys():
            array.append(key)
            array = quicksort(array)
        r = 1

        for key in array:
            Label(self.student_output, anchor=W, text=key, width=20, background='grey', font="Default 12").grid(row=r, column=0)
            Label(self.student_output, anchor=W, text=str(my_student[key].get_fullname()), width=20, background='grey', font="Default 12").grid(row=r, column=1)
            Label(self.student_output, anchor=W, text=str(my_student[key].get_login()), width=20, background='grey', font="Default 12").grid(row=r, column=2)
            r = r + 1

    def deleteStudent(self):
        deleteUsername = self.student_username_entry.get()
        del my_student[deleteUsername]
        SaveData(my_staff, my_student,my_user)#saves the login to file
        self.displayStudent()

    def searchStudent(self):
        array = []
        searchUsername = self.student_username_entry.get()

        for key in my_student.keys():
            array.append(key)

        array = quicksort(array)
        true_or_false = BinarySearch(array, 0, len(array)-1, searchUsername)

        if true_or_false == True:
            self.student_output.destroy()
            self.student_output = Frame(self.root, width=65, height=20, padx=20,pady=20, background='grey')
            self.student_output.grid(row=1, column=0, columnspan=5, sticky=W)
            Label(self.student_output, anchor=W, text='Username', width=20, background='grey', font='default 12 bold').grid(row=0, column=0)
            Label(self.student_output, anchor=W, text='Full Name', width=20, background='grey', font='Default 12 bold').grid(row=0, column=1)
            Label(self.student_output, anchor=W, text='Last Login', width=20, background='grey', font='Default 12 bold').grid(row=0, column=2)
            Label(self.student_output, anchor=W, text=searchUsername, width=20, background='grey', font="Default 12").grid(row=1, column=0)
            Label(self.student_output, anchor=W, text=str(my_student[searchUsername].get_fullname()), width=20, background='grey', font="Default 12").grid(row=1, column=1)
            Label(self.student_output, anchor=W, text=str(my_student[searchUsername].get_login()), width=20, background='grey', font="Default 12").grid(row=1, column=2)
        else:
            messagebox.showwarning("Error", "Test")

    def editStudent(self):
        username = self.student_username_entry.get()
        firstname = self.student_firstname_entry.get()
        surname = self.student_surname_entry.get()
        array=[]

        for key in my_student.keys():
            array.append(key)



        array = quicksort(array)
        true_or_false = BinarySearch(array, 0, len(array)-1, username)


        if true_or_false == TRUE:

            if firstname != "" and surname != "":

                my_student[username].edit_firstname(firstname)
                my_student[username].edit_surname(surname)
                SaveData(my_staff, my_student,my_user)#saves the login to file

            elif firstname != "":

                my_student[username].edit_firstname(firstname)
                SaveData(my_staff, my_student,my_user)#saves the login to file

            elif surname != "":

                my_student[username].edit_surname(surname)
                SaveData(my_staff, my_student,my_user)#saves the login to file

            else:
                messagebox.showwarning("Error", "I'm sorry, there's nothing to update")

        else:
            messagebox.showwarning("Error", "User does not exist")

        self.displayStudent()


class appointmentsMenu:

    def __init__(self, username, access):
        self.root=Tk()
        self.username = username
        self.access = access
        self.createWidgets()
        #self.displayAppointments()


    def createWidgets(self):
        self.root.title("Appointments")
        Label(self.root, text='Appointments:').grid(row=0, column=0, columnspan=5, sticky=W+E)
        Button(self.root, text='Menu', width=7, command=self.mainMenu).grid(row=0, column=4, sticky=E)
        self.appointments_output = Frame(self.root, width=65, height=20, padx=20,pady=20, background='grey')
        self.appointments_output.grid(row=1, column=0, columnspan=5, sticky=W)
        self.displayAppointment()

# Text Boxes

        Label(self.root, text='Teacher:').grid(row=2, column=1, sticky=W)
        #self.student_username_entry = Entry(self.root, width=20, bg='grey')
        #self.student_username_entry.grid(row=2, column=2, sticky=W)

        Label(self.root, text='Student:').grid(row=3, column=1, sticky=W)
        #self.student_firstname_entry = Entry(self.root, width=20, bg='grey')
        #self.student_firstname_entry.grid(row=3, column=2, sticky=W)



# Labels and Buttons
        Label(self.root, text='Add Appointment').grid(row=2, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.addAppointment).grid(row=2, column=4, sticky=W)

        Label(self.root, text='Search Appointment').grid(row=3, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.searchAppointment).grid(row=3, column=4, sticky=W)

        Label(self.root, text='Delete Appointment').grid(row=4, column=3, sticky=W)
        Button(self.root, text='OK', width=7, command=self.deleteAppointment).grid(row=4, column=4, sticky=W)

# Combo Boxes

        array =[]
        for key in my_staff.keys():
            array.append(key)
        array = quicksort(array)

        self.staff_combo_value = StringVar()
        self.staff_combo = ttk.Combobox(self.root, textvariable=self.staff_combo_value)
        self.staff_combo['values'] = array
        #self.staff_combo.current(0)
        self.staff_combo.grid(row = 2, column = 2, sticky=W)


        array =[]
        for key in my_student.keys():
            array.append(key)
        array = quicksort(array)

        self.student_combo_value = StringVar()
        self.student_combo = ttk.Combobox(self.root, textvariable=self.student_combo_value)
        self.student_combo['values'] = array
        #self.student_combo.current(0)
        self.student_combo.grid(row = 3, column = 2, sticky=W)


    def mainMenu(self):
        self.root.destroy()
        window = mainMenu(self.username, self.access)

    def displayAppointment(self):

        self.appointments_output.destroy()
        self.appointments_output = Frame(self.root, width=65, height=20, padx=20,pady=20, background='grey')
        self.appointments_output.grid(row=1, column=0, columnspan=5, sticky=W)

        Label(self.appointments_output, anchor=W, text='Student Name', width=20, background='grey', font='default 12 bold').grid(row=0, column=0)
        Label(self.appointments_output, anchor=W, text='Staff Name', width=20, background='grey', font='Default 12 bold').grid(row=0, column=1)

        r = 1

        for item in my_appointments:
            Label(self.appointments_output, anchor=W, text=item[0], width=20, background='grey', font="Default 12").grid(row=r, column=0)
            Label(self.appointments_output, anchor=W, text=item[1], width=20, background='grey', font="Default 12").grid(row=r, column=1)
            r = r + 1



    def addAppointment(self):
        newStaff = self.student_combo.get()
        newStudent = self.staff_combo.get()
        flag = True

        for item in my_appointments:
            if item[0] == newStaff and item[1] == newStudent:
                flag = False
                messagebox.showwarning("Error", "Appointment already exists")

        if flag == True:
            my_appointments.append([newStaff,newStudent])
            messagebox.showinfo("Informtion", "Appointment Added")

        for i in my_appointments:
            print()
            for j in i:
                print(j,end="\t")

        self.displayAppointment()



    def deleteAppointment(self):
        print("Hello World")
        #∞messagebox.showwarning("Error", "Test")

    def searchAppointment(self):
        searchStaff = self.student_combo.get()
        searchStudent = self.staff_combo.get()

        if searchStaff != "" and searchStudent != "":
            messagebox.showwarning("Error", "Please enter either a staff or student not both")
        else:
            r = 1
            self.appointments_output.destroy()
            self.appointments_output = Frame(self.root, width=65, height=20, padx=20,pady=20, background='grey')
            self.appointments_output.grid(row=1, column=0, columnspan=5, sticky=W)
            Label(self.appointments_output, anchor=W, text='Student Name', width=20, background='grey', font='default 12 bold').grid(row=0, column=0)
            Label(self.appointments_output, anchor=W, text='Staff Name', width=20, background='grey', font='Default 12 bold').grid(row=0, column=1)

            for item in my_appointments:
                if item[0] == searchStaff or item[1] == searchStudent:
                    Label(self.appointments_output, anchor=W, text=item[0], width=20, background='grey', font="Default 12").grid(row=r, column=0)
                    Label(self.appointments_output, anchor=W, text=item[1], width=20, background='grey', font="Default 12").grid(row=r, column=1)
                    r = r + 1



##### Main:


#creates an instance of the mainWindow class 
window = loginWindow()

 
mainloop()


