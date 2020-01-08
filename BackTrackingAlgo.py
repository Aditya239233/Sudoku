import numpy as np 

board=np.array([[3, 0, 6, 5, 0, 8, 4, 0, 0],  
                [5, 2, 0, 0, 0, 0, 0, 0, 0],  
                [0, 8, 7, 0, 0, 0, 0, 3, 1],  
                [0, 0, 3, 0, 1, 0, 0, 8, 0],  
                [9, 0, 0, 8, 6, 3, 0, 0, 5],  
                [0, 5, 0, 0, 9, 0, 6, 0, 0],  
                [1, 3, 0, 0, 0, 0, 2, 5, 0],  
                [0, 0, 0, 0, 0, 0, 0, 7, 4],  
                [0, 0, 5, 2, 0, 6, 3, 0, 0]] )
        
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def check_move(board,list):
    for row in range(9):
        for coloumn in range(9):
            if (board[row][coloumn])==0:
                list[0]=row
                list[1]=coloumn
                return True

    return False
    
def checking_row(board,row,num):
    for x in range(9):
        if board[row][x]==num:
            return True
    return False

def checking_coloumn(board,coloumn,num):
    for x in range(9):
        if board[x][coloumn]==num:
            return True
    return False

def checking_box(board,row,coloumn,num):
    for x in range(3):
        for y in range(3):
            if board[x+row][y+coloumn]==num:
                return True
    return False

def victory(board):
    l=[0,0]

    if not check_move(board,l):
        return True
    
    row=l[0]
    coloumn=l[1]

    for num in range(1,10):
        
        if not checking_row(board,row,num) and not checking_coloumn(board,coloumn,num) and not checking_box(board,row-row%3,coloumn-coloumn%3,num):

            board[row][coloumn]=num
            if victory(board):
                return True

            board[row][coloumn]=0
    return False


if __name__=="__main__":
    if victory(board):
        print(board)
    else:
        print("no solution")


'''
gameDisplay.fill(white)
        pygame.draw.line(gameDisplay,red,(66.67,0),(66.67,600),2)
        pygame.draw.line(gameDisplay,red,(133.34,0),(133.34,600),2)
        pygame.draw.line(gameDisplay,black,(200.1,0),(200.1,600),5)
        pygame.draw.line(gameDisplay,red,(266.68,0),(266.68,600),2)
        pygame.draw.line(gameDisplay,red,(333.35,0),(333.35,600),2)
        pygame.draw.line(gameDisplay,black,(400.02,0),(400.02,600),5)
        pygame.draw.line(gameDisplay,red,(466.69,0),(466.69,600),2)
        pygame.draw.line(gameDisplay,red,(533.36,0),(533.36,600),2)
        
        pygame.draw.line(gameDisplay,red,(0,66.67),(600,66.67),2)
        pygame.draw.line(gameDisplay,red,(0,133.34),(600,133.34),2)
        pygame.draw.line(gameDisplay,black,(0,200.1),(600,200.1),5)
        pygame.draw.line(gameDisplay,red,(0,266.68),(600,266.68),2)
        pygame.draw.line(gameDisplay,red,(0,333.35),(600,333.35),2)
        pygame.draw.line(gameDisplay,black,(0,400.02),(600,400.02),5)
        pygame.draw.line(gameDisplay,red,(0,466.69),(600,466.69),2)
        pygame.draw.line(gameDisplay,red,(0,533.36),(600,533.36),2)
        '''