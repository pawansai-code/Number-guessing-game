#guess the number from 1 to 10

from random import randint
lower_num, higher_num=1, 10
random_number: int=randint(lower_num, higher_num)
print(f"Guess the Number in the range from{lower_num} to {higher_num}.")
while True:#infinite loop
    try:
        user_guess: int=int(input("guess:"))
    except valueErrror as e:
        #shows warning or raise exception if its not in the integer format 
        print("please enter the valid number.")
        continue
    if user_guess > random_number:
        print("the number is lower")
    elif user_guess < random_number:
        print("the number is higher")
    else:
        print("you guessed the number")
        break
            #come out of the loop
    
