import random


def generate_numbers(start, end, list_name):
    for i in range(10):
        list_name.append(random.randint(start, end))


random_ints_1to99 = []
generate_numbers(1, 99, random_ints_1to99)
for i in range(10):
    user_number = int(input("Enter an integer from 1 to 99: "))
    while random_ints_1to99[i] != user_number:
        if user_number < random_ints_1to99[i]:
            print("guess is low")
            user_number = int(input("Enter an integer from 1 to 99: "))
        elif user_number > random_ints_1to99[i]:
            print("guess is high")
            user_number = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("you guessed it!")

random_ints_1to49 = []
generate_numbers(1, 49, random_ints_1to49)
for i in range(10):
    user_number = int(input("Enter an integer from 1 to 49: "))
    while random_ints_1to49[i] != user_number:
        if user_number < random_ints_1to49[i]:
            print("guess is low")
            user_number = int(input("Enter an integer from 1 to 49: "))
        elif user_number > random_ints_1to49[i]:
            print("guess is high")
            user_number = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")
