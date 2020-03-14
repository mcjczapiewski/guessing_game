import random


def generate_numbers(start, end, list_name):
    for i in range(10):
        list_name.append(random.randint(start, end))


def check_user_input(user_number, list_of_numbers, i):
    while list_of_numbers[i] != user_number:
        if user_number < list_of_numbers[i]:
            print("guess is low")
            user_number = int(input("Enter an integer from 1 to 99: "))
        elif user_number > list_of_numbers[i]:
            print("guess is high")
            user_number = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("you guessed it!")


def guess_10_numbers(list_of_numbers, range_end):
    for i in range(10):
        user_number = int(
            input("Enter an integer from 1 to " + str(range_end) + ": ")
        )
        check_user_input(user_number, list_of_numbers, i)


random_ints_1to99 = []
generate_numbers(1, 99, random_ints_1to99)
guess_10_numbers(random_ints_1to99, 99)

random_ints_1to49 = []
generate_numbers(1, 49, random_ints_1to49)
guess_10_numbers(random_ints_1to49, 49)
