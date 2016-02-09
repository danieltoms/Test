import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

def PrintData():

    print('Users Data')
    for row in c.execute('SELECT * FROM users ORDER BY username'):
            print(row)
    print()

    print("User Columns")
    for row in c.execute('PRAGMA table_info(users)'):
        print(row)
    print()
    print("staff data")
    for row in c.execute('SELECT * FROM staff ORDER BY staffID'):
            print(row)
    print()

    print("staff columns")
    for row in c.execute('PRAGMA table_info(staff)'):
        print(row)
    print()


    print("students data")
    for row in c.execute('SELECT * FROM students ORDER BY studentID'):
            print(row)
    print()

    print("student columns")
    for row in c.execute('PRAGMA table_info(students)'):
        print(row)
    print()

    print("appointments data")
    for row in c.execute('SELECT * FROM appointments ORDER BY studentID'):
            print(row)
    print()

    print("appointment columns")
    for row in c.execute('PRAGMA table_info(appointments)'):
        print(row)
    print()

    print("lesson data")
    for row in c.execute('SELECT * FROM lesson ORDER BY staff'):
            print(row)
    print()

    print("Tables")
    for row in c.execute('SELECT name FROM sqlite_master WHERE type="table"'):
            print(row)
    print()

    print("Load Staff")
    SQL = 'SELECT users.password, users.lastLogin, staff.staffID,staff.staffFirstname, staff.staffSurname'
    SQL = SQL + ' FROM staff'
    SQL = SQL + ' INNER JOIN users'
    SQL = SQL + ' ON users.username = staff.staffID;'

    print(SQL)
    for row in c.execute(SQL):
        print(row)
    print()

    print("Load Students")
    SQL = 'SELECT users.password, users.lastLogin, students.studentID,students.studentFirstname, students.studentSurname'
    SQL = SQL + ' FROM students'
    SQL = SQL + ' INNER JOIN users'
    SQL = SQL + ' ON users.username = students.studentID;'

    print(SQL)
    for row in c.execute(SQL):
        print(row)




PrintData()
