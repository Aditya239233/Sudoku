import pygame
import numpy as np
from BackTrackingAlgo import checking_row,checking_coloumn,checking_box,victory

pygame.init()
w=600
h=700

white=(255,255,255)
black=(0,0,0)
red=(200,0,0)
green=(0,200,0)
bright_red=(255,0,0)
bright_green=(0,255,0)

gameDisplay=pygame.display.set_mode((w,h))
gameDisplay.fill(white)
pygame.display.set_caption("SUDOKU")
clock=pygame.time.Clock()
typing_cursor=pygame.image.load('typing_cursor.png')

def cursor(x,y):
    gameDisplay.blit(typing_cursor,(x,y))

board=np.array([[3, 0, 6, 5, 0, 8, 4, 0, 0],  
                [5, 2, 0, 0, 0, 0, 0, 0, 0],  
                [0, 8, 7, 0, 0, 0, 0, 3, 1],  
                [0, 0, 3, 0, 1, 0, 0, 8, 0],  
                [9, 0, 0, 8, 6, 3, 0, 0, 5],  
                [0, 5, 0, 0, 9, 0, 6, 0, 0],  
                [1, 3, 0, 0, 0, 0, 2, 5, 0],  
                [0, 0, 0, 0, 0, 0, 0, 7, 4],  
                [0, 0, 5, 2, 0, 6, 3, 0, 0]] )

final_board=victory(board)
print(final_board)
board=np.array([[3, 0, 6, 5, 0, 8, 4, 0, 0],  
                [5, 2, 0, 0, 0, 0, 0, 0, 0],  
                [0, 8, 7, 0, 0, 0, 0, 3, 1],  
                [0, 0, 3, 0, 1, 0, 0, 8, 0],  
                [9, 0, 0, 8, 6, 3, 0, 0, 5],  
                [0, 5, 0, 0, 9, 0, 6, 0, 0],  
                [1, 3, 0, 0, 0, 0, 2, 5, 0],  
                [0, 0, 0, 0, 0, 0, 0, 7, 4],  
                [0, 0, 5, 2, 0, 6, 3, 0, 0]] )

def text_objects(text,font):
    TextSurface=font.render(text,True,black)
    return TextSurface,TextSurface.get_rect()

def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText=pygame.font.Font('freesansbold.ttf',115)
        TextSurface,TextRect=text_objects("SUDOKU",largeText)
        TextRect.center=(w/2,h/2)
        gameDisplay.blit(TextSurface,TextRect)
        
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        if 150+100>mouse[0]>150 and 450+50>mouse[1]>450 :    
            pygame.draw.rect(gameDisplay,bright_green,(150,450,100,50))
            if click[0]==1:
                gameDisplay.fill(white)
                main_loop()
        else:
            pygame.draw.rect(gameDisplay,green,(150,450,100,50))
        if 350+100>mouse[0] >350 and 450+50>mouse[1]>450:
            pygame.draw.rect(gameDisplay,bright_red,(350,450,100,50))
            if click[0]==1:
                quit()
        else:
            pygame.draw.rect(gameDisplay,red,(350,450,100,50))
        
        smallText=pygame.font.Font("freesansbold.ttf",20)
        textSurf,textRect=text_objects("GO!",smallText)
        textRect.center=(150+(100/2),450+(50/2))
        gameDisplay.blit(textSurf,textRect)

        textSurf,textRect=text_objects("Exit",smallText)
        textRect.center=(350+(100/2),450+(50/2))
        gameDisplay.blit(textSurf,textRect)

        pygame.display.update()
        clock.tick(15)

