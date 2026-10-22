import random 

def play_game():
    lucky_num = random.randint(1, 100)

    while True:
        user_guess = int(input("Guess a number between 1 and 100:"))
        if user_guess == lucky_num:
            print("Congratulations you win!")
            break
        elif user_guess < lucky_num:
            print("your guess is too low,try again")
        elif user_guess > lucky_num:
            print("your guess is too high,try again")
        else:
            print("Invalid input,please enter a number between 1 and 100")

    

play_game()