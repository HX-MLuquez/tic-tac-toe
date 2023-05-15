# from machine_move import moveIO, moveToWin
# from finish_game import win
"""
TA-TE-TI  || TRES EN RAYA || TIC-TAC-TOE
Espero que disfruten de este juego.
Es mi primer experiencia usando PYTHON en un algoritmo un poco complejo.
La idea era crear una machine invencible, jujujuu, a la que solo se le puede empatar en el mejor de los casos.

Como ven no he modularizado las funciones debido a que aún no manejo del todo el correcto uso de funciones
exportadas que puedan interactuar con el diccionario "board" de mi archivo principal.

Si aprecian que algo no funciona correctamente, o que se puede optimizar el code me escriben.
A disfrutar!!!!!!!!!
"""

board = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "prev_move": "",
    "win_X": False,
    "win_O": False,
    "max_move": 9
}

def viewBoard():
    print(f"""
    {board["1"]}  {board["2"]}  {board["3"]}
    {board["4"]}  {board["5"]}  {board["6"]}
    {board["7"]}  {board["8"]}  {board["9"]}
    """)

def win():
    if (board["1"] == "X" and board["5"] == "X" and board["9"] == "X") or (board["3"] == "X" and board["5"] == "X" and board["7"] == "X") or (board["1"] == "X" and board["2"] == "X" and board["3"] == "X") or (board["7"] == "X" and board["8"] == "X" and board["9"] == "X") or (board["1"] == "X" and board["4"] == "X" and board["7"] == "X") or (board["3"] == "X" and board["6"] == "X" and board["9"] == "X"):
        viewBoard()
        return 'Win player one ("X")'
    if (board["1"] == "O" and board["5"] == "O" and board["9"] == "O") or (board["3"] == "O" and board["5"] == "O" and board["7"] == "O") or (board["1"] == "O" and board["2"] == "O" and board["3"] == "O") or (board["7"] == "O" and board["8"] == "O" and board["9"] == "O") or (board["1"] == "O" and board["4"] == "O" and board["7"] == "O") or (board["3"] == "O" and board["6"] == "O" and board["9"] == "O"):
        # print(fin winnnnnnnnn')
        viewBoard()
        return """
                   GAME OVER
              Win player two ("O")
              The machine has won
         If you want you can try again
        """
    
def moveIO():
    if board["5"] == "5":
        board["5"] = "O"
    elif int(board["prev_move"]) % 2 != 0:
        if board["prev_move"] == "5":
            board["7"] = "O"
            # print(f'---___---> {board}')
        else:
            next_move = 10 - int(board["prev_move"])
            if board[str(next_move)] == "O":
                if board["prev_move"] == "7" or board["prev_move"] == "1":
                     if board["1"] == "X" and board["7"] == "X" and board["4"] == "4":
                        board["4"] = "O"
                     else:
                        next_move = int(board["prev_move"]) + 2
                        board[str(next_move)] = "O" 
                else:
                    if board["3"] == "X" and board["9"] == "X" and board["6"] == "6":
                        board["6"] = "O"
                    else:
                        next_move = int(board["prev_move"]) - 2
                        board[str(next_move)] = "O"
            else:
                board[str(next_move)] = "O"   
    else:
        if board["5"] == "O":
            if board["prev_move"] == "2": 
                if board["1"] == "X":
                    next_move = 3 
                    board[str(next_move)] = "O"
                else:
                    next_move = 1 
                    board[str(next_move)] = "O"
            if board["prev_move"] == "4": 
                if board["1"] == "X":
                    next_move = 7 
                    board[str(next_move)] = "O"
                else:
                    next_move = 1 
                    board[str(next_move)] = "O"
            if board["prev_move"] == "6": 
                if board["3"] == "X":
                    next_move = 9 
                    board[str(next_move)] = "O"
                else:
                    next_move = 3 
                    board[str(next_move)] = "O"
            if board["prev_move"] == "8": 
                if board["7"] == "X":
                    next_move = 9
                    board[str(next_move)] = "O"
                else:
                    next_move = 7 
                    board[str(next_move)] = "O"
        # falta cubrir el caso de la línea desde 1 2 3 o 2 3 1 o 3 2 1 creo etc, asi como 7 8 9
        else:
            # print(f' game 5 3 4')
            next_move = 10 - int(board["prev_move"])
            board[str(next_move)] = "O" 
    return

