"""A number-guessing game."""
from random import randint

# Put your code here
print('Howdy, Whats your name?')

#input the name and save it to a variable
name = input("type in your name:")
# we need to generate a random number between 1 and 100
print("I am thinking of a number between 1 and 100")
number = randint(1,100)
    
count = 0

    #loop untill the number is equal to the guess
while True:
    # prompt the player to guess the number
    guess = input("Guess the number: ")
    try: 
        guess = int(guess)
            
        if int(guess) < 1 or int(guess) > 100:
            print("Please only pick a number between 1 and 100")
            count+= 1
        elif int(guess) < number: 
            print("Your guess is too low, try again.")
            count += 1
        elif int(guess) < number:
            print("Your guess is too high, try again.")
            count += 1
        else:
            print("You are correct!")
            print(f"You guessed in {count} tries.")
            break
    except:
        print("please only enter an integer")
        count += 1
           
      


               




