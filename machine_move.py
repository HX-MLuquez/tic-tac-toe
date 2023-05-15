# board = {
#     "1": "1",
#     "2": "2",
#     "3": "3",
#     "4": "4",
#     "5": "5",
#     "6": "6",
#     "7": "7",
#     "8": "8",
#     "9": "9",
#     "prev_move": "",
#     "win_X": False,
#     "win_O": False
# }
# def moveIO():
#     if board["5"] == "5":
#         board["5"] == "O"
#     elif int(board.prev_move) % 2 != 0:
#         if board.prev_move == "5":
#             board["7"] == "O"
#         else:
#             next_move = 10 - int(board.prev_move)
#             board[str(next_move)] == "O"    
#     else:
#         next_move = 10 - int(board.prev_move)
#         board[str(next_move)] == "O" 
#     return

# def moveToWin():
#     if board["1"] == "O" and board["2"] == "O":
#         board["3"] == "O"
#         board.win_O = True
#     elif board["2"] == "O" and board["3"] == "O":
#         board["1"] == "O"
#         board.win_O = True
#     elif board["1"] == "O" and board["3"] == "O":
#         board["2"] == "O"
#         board.win_O = True
#     elif board["7"] == "O" and board["8"] == "O":
#         board["9"] == "O"
#         board.win_O = True
#     elif board["8"] == "O" and board["9"] == "O":
#         board["7"] == "O"
#         board.win_O = True
#     elif board["7"] == "O" and board["9"] == "O":
#         board["8"] == "O"
#         board.win_O = True
#     if board["1"] == "O" and board["4"] == "O":
#         board["7"] == "O"
#         board.win_O = True
#     elif board["4"] == "O" and board["7"] == "O":
#         board["1"] == "O"
#         board.win_O = True
#     elif board["1"] == "O" and board["7"] == "O":
#         board["4"] == "O"
#         board.win_O = True
#     elif board["3"] == "O" and board["6"] == "O":
#         board["9"] == "O"
#         board.win_O = True
#     elif board["6"] == "O" and board["9"] == "O":
#         board["3"] == "O"
#         board.win_O = True
#     elif board["3"] == "O" and board["9"] == "O":
#         board["6"] == "O"
#         board.win_O = True
#     elif board["1"] == "O" and board["5"] == "O":
#         board["9"] == "O"
#         board.win_O = True
#     elif board["5"] == "O" and board["9"] == "O":
#         board["1"] == "O"
#         board.win_O = True
#     elif board["1"] == "O" and board["9"] == "O":
#         board["5"] == "O"
#         board.win_O = True