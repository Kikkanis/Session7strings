name = input("what is your name? ")
# lets try this in a simpler way
age2 = input(f"how old are you {name}? ")
try:
    age2 = int(age2) # here there can be a problem
    print(f"{name}, you were born in {2024 - age2}")
    7 / 0
except ValueError:
    print("please enter a valid value for age")
    print("i can also print this in case of error that i prevented")
except ZeroDivisionError:
    print("you can not divide by 0!")
except:
    print("this is another type of error")
else: # this is for no exception
    print("thank you for playing as expected")
finally: # this will be excecuted no matter what, at the very end
    print("thanks for playing the game")

