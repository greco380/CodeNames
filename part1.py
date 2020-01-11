# This program is to make a 5 by 5 2D array
# This is going to be the format for my code names game


def playmat():
    # makes a 5 by 5 grid
    rows, cols = (5, 5)
    # arr = [[0] * cols] * rows
    arr = [[0 for i in range(cols)] for j in range(rows)]

    # changes 1 value
    arr[0][0] = 1

    # prints the rows and cols in the format that I want
    for row in arr:
        print(row)


def main():
    playmat()


if __name__ == '__main__':
    main()
