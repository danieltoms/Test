import sqlite3

conn = sqlite3.connect('booking.db')
c = conn.cursor()

#Deleting table
c.execute("DROP TABLE Usernames")

#Creating table
c.execute("CREATE TABLE Usernames(username text, password text, fullname text)")
c.execute("CREATE TABLE logins(username text, login_time date)")

for count in range(2):
    username = input('Add Username')
    password = input('Add Passsword')
    fullname = input('Sdd Fullname')
#   c.execute("INSERT INTO Usernames VALUES('" + username + "','" + password +"')")
    c.execute("INSERT INTO Usernames VALUES ('%s', '%s', '%s')" % (username, password, fullname))

for count in range(2):
    username = input('Add Username')
    password = input('Add Passsword')

#   c.execute("INSERT INTO Usernames VALUES('" + username + "','" + password +"')")
    c.execute("INSERT INTO Usernames VALUES ('%s', '%s', '%s')" % (username, password, fullname))



conn.commit()

