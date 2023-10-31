# # First Commit
# def dndmodifer(abscore):



#     return True


# def AbilityScoreChecker(abscore):

#     if abscore == 10 or abscore == 11:SWS
#         return 0
    
#     elif abscore == 12 or abscore == 13:
#         return 1




#     return True


# names = {"nick" : 37, "gabe" : 20}

# print (names["nick"])
#What do you do!? !?!YAY!
#yay i did it


#FIZZBuzz
#Write a function that takes in an arugement that should be an int.
# If that variable is divisible by 3 write Fizz the the console
# If that varibale is divisible by 5 write Buzz to the console
# If that variable is divislable by both 3 and 5 write FizzBuzz to the Console
# If that variable is divislbale by neither 3 or 5 don't write to the console. 

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 :
        print("Fizz")
    else:
        return False


x = input("enter a number ")

x = int(x)

fizzbuzz(x)

#haha!