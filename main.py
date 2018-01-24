import pygame   #for drawing the board
def getInput():
    boardData = []
    size = int(input("enter the size :"))
    print("Enter the data :\n")
    for i in range(size):
        boardData.append(input().split())
    return boardData
def solve(boardData):

    solution = []
    size = len(boardData)
    toSolve = input('Enter the words to find :').split()
    print(toSolve)
    for i in range(len(boardData)):
        solution.append([])
        for j in range(len(boardData)):
            solution[i].append(0)
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
    mult = 40
    size = len(Data)

    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 0, 255)

    pygame.init()
    screenx, screeny = (size * mult, size * mult)
    screen = pygame.display.set_mode((screenx, screeny))
    pygame.display.set_caption("Cross Word Solution")
    screen.fill(black)
    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit(0)
        for i in range(len(Data)):
            mult = 40
            for j in range(len(Data)):
                myfont = pygame.font.SysFont("arial", 15)
                if solution[j][i] == 0:
                    label = myfont.render(str(Data[j][i]), 2, white)
                else:
                    label = myfont.render(str(Data[j][i]), 2, green)
                screen.blit(label, (i * mult, j * mult))
        pygame.display.update()




boardData = getInput()
solution = solve(boardData)
draw(boardData, solution)
