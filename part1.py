import random
from random import randint
# This program is to make a 5 by 5 2D array
# This is going to be the format for my code names game


def speaker_playmat():
    # makes a 5 by 5 grid
    rows, cols = (5, 5)
    # arr = [[0] * cols] * rows
    arr = [[0 for i in range(cols)] for j in range(rows)]

    # changes 1 value
    # arr[0][0] = 1

    # prints the rows and cols in the format that I want
    for row in arr:
        print(row)
    return arr


def player_who_starts():
    start = randint(0, 1)
    if start == 0:
        print("Blue")
    else:
        print("Red")
    return start


def random_value(arr, starter):
    for i in range(0, 5):
        for j in range(0, 5):
            arr[i][j] = randint(1, 10)
    for row in arr:
        print(row)
    return arr


# def random_placement(arr, starter):
#     if starter == 1:
#         for i in range(0, 9):
#             x = randint(0, 4)
#             y = randint(0, 4)
#             arr[x][y] = 3
#         for row in arr:
#             print(row)
#         return arr
#     else:
#         for i in range(0, 8):
#             x = randint(0, 4)
#             y = randint(0, 4)
#             arr[x][y] = 3
#         for row in arr:
#             print(row)
#         return arr


def list_of_possibilities(starter):
    array = list()
    start_max = 9
    second_max = 8
    spy = 1
    bystander = 7
    if starter == 0:
        for i in range(0, start_max):
            array += ["B"]
        for i in range(0, second_max):
            array += ["R"]
        for i in range(0, spy):
            array += ["spy"]
        for i in range(0, bystander):
            array += ["By"]
    else:
        for i in range(0, start_max):
            array += ["R"]
        for i in range(0, second_max):
            array += ["B"]
        for i in range(0, spy):
            array += ["spy"]
        for i in range(0, bystander):
            array += ["By"]
    return array


def make_array(arr, list):
    for i in range(0, 5):
        for j in range(0, 5):
            # element = random.choice(list)
            rint = randint(0, len(list) - 1)
            element = list.pop(rint)
            arr[i][j] = element
            # list = list.remove(element)
    for row in arr:
        print(row)
    return arr



def main():
    arr = speaker_playmat()
    print("\nWho starts:")
    starter = player_who_starts()
    # print("\nRandom num grid:")
    # random_value(arr, starter)
    print("\n---------------")
    list = list_of_possibilities(starter)
    make_array(arr, list)



if __name__ == '__main__':
    main()
