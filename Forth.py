# Game Excercise Example 
n=20
guess_number=1
print("You have only 5 times")
while int((guess_number<=5)):
    guess_number= int(input("Guess the no. \n"))
    if guess_number<20:
        print("You entered less number, please input greater number")
    elif guess_number>20:
        print("You entered greater number, please input less number")
        print(5-guess_number, "number of guesses left")
        guess_number= guess_number+1
        continue
    print("Congratulation!! You Won")
        # print(guess_number, "number of guesses took to finish")
    break
if(guess_number>5):
        print("You Lose!! Game Over")










