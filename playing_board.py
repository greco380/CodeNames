import random


def playmat():
    # makes a 5 by 5 grid
    rows, cols = (5, 5)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    return arr


def make_board(arr, words):
    for i in range(0, 5):
        for j in range(0, 5):
            rint = random.randint(0, len(words) - 1)
            element = words.pop(rint)
            # element = random.choice(words)
            arr[i][j] = element
    # for row in arr:
    #     print(row)  # Error printing happening here when trying to display the dictionary
    return arr


def main():
    words = list()
    file = "words.txt"
    file = open(file)
    for line in file:
        line = line.strip()
        words.append(line)
    arr = playmat()
    array_board = make_board(arr, words)
    return array_board


if __name__ == '__main__':
    main()

