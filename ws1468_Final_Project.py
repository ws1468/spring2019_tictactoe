# Wendy Shi
# CS-UY 1114
# 9 May 2019
# Final Project

import turtle
import time
import random

turtle.title("Tic Tac Toe")

the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

def turtle_moves(): #drawing the lines of the board
    turtle.pd()
    turtle.fd(400)
    turtle.pu()
    
def draw_circle():  #drawing the circle
    turtle.pd()
    turtle.circle(40)
    turtle.pu()
    
def draw_x_1():     #drawing the /
    turtle.pd()
    turtle.left(45)
    turtle.forward(80)
    turtle.pu()
    
def draw_x_2():     #drawing the \
    turtle.pd()
    turtle.left(90)
    turtle.forward(80)
    turtle.pu()
    turtle.home()
    
def draw_board(board): #drawing board
    turtle.clear()
    turtle.pu()
    turtle.goto(-200,70)
    turtle_moves()
    turtle.goto(-200,-70)
    turtle_moves()
    turtle.goto(-75,200)
    turtle.right(90)
    turtle_moves()
    turtle.goto(75,200)
    turtle_moves()
    turtle.home()
    
    for i in range(len(board)): # drawing O or X
        if board[i] == "O":
            if i % 3 == 0:
                x = -135
            elif i % 3 == 1:
                x = 0
            else:
                x = 135
            if i in range(3):
                y = 90
                turtle.goto(x,y)
                draw_circle()   
            if i in range(3,6):
                y = -40
                turtle.goto(x,y)
                draw_circle()
            if i in range(6,9):
                y = -180
                turtle.goto(x,y)
                draw_circle()
        if board[i] == "X":
            if i % 3 == 0:
                x = -160
            elif i % 3 == 1:
                x = -30
            else:
                x = 110    
            if i in range(3):
                y = 100
                turtle.goto(x,y)
                draw_x_1()
                turtle.goto(x+60,y)
                draw_x_2()
            if i in range(3,6):
                y = -30
                turtle.goto(x,y)
                draw_x_1()
                turtle.goto(x+60,y)
                draw_x_2()
            if i in range(6,9):
                y = -170
                turtle.goto(x,y)
                draw_x_1()
                turtle.goto(x+60,y)
                draw_x_2()   
    turtle.update()
    
def do_user_move(board, x, y):
    print("user clicked at "+str(x)+","+str(y))
    #the ranges of each sqaure on the grid
    board_place = {"0": -200 < x < -75 and 200 > y > 70,
                   "1": -75 < x < 75 and 200 > y > 70,
                   "2":75 < x < 200 and 200 > y > 70,
                   "3": -200 < x < -75 and 70 > y > -70,
                   "4": -75 < x < 75 and 70 > y > -70,
                   "5": 75 < x < 200 and 70 > y > -70,
                   "6": -200 < x < -75 and -70 > y > -200,
                   "7": -75 < x < 75 and -70 > y > -200,
                   "8": 75 < x < 200 and -70 > y > -200}
    valid_move = False

    for key, val in board_place.items():
        if val:
            if board[int(key)] == "_":
                valid_move = True
                board[int(key)] = "O"

    print(the_board)
    return valid_move

