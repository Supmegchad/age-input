import random

UserAge = input("please input your age   ")

#Turns the user's input from a string into an integer.
try:
    AgeStr = int(UserAge)
except:
    print("you suck at this")
    exit()

#Generates a random number that will be used to determine the age in N amount of years.
YearsLater = random.randint(1,3)

if YearsLater == 1:
    print("in 1 year, your age will be ", AgeStr+1)
elif YearsLater == 2:
    print("in 2 years, your age will be", AgeStr+2)
elif YearsLater == 3:
    print("in 3 years, your age will be", AgeStr+3)
