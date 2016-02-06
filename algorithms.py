# menu.py is a quick revision application.
from new_algorithms import *
import random
import re
import csv
import sqlite3

Connection = sqlite3.connect('booking.db')
c = Connection.cursor()


# Initialise & assigning variables:
response=("I am afraid not. Please try again.",
         "That is a good password but not my password Keep guessing.",
         "That is not my password. It really is easy to guess my password.",
         "Well done! You must work for MI6. Give my regards to James Bond.",
          "You\'ve had four attempts")
usernames = []

#Checking if a username exists
def username_correct(usernames,username):
    itemFound = BinarySearch(usernames, 0, len(usernames)-1, username) 
    if itemFound == -1: #changed expression from False to -1
        print("Username not found")
    else:
        print("Username found")
    return itemFound

'''
# Function to find out if the user has guessed password correctly:
def is_correct(users_guess, users_password, usernames):
    validPassword = False
    for count in range (0 , len(usernames)):
        if usernames[count][0] == users_guess and usernames[count][1] == users_password:
           print("User's guess", users_guess )
           validPassword = True
    return validPassword
'''

'''
# Load the usernames and passwords from the database table to 2D usernames array
def LoadUsernamesDatabase(usernames): #Loads usernames from database

    SQL = "SELECT username,password FROM Usernames ORDER BY username"
    for row in c.execute(SQL):
        usernames.append([row[0],row[1]])
    print(usernames)
    Connection.commit()
'''

# Load the usernames and passwords from the database table to array of objects
def LoadUsernamesDatabase(usernames): #Loads usernames from database
    SQL = "SELECT * FROM Usernames ORDER BY username"
    for row in c.execute(SQL):
        usernames.append(Username(row[0],row[1],row[2]))
    Connection.commit()
# Print usernames
    for x in usernames:
        print(x.get_username(), x.password)


# def LoadAdminUsers( ):
#     SQL = "SELECT username FROM Usernames WHERE admin = True ORDER BY username"
    


# Saves the usernames and passwords to the database table from the 2D usernames array **Not Used**     
def SaveUsernamesDatabase(usernames): #Save usernames to database
    c.execute("DELETE FROM Usernames")
    for item in usernames:
        username = item.username #Updated to access class attributes
        password = item.password
        fullname = item.fullname
        c.execute("INSERT INTO Usernames VALUES ('%s', '%s','%s')" % (username, password, fullname))
        Connection.commit()

"""
def LoadUsernames(usernames): #load usernames from file
    with open('usernames.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            usernames.append([line[0],line[1]])
        print(usernames)

"""




#           (			    #   Start of group
#           (?=.*\d)		#   must contain one digit from 0-9
#           (?=.*[a-z])		#   must contain one lowercase characters
#           (?=.*[A-Z])		#   must contain one uppercase characters
#           (?=.*[@#$%])	#   must contain one special symbols in the list "@#$%"
#           .		        #   match anything with previous condition checking
#           {6,20}	        #   length at least 6 characters and maximum of 20
#           )			    #   End of group
#


#gets the username and performs validation checks    
def get_username():
    users_guess = input("What is your username ")
    while not (length_check(users_guess, 4) and type_check(users_guess)):
          users_guess = input("Invalid Username: Please try again")
    return users_guess

#As above but for the password, uses regular expressions to test password strength
def get_password():
    users_password = input("What is your password")
    while not (RegularExpressions(users_password)):
          users_password = input("Invalid Password: Please try again")         
    return users_password

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Add a new username and password')
  print('2. Change a user\'s password')
  print('3. Delete a user')
  print('4. Show an ordered list of users')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

#No validation on menu choice, yet!
def GetMenuChoice():
  Choice = input()
  print()
  return Choice

#Adds new user to the 2D and also to the database
def AddNewUser(usernames):
    password1, password2 = " ",""
    user_exists = 0
    print("Add New User")
    
    while user_exists != -1:
        username = get_username()
        user_exists = username_correct(usernames,username)

    while not password1 == password2:
        password1 = get_password()
        password2 = get_password()

    usernames.append(Username(username,password1)) #update list
    SaveUsernamesDatabase(usernames) #update database
    BubbleSort(usernames)   #print list
        

def login(usernames): #Created a new subroutine for the login process
    attempts = 0
    users_guess = -1
    print("Hello.\n")
    
    # call username and password input functions

    while users_guess == -1: #Had to change the condition
        username = get_username()
        users_guess = username_correct(usernames,username)

    users_password = get_password()
    
    # Check to see if user's password is correct
    true_or_false = usernames[users_guess].check_password(users_password)

    # Run the game until the user is correct:
    while true_or_false == False and attempts < 3:
        print (response[random.randint(0,2)]) #random response each time

        # Collect the user's next guess:
        users_password = get_password()

        # Use our function again:
       
        true_or_false = usernames[users_guess].check_password(users_password)
        attempts = attempts + 1    

    if true_or_false:
               print(response[3])
               Choice = ''#if successful Choice is set to nothing''
    else:
               print(response[4])
               Choice = 'q'#if unsuccessful Choice is set to q, so that menu is never displayed 
    return Choice


"""
#You use the ennumerate function to access the index rather than the value of a two dimentional array
def in_list(username, usernames): 
    for i, j in enumerate(usernames):
        if username in j: #if the username is in the sublist 
            return i #Return the index number of the sublist
    return -1
"""

# Changes the users password in the 2D list and on the database
def ChangeUserPassword(usernames):
    password1, password2 = " ",""
    user_exists = False
    print("Edit Users Password")
    
    while not user_exists:
        username = get_username()
        user_exists = username_correct(usernames,username)

    while not password1 == password2:
        password1 = get_password()
        password2 = get_password()

        #i = in_list(username,usernames)

    usernames[user_exists].change_password(password1)
    SQL = "UPDATE Usernames SET password = '%s' WHERE username = '%s' " % (password1, username,)
    print(SQL)
    c.execute(SQL) 
    Connection.commit()

#Delete a user from the 2D List and then the database
def DeleteUser(usernames):
    
    user_exists = False
    print("Delete Users")
    
    while not user_exists:
        username = get_username()
        user_exists = username_correct(usernames,username)
#        i = in_list(username,usernames)

        del usernames[user_exists]

        SQL = "DELETE FROM Usernames WHERE username = '%s'" % username 
        print(SQL)
        c.execute(SQL) 
        Connection.commit()
        BubbleSort(usernames)

if __name__ == "__main__":
    
    # Start the game:
    LoadUsernamesDatabase(usernames)
    Choice = login(usernames)
    
    while Choice != 'q':
        DisplayMenu()
        Choice = GetMenuChoice()
        if Choice == '1':
            AddNewUser(usernames)
        elif Choice == '2':
            ChangeUserPassword(usernames)
        elif Choice == '3':
            DeleteUser(usernames)
        elif Choice == '4':
            BubbleSort(usernames)  

    # End the game:

    input("\n\n\nPress RETURN to exit.")
