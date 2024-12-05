from random import randint

user_score = 0
# secret_number = randint (1,100)
# user_input = int(input("Enter your guess: "))
# difference = (secret_number - user_input)
while True:
    
    if user_input == secret_number:
        user_score+=100

    elif difference in range (11,20) or (-11,-20):
         user_score += 80
         print ("You score 80 points!")
    elif difference in range (21,30) or (-21,-30):
        user_score += 70
        print ("You score 70 points!")
    elif difference in range (31,40) or (-31,-40):
        user_score += 60
        print ("You score 60 points!")
    elif difference in range (41,50) or (-41,-50):
        user_score += 50
        print ("You score 50 points!")
    elif difference in range (51,60) or (-51,-60):
        user_score += 40
        print ("You score 40 points!")
    elif difference in range (61,70) or (-61,-70):
        user_score += 30
        print ("You score 30 points...")
    elif difference in range (71,80) or (-71,-80):
        user_score += 20
        print ("You score 20 points...")
    elif difference in range (81,90) or (-81,-90):
        user_score += 90
        print ("You score 10 points...")
    elif difference in range (91,100) or (-91,-100):
        user_score += 90
        print ("You score 0 points......")
    else:
            print ("uh")
# while True:
#     secret_number = randint (1,100)
#     user_input = int(input("Enter your guess: "))
#     diff = (secret_number - user_input)
#     print ("secret number was ",secret_number,"You guessed ",user_input,"Difference was ",diff)
#     if user_input == secret_number:
#         user_score+=100
#     print ("JACKPOT!!! You score 100 points")
# #     elif diff in range (1,10) or (-1,-10):
# #         user_score += 90
# #         print ("You score 90 points!")
