from new_algorithms import *
from algorithms import *
from tkinter import *
import time

# Initialise & assigning variables:
usernames = []
response=("I am afraid not. Please try again.",
         "That is a good password but not my password Keep guessing.",
         "That is not my password. It really is easy to guess my password.",
         "Well done! You must work for MI6. Give my regards to James Bond.",
          "You\'ve had four attempts")

class loginWindow:

    def __init__(self):
        self.root=Tk()
        self.createWidgets()
        self.attempts = 0

    def createWidgets(self):
        
        self.root.title("Login Window")
        self.output = Text(self.root, width=40, height=2, wrap=WORD, background='white', foreground = "red")
        self.output.grid(row=0, column=2, sticky=W)

        self.output.delete(0.0, END)
        self.output.insert(END, "Hello. \n")
        self.output.insert(END, "Please enter your username and password")        

        Label(self.root, text='Username:').grid(row=1, column=0, sticky=W)
        self.username_entry = Entry(self.root, width=20, bg='grey')
        self.username_entry.grid(row=1, column=2, sticky=W)

        Label(self.root, text='Password:').grid(row=2, column=0, sticky=W)
        self.password_entry = Entry(self.root, width=20, bg='grey',show="*")
        self.password_entry.grid(row=2, column=2,sticky=W)

        #Add a submit button
        Button(self.root, text='SUBMIT', width=7, command=self.login).grid(row=3, column=2, sticky=W)

    def login(self):
        
    
        username = self.username_entry.get()
        users_guess = username_correct(usernames,username)
        
        if users_guess == -1:
            self.output.delete(0.0, END)
            self.output.insert(END, "Username not found")
            self.username_entry.delete(0, END)

        else:
            users_password = self.password_entry.get()
            true_or_false = usernames[users_guess].check_password(users_password)

            
            if true_or_false:
                messagebox.showinfo("Welcome", response[3])
                push_stack(username)
                self.root.destroy()
                window = menuWindow()

            elif self.attempts < 3:
                self.output.delete(0.0, END)
                self.output.insert(END, response[random.randint(0,2)])
                self.password_entry.delete(0, END)
                self.attempts = self.attempts + 1

            else:
                messagebox.showwarning("Error", response[4])
                self.root.destroy()
                

