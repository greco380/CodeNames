import key_of_game
import playing_board


def link_key_with_board():
    link = dict()
    key = key_of_game.main()
    board = playing_board.main()
    # print(len(key))
    for i in range(len(key)):
        for j in range(len(key)):
            # dict name[key] = assign
            link[board[i][j]] = key[i][j]
        link[key[i][j]] = board[i][j]
    print(link)



def main():
    print("\n\t\tThe Board looks like:\n")
    arr = playing_board.main()
    for row in arr:
        print(row)
    print("\n\t\t\tThe key is")
    arra = key_of_game.main()
    for row in arra:
        print(row)
    print("\n-------------------")
    print("The dictionary that links the board to the key")
    link_key_with_board()


if __name__ == '__main__':
    main()
