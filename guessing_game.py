import random


def generate_numbers(start, end, list_name):
    for i in range(10):
        list_name.append(random.randint(start, end))


def check_user_input(user_number, list_of_numbers, i, range_end):
    while list_of_numbers[i] != user_number:
        if user_number < list_of_numbers[i]:
            print("guess is low")
            user_number = int(
                input("Enter an integer from 1 to " + str(range_end) + ": ")
            )
        elif user_number > list_of_numbers[i]:
            print("guess is high")
            user_number = int(
                input("Enter an integer from 1 to " + str(range_end) + ": ")
            )
        else:
            break
    print("you guessed it!")


def guess_10_numbers(list_of_numbers, range_end):
    for i in range(10):
        user_number = int(
            input("Enter an integer from 1 to " + str(range_end) + ": ")
        )
        check_user_input(user_number, list_of_numbers, i, range_end)


random_ints_1to99 = []
generate_numbers(start=1, end=99, list_name=random_ints_1to99)
guess_10_numbers(random_ints_1to99, range_end=99)

random_ints_1to49 = []
generate_numbers(start=1, end=49, list_name=random_ints_1to49)
guess_10_numbers(random_ints_1to49, range_end=49)
