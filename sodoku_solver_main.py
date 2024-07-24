from colorama import Fore, Back, Style
import random
import time
def check(main_sudoku, m, x, y):
    list_tekrari = []
    
    # Check the row
    for j in range(9):
        if main_sudoku[x][j] == m and j != y and m != 0:
            list_tekrari.append([x, j])
    
    # Check the column
    for i in range(9):
        if main_sudoku[i][y] == m and i != x and  m != 0  :
            list_tekrari.append([i, y])
    
    # Check the 3x3 block
    start_row = (x // 3) * 3
    start_col = (y // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if main_sudoku[i][j] == m and (i != x or j != y) and m != 0:
                list_tekrari.append([i, j])
    
    # Add the current position
    list_tekrari.append([x, y])
    
    return list_tekrari

def clear_board(main_sudoku: list, x : int, y : int):
    main_sudoku[x][y] = 0

def win_check(main_soduko : list) -> bool :
    for i in range(9):
        for j in range(9):
            if main_soduko[i][j] == 0:
                return False
    for i in range(9):
        for j in range(9):
            if(len(check(main_soduko, main_soduko[i][j], i, j)) > 1 ):
                return False
    return True
def initails_list_maker(main_soduku: list) -> list:
    initials_list = []
    for i in range(9):
        for j in range(9):
            if main_soduku[i][j] != 0 :
                initials_list.append([i, j])
    return initials_list

def print_main_soduku(main_soduku : list, initials_list : list) :
    for i in range(9):
        for j in range(9):
            if j % 3 != 2:
                list_tekrari = check(main_soduku, main_soduku[i][j], i, j)
                if len(list_tekrari) >= 2 :
                    print(f"{Fore.RED}{main_soduku[i][j]}{Style.RESET_ALL}|",end='')
                elif [i, j] in initials_list :
                    print(f"{main_soduku[i][j]}|", end ='')
                elif main_soduku[i][j] != 0:
                    print(f"{Fore.YELLOW}{main_soduku[i][j]}{Style.RESET_ALL}|",end = '')
                else :
                    print(f"{main_soduku[i][j]}|", end = '')
            elif j % 3 == 2:
                list_tekrari = check(main_soduku, main_soduku[i][j], i, j)
                if len(list_tekrari) >= 2 :
                    print(f"{Fore.RED}{main_soduku[i][j]}{Style.RESET_ALL} |*| ",end='')
                elif [i, j] in initials_list :
                    print(f"{main_soduku[i][j]} |*| ", end ='')
                elif main_soduku[i][j] != 0:
                    print(f"{Fore.YELLOW}{main_soduku[i][j]}{Style.RESET_ALL} |*| ",end = '')
                else :
                    print(f"{main_soduku[i][j]} |*| ", end = '')
            if j == 8 :
                print()
        if i % 3 == 2 :
            print('=' * 29)
def find_empty(main_soduku : list):
    for i in range(9):
        for j in range(9):
            if main_soduku[i][j] == 0:
                return i, j
    return -1, -1

def soduku_csp(main_soduku : list, back_track_csp : list, bool_check : bool, initials_list : list):
    if bool_check :
        x, y = find_empty(main_soduku)
        if x == -1:
            print_main_soduku(main_soduku, initials_list)
            exit()
        flag = 0
        for i in range(1, 10):
            list_tekrari = check(main_soduku, i, x, y)
            if len(list_tekrari) < 2 :
                back_track_csp.append([x, y, i])
                main_soduku[x][y] = i
                flag = 1
                return main_soduku, back_track_csp, True, initials_list
        if flag == 0 :
            return main_soduku, back_track_csp, False, initials_list
    else :
        if back_track_csp == []:
            print('invalid')
            exit()
        cell = back_track_csp.pop()
        x = cell[0]
        y = cell[1]
        clear_board(main_soduku, x, y)
        flag = 0
        for i in range(cell[2] + 1 , 10):
            list_tekrari = check(main_soduku, i, x, y)
            if len(list_tekrari) < 2 :
                back_track_csp.append([x, y, i])
                main_soduku[x][y] = i
                flag = 1
                return main_soduku, back_track_csp, True, initials_list
        if flag == 0:
            return main_soduku, back_track_csp, False, initials_list
def soduku_input():
    print("enter values of each line 0 means empty")
    main_soduku = []
    for i in range(9):
        print(main_soduku)
        while True:
            this_line = list(map(int,input().split()))
            flag = 0
            if len(this_line) != 9:
                print('not enough numbers or too many numbers try again')
                flag = 1
            if flag == 0 :
                for value in this_line :
                    if value < 0 or value > 9:
                        flag = 2
            if flag == 2:
                print('some inputs are out of range try again')
            if flag == 0:
                break
        main_soduku.append(this_line)
    return main_soduku
def soduku_genarator():
    main_soduku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    back_track_csp = []
    bool_check = True
    initials_list = []
    while not win_check(main_soduku):
        main_soduku, back_track_csp, bool_check, initials_list = soduku_csp(main_soduku, back_track_csp, bool_check , initials_list)
    for i in range(9):
        for j in range(9):
            rate = random.random()
            if rate > 0.7 :
                main_soduku[i][j] = 0
    return main_soduku




    






                    


    


sudoku_puzzle_1 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    # Sudoku Puzzle 2
sudoku_puzzle_2 = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]

    # Sudoku Puzzle 3
sudoku_puzzle_3 = [
        [0, 0, 5, 3, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 7, 0, 0, 1, 0, 5, 0, 0],
        [4, 0, 0, 0, 0, 5, 3, 0, 0],
        [0, 1, 0, 0, 7, 0, 0, 0, 6],
        [0, 0, 3, 2, 0, 0, 0, 8, 0],
        [0, 6, 0, 5, 0, 0, 0, 0, 9],
        [0, 0, 4, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 9, 7, 0, 0]
    ]

    # Sudoku Puzzle 4
sudoku_puzzle_4 = [
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
        [7, 0, 0, 0, 0, 3, 6, 0, 0],
        [0, 0, 0, 0, 9, 1, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 1, 8, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 6, 0, 4, 5],
        [0, 4, 0, 2, 0, 0, 0, 6, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0, 0]
    ]

    # Sudoku Puzzle 5
sudoku_puzzle_5 = [
        [0, 0, 0, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 3, 5, 0, 0, 0],
        [0, 0, 0, 7, 0, 1, 0, 0, 0],
        [0, 3, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 7, 0],
        [0, 0, 0, 1, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [9, 1, 0, 0, 0, 0, 0, 0, 0]
    ]
sudoku_puzzle6 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]


list_sodoku=[sudoku_puzzle_1,sudoku_puzzle_2,sudoku_puzzle_3,sudoku_puzzle_4,sudoku_puzzle_5,sudoku_puzzle6]
n = random.randint(0,5)


user_input = input("Sudoku generator|Input Sudoku|Pre-made Sudoku")
enter = ["Sudoku generator","Input Sudoku","Pre-made Sudoku"]

while user_input not in enter:
    print("wrong answer")
    user_input = input("Sudoku generator|Input Sudoku|Pre-made Sudoku ")
if user_input == 'Pre-made Sudoku':
    main_soduku = list_sodoku[n]
if user_input == 'Input Sudoku':
    main_soduku = soduku_input()
if user_input == 'Sudoku generator':
    main_soduku = soduku_genarator()

start = time.time()
back_track_csp = []
bool_check = True
initials_list = initails_list_maker(main_soduku)
while not win_check(main_soduku):
    main_soduku, back_track_csp, bool_check, initials_list = soduku_csp(main_soduku, back_track_csp, bool_check , initials_list)
for i in range(9):
    for j in range(9):
        list_tekrari = check(main_soduku, main_soduku[i][j], i, j)
        if len(list_tekrari)>= 2:
            print('invalid')
            break
else:         
    end = time.time()
    print_main_soduku(main_soduku, initials_list)
    print(f'elapsed time{end - start}')
