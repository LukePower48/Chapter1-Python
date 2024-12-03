from random import randint
def guessgame (max_guesses_allowed) :
    secret_number = randint(1, 5)
    print (max_guesses_allowed)  
    guess_count = 0
    user_guess = 0
    while (user_guess != secret_number and max_guesses_allowed > 0):
        user_guess = int(input("Enter your guess: "))
        guess_count += 1 #Increase guess_count by 1 if user_guess == secret_number: print("Congratulations! You win!")
        max_guesses_allowed -=1
        
        if user_guess == secret_number:
            print ("You win")
            print ("You took",guess_count, "guesses.")
        elif user_guess > secret_number:
             print ("Sorry! your guess was too high!")
        elif user_guess < secret_number:
            print ("Sorry! your guess was too high!")
print("Welcome to the guessing game!")
guessgame(3)