class menuWindow:

    def __init__(self):
        self.root=Tk()
        self.createWidgets()

    def createWidgets(self):
        
        self.root.title("Menu Window")
        self.menu_output = Text(self.root, width=40, height=2, wrap=WORD, background='white', foreground = "red")
        self.menu_output.grid(row=0, column=0, sticky=W)

        self.menu_output.delete(0.0, END)
        self.menu_output.insert(END, "Please choose an option:")        

        #Add menu buttons
        Label(self.root, text='1. Add a new username and password').grid(row=1, column=0, sticky=W)
        Button(self.root, text='Go', width=7, command=self.addUser).grid(row=1, column=1, sticky=W)

        Label(self.root, text='2. Change a user\'s password').grid(row=2, column=0, sticky=W)
        Button(self.root, text='Go', width=7, command=self.changeUser).grid(row=2, column=1, sticky=W)

        Label(self.root, text='3. Delete a user').grid(row=3, column=0, sticky=W)
        Button(self.root, text='Go', width=7, command=self.deleteUser).grid(row=3, column=1, sticky=W)

        Label(self.root, text='4. Login History').grid(row=4, column=0, sticky=W)
        Button(self.root, text='Go', width=7, command=self.loginUser).grid(row=4, column=1, sticky=W)

        Label(self.root, text='4. Show an ordered list of users').grid(row=5, column=0, sticky=W)
        Button(self.root, text='Go', width=7, command=self.showUser).grid(row=5, column=1, sticky=W)

        Label(self.root, text='5. Show an ordered list of admins').grid(row=6, column=0, sticky=W)
        Button(self.root, text='Go', width=7, command=self.showUser).grid(row=6, column=1, sticky=W)

    def addUser(self):
        newuser = AddUserDialog(self.root, title = "Add User")

        if newuser.result is not None: #In case cancel on dialog is pressed and no username or password is given    
            if newuser.username == "":
            	self.menu_output.delete(0.0, END)
            	self.menu_output.insert(END, "Please enter a username")
            elif not(length_check(newuser.username, 4) and type_check(newuser.username)):
                print(length_check(newuser.username, 4), type_check(newuser.username))
                self.menu_output.delete(0.0, END)
                self.menu_output.insert(END,"Invalid Username: Please try again")
            else:
                user_exists = username_correct(usernames,newuser.username)
                if user_exists == -1:
                    if newuser.password == "":
                        self.menu_output.delete(0.0, END)
                        self.menu_output.insert(END, "Please enter a password")
                    elife RegularExpressions(newuser.password) == False:
                        self.menu_output.delete(0.0, END)
                        self.menu_output.insert(END, "Invalid Password: Please try again")
                    else:
                        usernames.append(Username(newuser.username,newuser.password,newuser.fullname)) #update list
                        SaveUsernamesDatabase(usernames) #update database
                        BubbleSort(usernames)   #print list
                else:
                    self.menu_output.delete(0.0, END)
                    self.menu_output.insert(END, "User already exists")
	                
            
    def changeUser(self):
        #This routine will update a users password, it uses a dialog box to get the username and two passwords
        #If the user exists and the two passwords match the password is changed in both the database and the username object

        newuser = ChangeUserDialog(self.root, title = "Change Password") #Creates a new instance of ChangeUserDialog

        if newuser.result is not None: #In case cancel on dialog is pressed and no username or password is given
            
            #If username has been given check that it already exits
            if newuser.username == "":
                self.menu_output.delete(0.0, END)
                self.menu_output.insert(END, "Please enter a username")
            else:
                user_exists = username_correct(usernames,newuser.username)

            if user_exists != -1: #username_correct routine will return -1 if the user does not exist

                if newuser.password == "": #Checks the password has been entered
                    self.menu_output.delete(0.0, END)
                    self.menu_output.insert(END, "Please enter a password")

                elif newuser.password2 == "": #Checks the second password has been entered
                    self.menu_output.delete(0.0, END)
                    self.menu_output.insert(END, "Please re-enter a password")

                elif newuser.password != newuser.password2: #Checks the two passwords match
                    self.menu_output.delete(0.0, END)
                    self.menu_output.insert(END, "Please re-enter a password")
                else:
                    usernames[user_exists].change_password(newuser.password)# Calls the username objects method for changing passwords
                    # I could call the routine SaveUsernamesDatabase to update the whole database, in this case I'm just updating the password field
                    SQL = "UPDATE Usernames SET password = '%s' WHERE username = '%s' " % (newuser.password, newuser.username,) 
                    print(SQL)
                    c.execute(SQL) 
                    Connection.commit()
                    
            else:
                self.menu_output.delete(0.0, END)
                self.menu_output.insert(END, "User doesn't exists")

    def deleteUser(self):
        messagebox.showinfo("Delete User", "Do you want to delete a user?")

    def showUser(self):
    	Data_Item = pull_stack()
    	message = "The last user was " + str(Data_Item)
    	messagebox.showinfo("Show User", message)

    def loginUser(self):
        message = "The last users were: \n"
        StackMaximum,StackPointer = LoadStack()
        print("StackMaximum3", StackMaximum)
        print("StackPointer3", StackPointer)
        print("StackArray3", StackArray)
        
        for i in range(StackPointer+1):
            Data_Item = pull_stack()
            message = message + str(Data_Item) + "\n"
        messagebox.showinfo("Show User", message)


class AddUserDialog(simpledialog.Dialog):

    def body(self, master):

        Label(master, text="Username:").grid(row=0)
        Label(master, text="Password:").grid(row=1)
        Label(master, text="Full Name:").grid(row=2)
		
        self.username_entry = Entry(master)
        self.password_entry = Entry(master)
        self.fullname_entry = Entry(master)

        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)
        self.fullname_entry.grid(row=2, column=1)
        return self.username_entry # initial focus

    def apply(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.fullname = self.fullname_entry.get()
        self.result = "success"
        



class ChangeUserDialog(simpledialog.Dialog):

    def body(self, master):
        Label(master, text="Username:").grid(row=0)
        Label(master, text="Password:").grid(row=1)
        Label(master, text="Re-enter Password:").grid(row=2)

        self.username_entry = Entry(master)
        self.password_entry = Entry(master)
        self.password_re_entry = Entry(master)

        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)
        self.password_re_entry.grid(row=2, column=1)
        
        return self.username_entry # initial focus

    def apply(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.password2 = self.password_re_entry.get()
        self.result = "success"
        
        

if __name__ == "__main__":
    #creates an instance of the mainWindow class
##    c.execute("DELETE FROM Usernames")
##    c.execute("INSERT INTO Usernames VALUES ('%s', '%s')" % ("123", "$Password1",))
    LoadUsernamesDatabase(usernames)
    StackMaximum,StackPointer = LoadStack()
    print("StackMaximum1", StackMaximum)
    print("StackPointer1", StackPointer)
    print("StackArray1", StackArray)
    window = loginWindow()
    mainloop()
