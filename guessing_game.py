# program to play with user in number guessing
import math  # import math module
import random  # import random module
a = []  # initiate empty list named a
a.append(random.randint(1, 99))  # add random number between 1 and 99 to list a
a.append(random.randint(1, 99))  # add random number between 1 and 99 to list a
a.append(random.randint(1, 99))  # add random number between 1 and 99 to list a
a.append(random.randint(1, 99))  # add random number between 1 and 99 to list a
a.append(random.randint(1, 99))  # add random number between 1 and 99 to list a
a.append(random.randint(1, 99))  # add random number between 1 and 99 to list a
a.append(random.randint(1, 99))  # add random number between 1 and 99 to list a
a.append(random.randint(1, 99))  # add random number between 1 and 99 to list a
a.append(random.randint(1, 99))  # add random number between 1 and 99 to list a
a.append(random.randint(1, 99))  # add random number between 1 and 99 to list a
for i in range(10):  # loop through numbers in range 0 to 10 (10 excluded)
    g = int(input("Enter an integer from 1 to 99: "))  # ask user to input an integer and assign it to variable g
    while a[i] != g:  # loop as long as number from list a in position i is not equal to user input
        if g < a[i]:  # if numer given by user is lower than number from list a in position i
            print("guess is low")  # print message
            g = int(input("Enter an integer from 1 to 99: "))  # ask once again for user input and assign it to variable g
        elif g > a[i]:  # if first statemant 'if' would not go through check if user input is greater than number from list a in position i
            print("guess is high")  # print message
            g = int(input("Enter an integer from 1 to 99: "))  # ask once again for user input and assign it to variable g
        else:  # if none of the above statements is true
            break  # break the while loop and go to next number in range 0-9 in 'for' loop
    print("you guessed it!")  # if user input is equal the number from list a in positions i print message
# empty line
b = []  # initiate empty list named b
b.append(random.randint(1, 49))  # add random number between 1 and 49 to list b
b.append(random.randint(1, 49))  # add random number between 1 and 49 to list b
b.append(random.randint(1, 49))  # add random number between 1 and 49 to list b
b.append(random.randint(1, 49))  # add random number between 1 and 49 to list b
b.append(random.randint(1, 49))  # add random number between 1 and 49 to list b
b.append(random.randint(1, 49))  # add random number between 1 and 49 to list b
b.append(random.randint(1, 49))  # add random number between 1 and 49 to list b
b.append(random.randint(1, 49))  # add random number between 1 and 49 to list b
b.append(random.randint(1, 49))  # add random number between 1 and 49 to list b
b.append(random.randint(1, 49))  # add random number between 1 and 49 to list b
for i in range(10):  # loop through numbers in range 0 to 10 (10 excluded)
    g = int(input("Enter an integer from 1 to 49: "))  # ask user to input an integer and assign it to variable g
    while b[i] != g:  # loop as long as number from list b in position i is not equal to user input
        if g < b[i]:  # if numer given by user is lower than number from list b in position i
            print("guess is low")  # print message
            g = int(input("Enter an integer from 1 to 49: "))  # ask once again for user input and assign it to variable g
        elif g > b[i]:  # if first statemant 'if' would not go through check if user input is greater than number from list b in position i
            print("guess is high")  # print message
            g = int(input("Enter an integer from 1 to 49: "))  # ask once again for user input and assign it to variable g
        else:  # if none of the above statements is true
            break  # break the while loop and go to next number in range 0-9 in 'for' loop
    print("you guessed it!")  # if user input is equal the number from list b in positions i print message
