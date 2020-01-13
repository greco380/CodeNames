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
    return link


# def first():
#     hint = str(input("Enter your one-word hint: "))
#     number = int(input("Enter how many cards the hint is for: "))
#     return hint, number


def second(number, linked_dict):
    for i in range(0, number + 1):
        guess = str(input("Enter your guess( None, ?, and enter ends your turn): "))
        if guess in linked_dict:
            # return linked_dict.get(guess)  # need to not return here because I want to stay in the for loop
            get_value = linked_dict.get(guess)
            if get_value == 'Bystander':
                print(get_value)
                return None
            else:
                print(get_value)
        elif guess == "None" or "?" or "":
            return None
        else:
            print("That word is not on the board")
            return None


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
    linked_dict = link_key_with_board()
    print(linked_dict)
    print("\n\n")
    for i in range(1, 15):
        str(input("Enter your one-word hint: "))
        number = int(input("Enter how many cards the hint is for: "))
        print(second(number, linked_dict))


if __name__ == '__main__':
    main()
