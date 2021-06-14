# Q. Generate a random no. and ask user to guess it, if correct then congrats,
#  if higher then choose smaller, if smaller then choose higher and lastly 
# calculate the total no. of guess.
import random 
randomNumber = random.randint(1,100)
# print(randomNumber)
userGuess = None
guesses = 0
while(userGuess != randomNumber): 
    userGuess = int(input("Guess the number : "))
    guesses += 1 
    if(userGuess==randomNumber):
        print("Congratulation! You Win...")
    else:
        if(userGuess>randomNumber):
            print("You guessed it Wrong! Please enter smaller number")
        else:
            print("You guessed it Wrong! Please enter higher number")
print(f"The Total No. of Guessing is : {guesses}")

