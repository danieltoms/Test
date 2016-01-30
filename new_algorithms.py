import re
import random


def BubbleSort(my_list):
    for count in range (0, len(my_list)-1):
        for count2 in range (0, len(my_list)-1):
            if my_list[count2].get_username() > my_list[count2+1].get_username():
                temp = my_list[count2]
                my_list[count2] = my_list[count2+1]
                my_list[count2+1] = temp
    for i in my_list:
            print(i.get_username())

def BinarySearch(my_list, first, last, itemSought):
##    BubbleSort(my_list)
    my_list = quicksort(my_list)
    midpoint = (first + last) //2

    if my_list[midpoint].get_username() == itemSought:
        itemFound = midpoint #changd False to midpoint so that it can identify the object it has found
                
    else:
        if first >= last:
            itemFound = -1 #-1 because it hasn't found an object
        else:
            if my_list[midpoint].get_username()<itemSought:
                itemFound = BinarySearch(my_list, midpoint+1, last, itemSought)
            else:
                itemFound = BinarySearch(my_list, first, midpoint-1, itemSought)
 
    return itemFound

def quicksort(array):
        less = []
        equal = []
        more = []

        if len(array) > 1:
            pivot = array[random.randint(0,len(array)-1)].get_username()
            for x in array:
                if x.get_username() < pivot:
                    less.append(x)
#                   printarray("less", less)
                elif x.get_username() == pivot:
                    equal.append(x)
#                    printarray("equal", equal)
                else:
                    more.append(x)
#                    printarray("more",more)

            less = quicksort(less)
            more = quicksort(more)
            array = less + equal + more
        return array

def length_check(user_string, length): # Validates any string for any length
    return len(user_string) > 0 and len(user_string) < length

def type_check(user_string): # checks to see if a string is a digit
    return user_string.isdigit()# returns true if all characters are digits 

def RegularExpressions(new_password):
    if re.match(r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{6,20})', new_password):
        return True
    else:
        return False

def printarray(label, array):
     for x in array:
        print(label,x.get_username())

def stack_pop(stack_array):
	for i in range (len(stack_array)):
		print(stack_array.pop())
	
class Username:

    #constructor

    def __init__(self, username, password):
        self.username = username
        self.password = password
   
        
    def get_username(self):
        return self.username

    def check_password(self, password):
        return self.password == password

    def change_password(self,password):
        self.password = password


if __name__ == "__main__":
##    # Simple test to ensure BubbleSort works
##    test_array = [["a",1],["d",4],["c",6],["b",8]]
##    BubbleSort(test_array)
##    print('BubbleSort:', test_array)
##
##    # More complicated test to ensure that QuickSort works
##    test_array = [["a",1],["d",4],["c",6],["b",8]]
##    quicksort(test_array)
##    print('quicksort:', test_array)

### Simple test to ensure BubbleSort works with Username class
##    test_array = []
##    test_array.append(Username("KLN","$Password1"))
##    test_array.append(Username("DST","$Password2"))
##    test_array.append(Username("WBT","$Password2"))
##    print(test_array)
##    test_array = quicksort(test_array)
##    for x in test_array:
##        print(x.get_username())


# Simple test to ensure database works with Username class
#     import sqlite3
#     Connection = sqlite3.connect('booking.db')
#     c = Connection.cursor()
#     test_array = []
#     SQL = "SELECT username,password FROM Usernames ORDER BY username"
#     for row in c.execute(SQL):
#         test_array.append(Username(row[0],row[1]))
# 
#     Connection.commit()
# 
#     for x in test_array:
#         print(x.get_username(), x.password)
       
# Simple test to ensure BinarySearch works with Username class
#     
#     username = "123"
#     password = "$Password1"
#     test_array = quicksort(test_array)
#     i = BinarySearch(test_array, 0, len(test_array)-1, username)
#     print(i) 
#     if test_array[i].check_password(password):
#         print("success")
#     else:
#         print("fail")

    test_array = []
    test_array.append(1)
    test_array.append(2)
    test_array.append(3)
    
    for i in test_array:
    	print(test_array.pop())
    
    stack_pop(test_array)
    	