import pygame   #for drawing the board
import random
def getInput():
    boardData = []
    print("Enter the data :\n")
    boardData.append(input().split())
    size = len(boardData[0])
    for i in range(size-1):
        boardData.append(input().split())
    return boardData
def solve(boardData, solution):

    size = len(boardData)
    if solution == []:
        for i in range(len(boardData)):
            solution.append([])
            for j in range(len(boardData)):
                solution[i].append(0)
    toSolve = input('Enter the words to find :').split()
    print(toSolve)
    for i in range(len(boardData)):
        solution.append([])
        for j in range(len(boardData)):
            for word in toSolve:
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
                        print(wordl[q])
                        if boardData[i][j+q] != wordl[q]:
                            flag = -1
                            break
                    if flag == 1:
                        toSolve.remove(word)
                        for q in range(wordLength):
                            solution[i][j+q] = 1
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
                            toSolve.remove(word)
                            for q in range(wordLength):
                                solution[i+q][j] = 1
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
                                toSolve.remove(word)
                                for q in range(wordLength):
                                    solution[i + q][j-q] = 1
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
                                    toSolve.remove(word)
                                    for q in range(wordLength):
                                        solution[i + q][j + q] = 1
                                else:
                                    if solution[i][j] != 1:
                                        solution[i][j] = 0
    return solution

def draw(Data, solution):
    mult = 20
    size = len(Data)

    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    red = [255, 0, 0]
    green = [0, 255, 0]


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
        mult = 20
        for j in range(len(Data)):
            x = random.randrange(34,255)
            y = random.randrange(34,255)
            z = random.randrange(34,255)
            color = (x, y, z)
            myfont = pygame.font.SysFont("arial", 13)
            if solution[j][i] == 0:
                label = myfont.render(str(Data[j][i]), 2, white)
            elif solution[j][i] == 1:
                label = myfont.render(str(Data[j][i]), 2, color)

            screen.blit(label, (i * mult, j * mult))
    pygame.display.update()


boardData = getInput()
solution = []
while True:
    solution = solve(boardData, solution)
    draw(boardData, solution)