def moveToWin():
    if board["1"] == "O" and board["2"] == "O":
        if board["3"] != "X":
            board["3"] = "O"
            board["win_O"] = True
    elif board["2"] == "O" and board["3"] == "O":
        if board["1"] != "X":
            board["1"] = "O"
            board["win_O"] = True
    elif board["1"] == "O" and board["3"] == "O":
        if board["2"] != "X":
            board["2"] = "O"
            board["win_O"] = True
    elif board["7"] == "O" and board["8"] == "O":
        if board["9"] != "X":
            board["9"] = "O"
            board["win_O"] = True
    elif board["8"] == "O" and board["9"] == "O":
        if board["7"] != "X":
            board["7"] = "O"
            board["win_O"] = True
    elif board["7"] == "O" and board["9"] == "O":
        if board["8"] != "X":
            board["8"] = "O"
            board["win_O"] = True
    if board["1"] == "O" and board["4"] == "O":
        if board["7"] != "X":
            board["7"] = "O"
            board["win_O"] = True
    elif board["4"] == "O" and board["7"] == "O":
        if board["1"] != "X":
            board["1"] = "O"
            board["win_O"] = True
    elif board["1"] == "O" and board["7"] == "O":
        if board["4"] != "X":
            board["4"] = "O"
            board["win_O"] = True
    elif board["3"] == "O" and board["6"] == "O":
        if board["9"] != "X":
            board["9"] = "O"
            board["win_O"] = True
    elif board["6"] == "O" and board["9"] == "O":
        if board["3"] != "X":
            board["3"] = "O"
            board["win_O"] = True
    elif board["3"] == "O" and board["9"] == "O":
        if board["6"] != "X":
            board["6"] = "O"
            board["win_O"] = True
    elif board["1"] == "O" and board["5"] == "O":
        if board["9"] != "X":
            board["9"] = "O"
            board["win_O"] = True
    elif board["5"] == "O" and board["9"] == "O":
        if board["1"] != "X":
            board["1"] = "O"
            board["win_O"] = True
    elif board["1"] == "O" and board["9"] == "O":
        if board["5"] != "X":
            board["5"] = "O"
            board["win_O"] = True
    elif board["3"] == "O" and board["5"] == "O":
        if board["7"] != "X":
            board["7"] = "O"
            board["win_O"] = True
    elif board["5"] == "O" and board["7"] == "O":
        if board["3"] != "X":
            board["3"] = "O"
            board["win_O"] = True
    elif board["3"] == "O" and board["7"] == "O":
        if board["5"] != "X":
            board["5"] = "O"
            board["win_O"] = True
    elif board["5"] == "O" and board["6"] == "O":
        if board["4"] != "X":
            board["4"] = "O"
            board["win_O"] = True
    elif board["4"] == "O" and board["6"] == "O":
        if board["5"] != "X":
            board["5"] = "O"
            board["win_O"] = True
    elif board["4"] == "O" and board["5"] == "O":
        if board["6"] != "X":
            board["6"] = "O"
            board["win_O"] = True



initGame = print(f"""
Welcome to this wonderful game ta te ti. 
I challenge you to try to beat me
""")


def move():
    print(f'Player "X" Select your place NUMBER: ')
    motion = input()
    board["prev_move"] = motion
    # print(f'----> {board}')
    if board[motion] == "X" or board[motion] == "O":
        print(f'ERROR: wrong move')
        return False
    else:
        board[motion] = "X"
        return True

def game():
    while not board["win_O"] and not board["win_X"] and board["max_move"]>0 :
        viewBoard()
        moveTrue = move()
        if moveTrue:
            moveToWin()
            if board["win_O"]:
                result = win()
                print(f'{result}')
                return result
            else:
                moveIO()
            board["max_move"] = board["max_move"] - 2
    print(f"""
            GAME OVER
           We have tied 
    If you want you can try again
    """)
    return "finish"

game()

# move()
# viewBoard()
# move()
# viewBoard()
# move()
# viewBoard()
# move()
# viewBoard()