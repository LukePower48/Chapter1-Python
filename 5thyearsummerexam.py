import numpy as np

'''Task 1'''
# students =[45,97,9,10,8,85,64,56,1,4,25,36,78]
# missingstudent = int(input('Enter a new grade of 100 for this student: '))
# students.append(missingstudent)                 
# while min((students)) < 10:
#     students.sort()
#     students.pop(0)
# students.reverse()
# print (students)
# print('There are',len((students)),'students in the list')
# print ('average grade = ',np.mean(students))
# print ('highest grade = ',max(students))
# print ('lowst grade = ',min(students))



'''Task 3'''
password = 'secret'
counter = 3
while counter >0:
    userguess = input('What is your password? ')
    if password == userguess:
        print('Password correct, access granted')
        break
    else:
        print('Incorrect password, please try again')
        counter -=1
    if counter == 0:
        print('You have been locked out of your account')
        break

    
