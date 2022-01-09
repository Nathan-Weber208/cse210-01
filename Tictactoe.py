def main():
    board = 1,2,3,4,5,6,7,8,9
    playersturn = "O"
    while win(board) == False:
        showboard(board)
        playersturn = turnstep(playersturn)
        selection = int(turnselect(playersturn))
        board[selection-1] = playersturn
        


def changeboard(board,playersturn,selection):
    board[selection-1] = playersturn
    return board
    
def turnselect(playersturn):
    choice = "N/A"
    while choice != "1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9":
        choice = input(f'Player {playersturn} which position will you place your {playersturn}? ')
        if choice == "1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9":
            return choice
        else: print("Must be a number 1-9")
    

def turnstep(playersturn):
    if playersturn == "X":
        return "O"
    else:
        return "X"

def win(board):
    if board[0] == board[1] == board[2]:
        return True,board[1]
    elif board[3] == board[4] == board[5]:
        return True,board[4]
    elif board[6] == board[7] == board[8]:
        return True,board[7]
    elif board[0] == board[3] == board[6]:
        return True,board[3]
    elif board[1] == board[4] == board[7]:
        return True,board[4]
    elif board[0] == board[4] == board[8]:
        return True,board[4]
    elif board[2] == board[4] == board[6]:
        return True,board[4]
    else:
        return False


def showboard(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()



if __name__ == "__main__":
    main()