def check_game_over(board):
    #Game over when:
    #Horizontal: 012, 345, 678
    #Vertical: 036, 147, 258
    #Diagonal: 048, 246
    endgame = False
    stalemate = False
    computer_win = False
    user_win = False
    
    for i in range(len(board)):
        if((board[0] == "O" and board[0] == board[1] == board[2]) or
            (board[3] == "O" and board[3] == board[4] == board[5]) or
            (board[6] == "O" and board[6] == board[7] == board[8]) or
            (board[0] == "O" and board[0] == board[3] == board[6]) or
            (board[1] == "O" and board[1] == board[4] == board[7]) or
            (board[2] == "O" and board[2] == board[5] == board[8]) or
            (board[0] == "O" and board[0] == board[4] == board[8]) or
            (board[2] == "O" and board[2] == board[4] == board[6])):
                user_win = True
        elif((board[0] == "X" and board[0] == board[1] == board[2]) or
            (board[3] == "X" and board[3] == board[4] == board[5]) or
            (board[6] == "X" and board[6] == board[7] == board[8]) or
            (board[0] == "X" and board[0] == board[3] == board[6]) or
            (board[1] == "X" and board[1] == board[4] == board[7]) or
            (board[2] == "X" and board[2] == board[5] == board[8]) or
            (board[0] == "X" and board[0] == board[4] == board[8]) or
            (board[2] == "X" and board[2] == board[4] == board[6])):
                computer_win = True
        else:         
            count = 0
            for i in range(len(board)):
                if board[i] != "_":
                    count += 1
                    if count == 9:
                        stalemate = True
    #game over message
    if stalemate == True:
        endgame = True
        turtle.write("Game over! No Winner!", \
                     font = ("Arial", 20, 'bold'))
    elif computer_win == True:
        endgame = True
        turtle.write("Game Over! You Lose!", \
                     font = ("Arial", 20, 'bold'))
    elif user_win == True:
        endgame = True
        turtle.write("Game Over! You WIN!", \
                     font = ("Arial", 20, 'bold'))
    if endgame:
        turtle.clear()
        time.sleep(3)
        for i in range(len(board)):
            board[i] = "_"
        draw_board(board)

    return endgame

def check_temp_board(board):  
    endgame = False
    computer_win = False
    user_win = False
    for i in range(len(board)):
        if((board[0] == "O" and board[0] == board[1] == board[2]) or
            (board[3] == "O" and board[3] == board[4] == board[5]) or
            (board[6] == "O" and board[6] == board[7] == board[8]) or
            (board[0] == "O" and board[0] == board[3] == board[6]) or
            (board[1] == "O" and board[1] == board[4] == board[7]) or
            (board[2] == "O" and board[2] == board[5] == board[8]) or
            (board[0] == "O" and board[0] == board[4] == board[8]) or
            (board[2] == "O" and board[2] == board[4] == board[6])):
                user_win = True
            
        if((board[0] == "X" and board[0] == board[1] == board[2]) or
            (board[3] == "X" and board[3] == board[4] == board[5]) or
            (board[6] == "X" and board[6] == board[7] == board[8]) or
            (board[0] == "X" and board[0] == board[3] == board[6]) or
            (board[1] == "X" and board[1] == board[4] == board[7]) or
            (board[2] == "X" and board[2] == board[5] == board[8]) or
            (board[0] == "X" and board[0] == board[4] == board[8]) or
            (board[2] == "X" and board[2] == board[4] == board[6])):
                computer_win = True
    if user_win or computer_win == True:
        endgame = True
    return endgame
                
def do_computer_move(board):
    valid_move = False
    temp_board = board.copy()

    #checks for computer's winning move
    i = 0
    while valid_move == False and i < len(board):
        if temp_board[i] == "_":
            temp_board[i] = "X"
            if check_temp_board(temp_board) == True:
                print("compupter's winning move")
                valid_move = True
                board[i] = "X"
            else:
                temp_board[i] = "_"
        i += 1
        
    #blocks user's winning move
    i = 0
    while valid_move == False and i < len(board):
        if temp_board[i] == "_":
            temp_board[i] = "O"
            if check_temp_board(temp_board) == True:
                print("block user's winning move")
                valid_move = True
                board[i] = "X"
            else:
                temp_board[i] = "_"
        i += 1
        
    #random move
    while valid_move == False:
        board_spaces = [0,1,2,3,4,5,6,7,8]
        comp_choice = random.choice(board_spaces)
        if board[comp_choice] == "_":
            print("random move")
            valid_move = True
            board[comp_choice] = "X"
    
def clickhandler(x, y):
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)
def main():
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()
main()
