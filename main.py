def checkWin(x, o):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for indices in wins:
        if x[indices[0]] + x[indices[1]] + x[indices[2]] == 3:
            print("X WINS THE MATCH!")
            return 1
        if o[indices[0]] + o[indices[1]] + o[indices[2]] == 3:
            print("O WINS THE MATCH!")
            return 1
    return 0


def checkInput(xState, oState, index):
    if (index > 8 or index < 0) or (xState[index] or oState[index]):
        print('INVALID INPUT!!!\n')
        return 1
    return 0


def enter(xState, oState, turn):
    if turn:
        print("\nX's turn: Enter an index value: ")
        index = int(input())-1
        while checkInput(xState, oState, index):
            index = int(input("Enter an index value:\n"))-1
        xState[index] = 1
    else:
        print("\nO's turn: Enter an index value: ")
        index = int(input())-1
        while checkInput(xState, oState, index):
            index = int(input("Enter an index value:\n"))-1
        oState[index] = 1


def display(xState, oState):
    for i in range(1, 10):
        if i % 3 == 0:
            print('x' if xState[i-1] else ('o' if oState[i-1] else i))
            if i != 9:
                print("--|---|---")
        else:
            print('x' if xState[i-1]
                  else ('o' if oState[i-1] else i), end=' | ')


if __name__ == "__main__":
    print("      Welcome to TIC TAC TOE multiplayer  ")
    xState = [0 for i in range(9)]
    oState = [0 for i in range(9)]
    turn = 1        # 1 for x and 0 for o
    while True:
        display(xState, oState)
        enter(xState, oState, turn)
        turn = not(turn)
        if checkWin(xState, oState):
            display(xState, oState)
            break
    print("\nGAME OVER")
