#this programe demonstrates a guessing game
#get random number from another file
from random import randint
#get the user name
user_name = input("whats your name?")
print("hello there" + user_name)

#generate a random number
number = randint(10, 50)

#get user input

counter = 0
while counter < 5:
    user_number = eval(input("enter a number"))
    print(user_number)