l=[0,0]
def main_loop():
    threshold=66.67
    gameExit=False
    num=None
    for row in range(9):
        for coloumn in range(9):
            if board[row][coloumn]!=0:
                pygame.draw.rect(gameDisplay,white,(coloumn*66.67 + 2,row*66.67 +2,64,64))            
                largeText=pygame.font.Font('freesansbold.ttf',30)
                TextSurface,TextRect=text_objects(str(board[row][coloumn]),largeText)
                TextRect.center=((coloumn*66.67+(coloumn+1)*66.67)/2,(row*66.67+(row+1)*66.67)/2)
                gameDisplay.blit(TextSurface,TextRect)

    pygame.draw.line(gameDisplay,red,(66.67,0),(66.67,600),2)
    pygame.draw.line(gameDisplay,red,(133.34,0),(133.34,600),2)
    pygame.draw.line(gameDisplay,red,(266.68,0),(266.68,600),2)
    pygame.draw.line(gameDisplay,red,(333.35,0),(333.35,600),2)
    pygame.draw.line(gameDisplay,red,(466.69,0),(466.69,600),2)
    pygame.draw.line(gameDisplay,red,(533.36,0),(533.36,600),2)
        
    pygame.draw.line(gameDisplay,red,(0,66.67),(600,66.67),2)
    pygame.draw.line(gameDisplay,red,(0,133.34),(600,133.34),2)
    pygame.draw.line(gameDisplay,red,(0,266.68),(600,266.68),2)
    pygame.draw.line(gameDisplay,red,(0,333.35),(600,333.35),2)
    pygame.draw.line(gameDisplay,red,(0,466.69),(600,466.69),2)
    pygame.draw.line(gameDisplay,red,(0,533.36),(600,533.36),2)
    
    pygame.draw.line(gameDisplay,black,(200.1,0),(200.1,600),5)
    pygame.draw.line(gameDisplay,black,(400.02,0),(400.02,600),5)
    pygame.draw.line(gameDisplay,black,(0,200.1),(600,200.1),5)
    pygame.draw.line(gameDisplay,black,(0,400.02),(600,400.02),5)
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()   
        click=pygame.mouse.get_pressed()
        mouse=pygame.mouse.get_pos()
        if click[0]==1 and mouse[1]<600:     
            temp_mouse=mouse
            cursor((mouse[0]//66.6666667 +0.5)*threshold-13,(mouse[1]//66.6666667 +0.5)*threshold-13)
            l[0]=mouse[0]//66.67
            l[1]=mouse[1]//66.67
            while True:
                pygame.display.update()
                row=l[1]
                coloumn=l[0]
                
                for event in pygame.event.get():
                    click=pygame.mouse.get_pressed()
                    mouse=pygame.mouse.get_pos()
                    if click[0]==1 and (mouse[0]//66.67!=l[0] or mouse[1]//66.67!=l[1]):
                        pygame.draw.rect(gameDisplay,white,((temp_mouse[0]//66.6666667)*66.67 + 2,(temp_mouse[1]//66.6666667)*66.67 +2,64,64))
                        main_loop()
                    if event.type==pygame.QUIT:
                        quit()    
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            num = 1
                        elif event.key == pygame.K_2:
                            num = 2
                        elif event.key == pygame.K_3:
                            num = 3
                        elif event.key == pygame.K_4:
                            num = 4
                        elif event.key == pygame.K_5:
                            num = 5
                        elif event.key == pygame.K_6:
                            num = 6
                        elif event.key == pygame.K_7:
                            num = 7
                        elif event.key == pygame.K_8:
                            num = 8
                        elif event.key == pygame.K_9:
                            num = 9
                        elif event.key == pygame.K_DELETE:
                            pygame.draw.rect(gameDisplay,white,((mouse[0]//66.6666667)*66.67 + 2,(mouse[1]//66.6666667)*66.67 +2,64,64))
                            board[int(row)][int(coloumn)]=0
                            break
                        elif event.key == pygame.K_SPACE:
                            victory(board)
                            for row in range(9):
                                for coloumn in range(9):
                                        pygame.draw.rect(gameDisplay,white,(coloumn*66.67 + 2,row*66.67 +2,64,64))            
                                        largeText=pygame.font.Font('freesansbold.ttf',30)
                                        TextSurface,TextRect=text_objects(str(board[row][coloumn]),largeText)
                                        TextRect.center=((coloumn*66.67+(coloumn+1)*66.67)/2,(row*66.67+(row+1)*66.67)/2)
                                        gameDisplay.blit(TextSurface,TextRect)
                            gameExit=False
                            break

                        else:
                            print("Enter a valid key")
                            break
                        if not checking_row(board,int(row),int(num)) and not checking_coloumn(board,int(coloumn),num) and not checking_box(board,int(row)-int(row)%3,int(coloumn)-int(coloumn)%3,num):
                            board[int(row)][int(coloumn)]=num
                            pygame.draw.rect(gameDisplay,white,((mouse[0]//66.6666667)*66.67 + 2,(mouse[1]//66.6666667)*66.67 +2,64,64))
                            TextSurface,TextRect=text_objects(str(num),largeText)
                            TextRect.center=((temp_mouse[0]//66.6666667 +0.5)*66.67,(temp_mouse[1]//66.6666667 +0.5)*66.67)
                            gameDisplay.blit(TextSurface,TextRect)
                            pygame.display.update()
                            if np.array_equal(board,final_board):
                                print("Game Over! Congratulations, You've completed the puzzle") 
                            else:
                                main_loop()
                        else:
                            print("You cannot put that number in that position")
        
        pygame.display.update()
        clock.tick(15)
               
game_intro()