
import math
import random
random_ints_1to99 = []
random_ints_1to99.append(random.randint(1, 99))
random_ints_1to99.append(random.randint(1, 99))
random_ints_1to99.append(random.randint(1, 99))
random_ints_1to99.append(random.randint(1, 99))
random_ints_1to99.append(random.randint(1, 99))
random_ints_1to99.append(random.randint(1, 99))
random_ints_1to99.append(random.randint(1, 99))
random_ints_1to99.append(random.randint(1, 99))
random_ints_1to99.append(random.randint(1, 99))
random_ints_1to99.append(random.randint(1, 99))
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
random_ints_1to49.append(random.randint(1, 49))
random_ints_1to49.append(random.randint(1, 49))
random_ints_1to49.append(random.randint(1, 49))
random_ints_1to49.append(random.randint(1, 49))
random_ints_1to49.append(random.randint(1, 49))
random_ints_1to49.append(random.randint(1, 49))
random_ints_1to49.append(random.randint(1, 49))
random_ints_1to49.append(random.randint(1, 49))
random_ints_1to49.append(random.randint(1, 49))
random_ints_1to49.append(random.randint(1, 49))
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
