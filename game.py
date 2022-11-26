import random
from colorama import Fore
number = random.randint(1,30)
life = 5
def game():
    global life
    while(life!=0):
        print(number)
        guess = int(input(Fore.WHITE + "Enter a number between 1 to 30...\n"))
        if (guess==number):
            print(f"{Fore.RED}Congratulations {Fore.YELLOW}you {Fore.GREEN}have {Fore.CYAN}won {Fore.BLUE}this {Fore.MAGENTA}game!{Fore.WHITE}")
            print(Fore.WHITE + f"Remaining life is : {Fore.GREEN}", life)
            print(Fore.WHITE + f"The number is : {Fore.GREEN}", number)
            break
        elif (guess<number):
            life -= 1
            print(f"{Fore.WHITE}The number you have guessed is too low!, higher it a bit")
            print(f"Remaining life is : {Fore.RED}", life)
        elif (guess>number):
            life -= 1
            print(Fore.WHITE + "The number you have guessed is too high! lower it a bit")
            print(f"Remaining life is : {Fore.RED}", life)
        
        if (life==0):
            print(Fore.WHITE + f"The number is : {Fore.RED}", number)
            break

game()