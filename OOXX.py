import os

def printBoard(Board):
    print(Board["top-L"]+"|"+Board["top-M"]+"|"+Board["top-R"])
    print("-+-+-")
    print(Board["mid-L"]+"|"+Board["mid-M"]+"|"+Board["mid-R"])
    print("-+-+-")
    print(Board["bot-L"]+"|"+Board["bot-M"]+"|"+Board["bot-R"])

def checkBoard_ASCII(Board, move, turn):
    if Board[move]==" ":
        Board[move] = turn
        return True
    else: 
        return False

def checkBoard_Num(Board, theBoardNum, move, turn):
    if Board[theBoardNum[int(move)]]==" ":
        Board[theBoardNum[int(move)]] = turn
        return True
    else: 
        return False

def checkWinner(Board, pos):
    i = 0
    for _, value in Board.items():
        pos[i] = value
        i+=1

    if pos[0]==pos[1] and pos[1]==pos[2] and not pos[0]=" ": 
        print(f"{pos[0]} is winner")
        return False
    elif pos[3]==pos[4] and pos[4]==pos[5]  not pos[3]=" ": 
        print(f"{pos[3]} is winner")
        return False
    elif pos[6]==pos[7] and pos[7]==pos[8]  not pos[6]=" ": 
        print(f"{pos[6]} is winner")
        return False
    elif pos[0]==pos[3] and pos[3]==pos[6]  not pos[0]=" ": 
        print(f"{pos[0]} is winner")
        return False
    elif pos[1]==pos[4] and pos[4]==pos[7]  not pos[1]=" ": 
        print(f"{pos[1]} is winner")
        return False
    elif pos[2]==pos[5] and pos[5]==pos[8]  not pos[2]=" ": 
        print(f"{pos[2]} is winner")
        return False
    elif pos[0]==pos[4] and pos[4]==pos[8]  not pos[0]=" ": 
        print(f"{pos[1]} is winner")
        return False
    elif pos[2]==pos[4] and pos[4]==pos[6]  not pos[2]=" ": 
        print(f"{pos[2]} is winner")
        return False
    else: return True

if __name__ == "__main__":
    theBoard = {"top-L": " ", "top-M": " ", "top-R": " ", 
                "mid-L": " ", "mid-M": " ", "mid-R": " ",
                "bot-L": " ", "bot-M": " ", "bot-R": " "}
    theBoardNum = ["top-L", "top-M", "top-R", "mid-L", "mid-M",
                     "mid-R","bot-L", "bot-M", "bot-R"]
    # pos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = "X"
    pos = [" " for i in range(10)]
    # print(pos)

    for i in range(9):
        printBoard(theBoard)
        move = input(f"Turn for {turn}. Move on which sapce?")
        if move in theBoard or (int(move)>=0 and int(move)<=9):
            if move.isnumeric():
                if not checkBoard_Num(theBoard, theBoardNum, move, turn): 
                    print("位置已經填過了，請重新輸入")
                    continue
            else:
                if not checkBoard_ASCII(theBoard, move, turn): 
                    print("位置已經填過了，請重新輸入")
                    continue

            stop = checkWinner(theBoard, pos)
            if not stop : break;
            if turn == "O": turn = "X" 
            else : turn = "O"
        else :
            print("位置輸入錯誤，請重新輸入")
            continue

        
        
    