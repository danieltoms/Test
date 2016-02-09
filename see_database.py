import sqlite3

conn = sqlite3.connect('booking.db')
c = conn.cursor()

def PrintData():

    print('Users Data')
    for row in c.execute('SELECT * FROM Usernames ORDER BY username'):
            print(row)
    print()

    print('groups Data')
    for row in c.execute('SELECT * FROM groups ORDER BY group_name'):
            print(row)
    print()

    print('assign Data')
    for row in c.execute('SELECT * FROM assign ORDER BY group_name'):
            print(row)
    print()

    print("User Columns")
    for row in c.execute('PRAGMA table_info(Usernames)'):
        print(row)
    print()

    print("groups Columns")
    for row in c.execute('PRAGMA table_info(groups)'):
        print(row)
    print()
    
    print("assign Columns")
    for row in c.execute('PRAGMA table_info(assign)'):
        print(row)
    print()
    
    print("Tables")
    for row in c.execute('SELECT name FROM sqlite_master WHERE type="table"'):
            print(row)
    print()


PrintData()
