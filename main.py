import pygame   #for drawing the board
import random

def getInput():
    boardData = []
    print("Enter the data :\n")
    boardData.append(list(input()))
    size = len(boardData[0])
    for i in range(size-1):
        boardData.append(list(input()))
    return boardData
def solve(boardData, solution, base):

    size = len(boardData)
    for i in range(len(boardData)):
        for j in range(len(boardData)):
            if solution[i][j] != 0:
                if solution[i][j] >= base:
                    base = solution[i][j] + 1
    word = input('Enter the word to find :')
    if word != '':
        for i in range(len(boardData)):
            for j in range(len(boardData)):
                wordl = list(word)
                if wordl[0] == boardData[i][j]:
                    trav = 1
                elif wordl[-1] == boardData[i][j]:
                    trav = -1
                else:
                    trav = 0
                if trav != 0:
                    if trav == -1:
                        wordl.reverse()
                    wordLength = len(wordl)
                    flag = 1
                    for q in range(wordLength):# sove R
                        if j + q > size - 1:
                            flag = -1
                            break
                        if boardData[i][j+q] != wordl[q]:
                            flag = -1
                            break
                    if flag == 1:
                        #toSolve.remove(word)
                        for q in range(wordLength):
                            solution[i][j+q] = base
                    else:
                        flag = 1    #sove D
                        for q in range(wordLength):
                            if i + q > size - 1:
                                flag = -1
                                break
                            if boardData[i + q][j] != wordl[q]:
                                flag = -1
                                break
                        if flag == 1:
                            #toSolve.remove(word)
                            for q in range(wordLength):
                                solution[i+q][j] = base
                        else:
                            flag = 1  # sove LS
                            for q in range(wordLength):
                                if j-q < 0 or i + q > size - 1:
                                    flag = -1
                                    break
                                if boardData[i + q][j-q] != wordl[q]:
                                    flag = -1
                                    break
                            if flag == 1:
                                #toSolve.remove(word)
                                for q in range(wordLength):
                                    solution[i + q][j-q] = base
                            else:
                                flag = 1  # sove RS
                                for q in range(wordLength):
                                    if j + q > size-1 or i + q > size-1:
                                        flag = -1
                                        break
                                    if boardData[i + q][j + q] != wordl[q]:
                                        flag = -1
                                        break
                                if flag == 1:
                                    #toSolve.remove(word)
                                    for q in range(wordLength):
                                        solution[i + q][j + q] = base
    return [solution, base]
def draw(Data, solution):
    mult = 35
    size = len(Data)

    black = (0, 0, 0)
    white = (255, 255, 255)
    listOfColors = [
        (0, 255, 0),
        (0, 255, 255),
        (255, 0, 255),
        (255, 255, 0),
        (255, 0, 0),
        (102, 255, 255),
        (0, 0, 255),
    ]

    pygame.init()
    screenx, screeny = (size * mult, size * mult)
    screen = pygame.display.set_mode((screenx, screeny))
    pygame.display.set_caption("Cross Word Solution")
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit(0)
    for i in range(len(Data)):
        mult = 35
        for j in range(len(Data)):
            font = pygame.font.SysFont("arial", 22)
            solfont = pygame.font.SysFont("arial", 25)
            if solution[j][i] == 0:
                label = font.render(str(Data[j][i]), 2, white)
                screen.blit(label, (i * mult,j*mult ))
            else:
                color = listOfColors[solution[j][i]%len(listOfColors)]
                label = solfont.render(str(Data[j][i]), 2, color)
                screen.blit(label, (i * mult, j * mult))
    pygame.display.update()
def initialise():
    solution = []
    for i in range(len(boardData)):
        solution.append([])
        for j in range(len(boardData)):
            solution[i].append(0)
    base = 1
    return [solution, base]

boardData = getInput()
solution, base = initialise()
while True:
    print(base)
    draw(boardData, solution)
    temp = base
    solution, base = solve(boardData, solution, base)