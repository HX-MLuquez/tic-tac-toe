# boardView = {
#     "1": "1",
#     "2": "2",
#     "3": "3",
#     "4": "4",
#     "5": "5",
#     "6": "6",
#     "7": "7",
#     "8": "8",
#     "9": "9",
# }
# """
# Valores
#     1  2  3
#     2  3  1
#     3  1  2

# La suma de todas sus filas y columnas nos da 6 (seis)
#      a  b  c
#   x  1  2  3  
#   y  2  3  1  
#   z  3  1  2  
# """
# board = {
#     "a": {"1": "","2": "","3": ""},
#     "b": {"2": "","3": "","1": ""},
#     "c": {"3": "","1": "","2": ""},
#     "x": {"1": "","2": "","3": ""},
#     "y": {"2": "","3": "","1": ""},
#     "z": {"3": "","1": "","2": ""},
#     "prev_move": "",
#     "win_X": False,
#     "win_O": False,
#     "max_move": 9
# }
# def viewBoard():
#     print(f"""
#     {boardView["1"]}  {boardView["2"]}  {boardView["3"]}
#     {boardView["4"]}  {boardView["5"]}  {boardView["6"]}
#     {boardView["7"]}  {boardView["8"]}  {boardView["9"]}
#     """)

# def win():
#     for key, value in board.items():
#         if len(set(value.values())) == 1:
#             if list(value.values())[0] == "O":
#                 board["win_O"] = True
#             if list(value.values())[0] == "X":
#                 board["win_X"] = True
#             return f'Ganan la {list(value.values())[0]}'
#     return 