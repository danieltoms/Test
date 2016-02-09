from datetime import datetime
import random
import sqlite3
import re

conn = sqlite3.connect('example.db')
c = conn.cursor()



def LoadAppointments(my_appointments):
    my_appointments.clear
    SQL = 'Select *'
    SQL = SQL + ' FROM appointments'

def LoadUsers(my_user):
    my_user.clear()
    SQL = 'SELECT *'
    SQL = SQL + ' FROM users'

    for row in c.execute(SQL):
        username = row[0]
        password = row[1]
        last_login = row[2]
        access = row[3]
        my_user[username] = Username(password, last_login, access)

def LoadStaff(my_staff): #load usernames from file

    SQL = 'SELECT users.password, users.lastLogin, staff.staffID,staff.staffFirstname, staff.staffSurname, users.userAccess'
    SQL = SQL + ' FROM staff'
    SQL = SQL + ' INNER JOIN users'
    SQL = SQL + ' ON users.username = staff.staffID;'

    for row in c.execute(SQL):
        password = row[0]
        last_login = row[1]
        staffID = row[2]
        staffFirstname = row[3]
        staffSurname = row[4]
        access = row[5]
        my_staff[staffID] = Staff(staffFirstname, staffSurname, password, last_login, access)

def LoadStudents(my_student): #load usernames from file

    SQL = 'SELECT users.password, users.lastLogin, students.studentID, students.studentFirstname, students.studentSurname, users.userAccess'
    SQL = SQL + ' FROM students'
    SQL = SQL + ' INNER JOIN users'
    SQL = SQL + ' ON users.username = students.studentID;'

    for row in c.execute(SQL):
        password = row[0]
        last_login = row[1]
        studentID = row[2]
        studentFirstname = row[3]
        studentSurname = row[4]
        access = row[5]
        my_student[studentID] = Student(studentFirstname, studentSurname, password, last_login, access)

def SaveData(my_staff, my_student, my_user): #Save usernames to file
    c.execute("DELETE FROM users")
    for key in my_staff:
        username = key
        password = str(my_staff[key].password)
        last_login = str(my_staff[key].last_login)
        access = str(my_staff[key].access)
        c.execute("INSERT INTO users VALUES ('%s', '%s', '%s', '%s')" % (username, password, last_login, access,))
        conn.commit()

    for key in my_student:
        username = key
        password = str(my_student[key].password)
        last_login = str(my_student[key].last_login)
        access = str(my_student[key].access)
        c.execute("INSERT INTO users VALUES ('%s', '%s', '%s', '%s')" % (username, password, last_login, access,))
        conn.commit()

    LoadUsers(my_user)

    c.execute("DELETE FROM staff")
    for key in my_staff:
        username = key
        firstname = str(my_staff[key].firstname)
        surname = str(my_staff[key].surname)
        c.execute("INSERT INTO staff VALUES ('%s', '%s', '%s')" % (username, firstname, surname, ))
        conn.commit()

    c.execute("DELETE FROM students")
    for key in my_student:
        username = key
        firstname = str(my_student[key].firstname)
        surname = str(my_student[key].surname)
        c.execute("INSERT INTO students VALUES ('%s', '%s', '%s')" % (username, firstname, surname, ))
        conn.commit()


def quicksort(array):
        less = []
        equal = []
        more = []

        if len(array) > 1:
            pivot = array[random.randint(0,len(array)-1)]
            for x in array:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                else:
                    more.append(x)

            less = quicksort(less)
            more = quicksort(more)
            array = less + equal + more
        return array

def BinarySearch(array, first, last, itemSought):
        global itemFound
        global searchFailed

        itemFound = False
        searchFailed = False

        midpoint = (first + last)//2

        if array[midpoint] == itemSought:
            itemFound = True
        else:
            if first >= last:
                searchFailed = True
            else:
                if array[midpoint] < itemSought:
                    BinarySearch(array, midpoint+1, last, itemSought)
                else:
                    BinarySearch(array, first, midpoint-1, itemSought)

        if searchFailed == True:
            return False
        if itemFound == True:
            return True

def HashPassword(password):
    total = 0
    for letter in password:
        total = total + ord(letter) * password.index(letter)
        hashedAddress = (total % 1000) + 1
    return hashedAddress

#           (			    #   Start of group
#           (?=.*\d)		#   must contain one digit from 0-9
#           (?=.*[a-z])		#   must contain one lowercase characters
#           (?=.*[A-Z])		#   must contain one uppercase characters
#           (?=.*[@#$%])	#   must contain one special symbols in the list "@#$%"
#           .		        #   match anything with previous condition checking
#           {6,20}	        #   length at least 6 characters and maximum of 20
#           )			    #   End of group
#


def RegularExpressions(new_password):
    if re.match(r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{6,20})', new_password):
        return True
    else:
        return False


class Username:
# constructor
        idCounter = 0
        
        def __init__(self, password, last_login, access):
                self.password = password
                self.access = access
                self.last_login = last_login

        def login(self,password):
            return self.password == str(HashPassword(password))

        def get_login(self):
                return self.last_login
            
        def get_password(self):
                return self.password

        def edit_login(self):
                d = datetime.now()
                self.last_login = d.strftime("%A %B %d")

        def edit_password(self,new_password):
                self.password = new_password

        def get_access(self):
                return self.access

class Staff(Username):
# constructor

        def __init__(self, firstname, surname, password, last_login, access):
                Username.__init__(self,password,last_login, access)
                self.firstname = firstname
                self.surname = surname

        def get_fullname(self):
                return self.firstname + ' ' + self.surname

        def edit_firstname(self, new_firstname):
            self.firstname = new_firstname

        def edit_surname(self,new_surname):
                self.surname = new_surname


class Student(Username):
# constructor

        def __init__(self, firstname, surname, password, last_login, access):
                Username.__init__(self,password,last_login, access)
                self.firstname = firstname
                self.surname = surname

        def get_fullname(self):
                return self.firstname + ' ' + self.surname

        def edit_firstname(self, new_firstname):
            self.firstname = new_firstname

        def edit_surname(self,new_surname):
                self.surname = new_surname
