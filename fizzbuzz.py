#Has this changed?
HowFar = int(input("How far to count"))
while HowFar < 1:
    HowFar = int(input("Not a valid number, please try again"))
for myloop in range (1, HowFar +1):
    if myloop %3 == 0 and myloop %5 == 0:
        print("FizzBuzz")
    elif myloop % 3 == 0:
        print("Fizz")
    elif myloop % 5 == 0:
        print("Buzz")
    else:
        print(myloop)
