import random
number = random.randint(1,30)
life = 5
def game():
    global life
    while(life!=0):
        guess = int(input("Enter a number between 1 to 30...\n"))
        if (guess==number):
            print("Congratulations you have won this game!")
            print("Remaining life is : ", life)
            print("The correct number is : ", number)
            break
        elif (guess<number):
            life -= 1
            print("The number you have guessed is too low!, higher it a bit")
            print("Remaining life is : ", life)
        elif (guess>number):
            life -= 1
            print("The number you have guessed is too high! lower it a bit")
            print("Remaining life is : ", life)
        
        if (life==0):
            print("The number is : ", number)
            break

game()