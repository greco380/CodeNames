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
    if start == 1:
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




def main():
    arr = speaker_playmat()
    print("\nWho starts:")
    starter = player_who_starts()
    print("\nRandom num grid:")
    random_value(arr, starter)



if __name__ == '__main__':
    main()
