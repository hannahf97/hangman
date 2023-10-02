# This is a sample Python script.
import random, pygame,sys, time, string
from InputBox import *
from pygame.locals import *

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# SIZE
CELL_SIZE = 25
WIDTH = 800
HEIGHT = 600

# COLOR
WHITE = (255, 255, 255)  # 하얀색\
BLACK =(0,0,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LINECOLOR = (179, 140, 101)
BGCOLOR = (97,82,113)
GREEN = (169,166,50)
YELLOW = (255,195,18)
done = False

titleFont = pygame.font.Font('source/Jalnan.ttf', 40)
baseFont = pygame.font.Font('source/Jalnan.ttf', 30)
clock = pygame.time.Clock()
answer_list = ['apple', 'family', 'holiday', 'harvest']

text = ''
box = InputBox(300, 400, 250, 100, text)

class GameLogic():
    def __init__(self):  # 게임 초기화 지점
        global alpha_list
        alpha_list = list(string.ascii_lowercase)
        pass

    def calculate(self, alpha):
        for i in range(len(answer)):
            if answer[i] == alpha:
                return i
        return -1

    def start(self):
        screen.fill(WHITE)  # 화면 채우기
        askSurf = titleFont.render("단어를 맞춰보세요 (영어로)", True, BLACK)
        askRect = askSurf.get_rect()
        askRect.center = (800 / 2, 70 )
        screen.blit(askSurf, askRect)
        for i in range(len(alpha_list)):
            messageSurf = baseFont.render(alpha_list[i], False, BLACK)

            if i < 13:
                screen.blit(messageSurf, (100 + 40 * (i + 1), 510))
            else:
                screen.blit(messageSurf, (100 + 40 * (i-13 + 1), 540))

        # MAINIMG = pygame.image.load('source/foot.png')
        # pygame.display.set_icon(MAINIMG)
        # Img_scale = pygame.transform.scale(MAINIMG, (300, 300))
        # img_x = 800 / 2 - 150
        # img_y = 120
        # screen.blit(Img_scale, (img_x, img_y))

        box.draw(screen)
        pygame.display.update()

    def hangman_grow(self, alpha):
        numbers = self.calculate(alpha.lower())
        if numbers != -1:
            message = "맞췄다 !"

        else:
            message = "틀렸다ㅠ"
            if cnt == 1:
                 MAINIMG = pygame.image.load('source/start.png')
            elif cnt == 2:
                MAINIMG = pygame.image.load('source/rope.png')
            elif cnt == 3:
                MAINIMG = pygame.image.load('source/head.png')
            elif cnt == 4:
                MAINIMG = pygame.image.load('source/body.png')
            elif cnt == 5:
                MAINIMG = pygame.image.load('source/arm.png')
            elif cnt == 6:
                MAINIMG = pygame.image.load('source/hand.png')
            elif cnt == 7:
                MAINIMG = pygame.image.load('source/leg.png')
            elif cnt == 8:
                MAINIMG = pygame.image.load('source/foot.png')
                done = True

        askSurf = baseFont.render(message, True, BLUE)
        askRect = askSurf.get_rect()
        askRect.center = (800 / 2, 100)
        pygame.display.set_icon(MAINIMG)
        Img_scale = pygame.transform.scale(MAINIMG, (300, 300))
        img_x = 800 / 2 - 150
        img_y = 120
        screen.blit(Img_scale, (img_x, img_y))

def runGame():
    global done, cnt
    cnt = 0
    input_active = True
    print("answer", answer)
    hangman = GameLogic()
    hangman.start()


    while not done:
        for event in pygame.event.get():
            box.handle_event(event)
            box.update()
            box.draw(screen)

            pygame.display.update()
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()




def showChooseAnswer():
    global answer
    random.shuffle(answer_list)
    while True:

        screen.fill(WHITE)
        titleSurf2 = titleFont.render("단어를 선택해주세요", True, BLACK)
        titleRect2 = titleSurf2.get_rect()
        titleRect2.center = (800 / 2, 100)
        screen.blit(titleSurf2, titleRect2)

        mainSurf1 = baseFont.render(answer_list[0], True, BLACK)
        mainRect1 = mainSurf1.get_rect()
        mainRect1.center = (200, 300)
        screen.blit(mainSurf1, mainRect1)


        mainSurf2 = baseFont.render(answer_list[1], True, BLACK)
        mainRect2 = mainSurf2.get_rect()
        mainRect2.center = (400, 300)
        screen.blit(mainSurf2, mainRect2)


        mainSurf3 = baseFont.render(answer_list[2], True, BLACK)
        mainRect3 = mainSurf3.get_rect()
        mainRect3.center = (600, 300)
        screen.blit(mainSurf3, mainRect3)


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if mainRect3.collidepoint((mousex, mousey)) :
                    answer = answer_list[2]

                    return
                if mainRect2.collidepoint((mousex, mousey)) :
                    answer = answer_list[1]

                    return
                if mainRect1.collidepoint((mousex, mousey)) :
                    answer = answer_list[0]

                    return
        pygame.display.update()

def showStartScreen():
    # title
    screen.fill(WHITE)
    titleSurf1 = titleFont.render("추석에 하는 행맨", True, BLACK)
    titleRect1 = titleSurf1.get_rect()
    titleRect1.center = (800 / 2, 100)
    screen.blit(titleSurf1, titleRect1)
    pygame.display.update()  # 모든 화면 그리기 업데이트
    pygame.time.wait(300)

    # start
    while True:
        startFont = pygame.font.Font('source/Jalnan.ttf', 50)
        startSurf1 = startFont.render('START', True, BLACK)
        startRect1 = startSurf1.get_rect()
        startRect1.center = (800 / 2, 400)
        screen.blit(startSurf1, startRect1)
        pygame.display.update()  # 모든 화면 그리기 업데이트
        pygame.time.wait(300)
        startSurf2 = startFont.render('START', True, RED)
        startRect2 = startSurf2.get_rect()
        startRect2.center = (800 / 2, 400)
        screen.blit(startSurf2, startRect2)
        pygame.display.update()  # 모든 화면 그리기 업데이트
        pygame.time.wait(300)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if startRect1.collidepoint((mousex, mousey)):
                    print("다시 돌아가잇")
                    return

def main():
    global screen, BASICFONT
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    BASICFONT = pygame.font.Font('source/Jalnan.ttf', 18)
    pygame.display.set_caption("추석에 하는 행맨 ! ")

    showStartScreen()
    showChooseAnswer()
    runGame()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
