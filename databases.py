import sqlite3

conn = sqlite3.connect('booking.db')
c = conn.cursor()

#Deleting table
#c.execute("DROP TABLE Usernames")

#Creating table
#c.execute("CREATE TABLE Usernames(username text, password text, fullname text)")
#c.execute("CREATE TABLE logins(username text, login_time date)")
#c.execute("CREATE TABLE groups(group_name text, group_description text)")
#c.execute("CREATE TABLE assign(group_name text, username text)")

##for count in range(2):
##    username = input('Add Username')
##    password = input('Add Passsword')
##    fullname = input('Sdd Fullname')
##   c.execute("INSERT INTO Usernames VALUES('" + username + "','" + password +"')")
##    c.execute("INSERT INTO Usernames VALUES ('%s', '%s', '%s')" % (username, password, fullname))

##for count in range(2):
##    username = input('Add Username')
##    password = input('Add Passsword')
##
##   c.execute("INSERT INTO Usernames VALUES('" + username + "','" + password +"')")
##   c.execute("INSERT INTO Usernames VALUES ('%s', '%s', '%s')" % (username, password, fullname))

##c.execute("INSERT INTO groups VALUES ('%s', '%s')" % ("ProjectA", "My first project"))
##c.execute("INSERT INTO assign VALUES ('%s', '%s')" % ("123", "ProjectA"))

conn.commit()

