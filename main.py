# This is a sample Python script.
import random, pygame, sys, time, string
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
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LINECOLOR = (179, 140, 101)
BGCOLOR = (97, 82, 113)
GREEN = (169, 166, 50)
YELLOW = (255, 195, 18)
done = False

titleFont = pygame.font.Font('source/Jalnan.ttf', 40)
baseFont = pygame.font.Font('source/Jalnan.ttf', 30)
clock = pygame.time.Clock()
answer_list = ['apple', 'family', 'holiday', 'harvest']

text = ''
box = InputBox(300, 450, 150, 60, text)


class GameLogic():
    def __init__(self):  # 게임 초기화 지점
        global alpha_list, result
        self.cnt = 0
        self.answer_cnt = 0
        self.self_answer = ''
        self.MAIN_IMG = pygame.image.load('source/blank.png')
        alpha_list = list(string.ascii_lowercase)
        result = ''
        pass

    def calculate(self, alpha):
        numberlist = []
        if self.self_answer.count(alpha) >= 1:
            numberlist.append(-2)
        elif answer.count(alpha) >= 1:
            for i in range(len(answer)):
                if answer[i] == alpha:
                    numberlist.append(i)
        else:
            numberlist.append(-1)

        return numberlist

    def start(self):
        screen.fill(WHITE)  # 화면 채우기
        askSurf = titleFont.render("단어를 맞춰보세요 (영어로)", True, BLACK)
        askRect = askSurf.get_rect()
        askRect.center = (800 / 2, 70)
        screen.blit(askSurf, askRect)

        for i in range(len(answer)):
            answerSurf = baseFont.render('_', False, BLACK)
            screen.blit(answerSurf, (250 + 40 * (i + 1), 140))

        for i in range(len(alpha_list)):
            messageSurf = baseFont.render(alpha_list[i], False, BLACK)

            if i < 13:
                screen.blit(messageSurf, (100 + 40 * (i + 1), 510))
            else:
                screen.blit(messageSurf, (100 + 40 * (i - 13 + 1), 540))

        # MAINIMG = pygame.image.load('source/foot.png')
        # pygame.display.set_icon(MAINIMG)
        # Img_scale = pygame.transform.scale(MAINIMG, (300, 300))
        # img_x = 800 / 2 - 150
        # img_y = 120
        # screen.blit(Img_scale, (img_x, img_y))

        box.draw(screen)
        pygame.display.update()

    def hangman_grow(self):
        text = box.getResult().lower()

        numberlist = self.calculate(text)

        idx = alpha_list.index(text)

        messageSurf = baseFont.render(X, False, RED)
        if idx < 13:
            screen.blit(messageSurf, (100 + 40 * (idx + 1), 510))
        else:
            screen.blit(messageSurf, (100 + 40 * (idx - 13 + 1), 540))

        Img_scale = pygame.transform.scale(self.MAIN_IMG, (300, 300))
        img_x = 800 / 2 - 150
        img_y = 170

        if numberlist[0] != -1 and numberlist[0] != -2 :
            message = "맞췄다 !"
            self.answer_cnt += answer.count(text)
            self.self_answer += text
            for number in numberlist:
                answerSurf = baseFont.render(text, False, BLACK)
                screen.blit(answerSurf, (250 + 40 * (number + 1), 140))

            askSurf = baseFont.render(message, True, BLUE)
            askRect = askSurf.get_rect()
            askRect.center = (800 / 2, 300)
            screen.blit(askSurf, askRect)
            pygame.display.update()  # 모든 화면 그리기 업데이트
            pygame.time.wait(300)

            screen.blit(Img_scale, (img_x, img_y))

            pygame.display.update()

            if self.answer_cnt == len(answer):
                showYouEndScreen("Win")
                pygame.time.delay(5000)

        elif numberlist[0] == -2:
            message = "이미 입력한 글자"
            askSurf = baseFont.render(message, True, RED)
            askRect = askSurf.get_rect()
            askRect.center = (800 / 2, 300)
            screen.blit(askSurf, askRect)
            pygame.display.update()  # 모든 화면 그리기 업데이트
            pygame.time.wait(300)

            screen.blit(Img_scale, (img_x, img_y))
            pygame.display.update()

        else:
            message = "틀렸다ㅠ"
            self.cnt += 1
            if self.cnt == 1:
                self.MAIN_IMG = pygame.image.load('source/start.png')
            elif self.cnt == 2:
                self.MAIN_IMG = pygame.image.load('source/rope.png')
            elif self.cnt == 3:
                self.MAIN_IMG = pygame.image.load('source/head.png')
            elif self.cnt == 4:
                self.MAIN_IMG = pygame.image.load('source/arm.png')
            elif self.cnt == 5:
                self.MAIN_IMG = pygame.image.load('source/hand.png')
            elif self.cnt == 6:
                self.MAIN_IMG = pygame.image.load('source/body.png')
            elif self.cnt == 7:
                self.MAIN_IMG = pygame.image.load('source/leg.png')
            else:
                self.MAIN_IMG = pygame.image.load('source/foot.png')

            askSurf = baseFont.render(message, True, RED)
            askRect = askSurf.get_rect()
            askRect.center = (800 / 2, 300)
            screen.blit(askSurf, askRect)

            pygame.display.update()  # 모든 화면 그리기 업데이트

            pygame.time.wait(300)

            askSurf2 = baseFont.render(message, True, WHITE)
            askRect2 = askSurf2.get_rect()
            askRect2.center = (800 / 2, 300)
            screen.blit(askSurf2, askRect2)

            pygame.display.update()


            screen.blit(Img_scale, (img_x, img_y))

            pygame.display.update()  # 모든 화면 그리기 업데이트

            if self.cnt == 8:
                showYouEndScreen("Lose")
                pygame.time.delay(5000)


def runGame():
    global done
    done = False
    hangman = GameLogic()
    hangman.start()

    while not done:
        for event in pygame.event.get():
            box.handle_event(event)
            box.update()
            box.draw(screen)

            pygame.display.flip()

            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                print("키 확인용" , len(box.getResult()))
                if event.key == 13:
                    hangman.hangman_grow()


def showYouEndScreen(message):
    if message == 'Lose':  # 질경우
        overSurf1 = titleFont.render('GAME', True, BLACK)  # game이라는 글씨색 설정
        overRect1 = overSurf1.get_rect()
        overRect1.center = (WIDTH / 2 - 140, CELL_SIZE)  # game의 위치설정

        overSurf2 = titleFont.render('OVER', True, BLACK)  # GameOver라는 글자가 주황색과 빨강색이 겹쳐서나오게한다.
        overRect2 = overSurf2.get_rect()
        overRect2.center = (WIDTH / 2 + 130, CELL_SIZE)

        shadowSurf1 = titleFont.render('GAME', True, RED)
        shadowRect1 = shadowSurf1.get_rect()
        shadowRect1.center = (WIDTH / 2 - 140 + 4, CELL_SIZE + 4)

        shadowSurf2 = titleFont.render('OVER', True, RED)
        shadowRect2 = shadowSurf2.get_rect()
        shadowRect2.center = (WIDTH / 2 + 130 + 4, CELL_SIZE + 4)

    elif message == 'Win':  # 이겼을 경우
        overSurf1 = titleFont.render('YOU', True, BLACK)  # YOU, WIN이라는 글자가 나오도록한다
        overRect1 = overSurf1.get_rect()
        overRect1.center = (WIDTH / 2 - 120, CELL_SIZE)

        overSurf2 = titleFont.render('WIN!', True, BLACK)
        overRect2 = overSurf2.get_rect()
        overRect2.center = (WIDTH / 2 + 120, CELL_SIZE)

        shadowSurf1 = titleFont.render('YOU', True, RED)
        shadowRect1 = shadowSurf1.get_rect()
        shadowRect1.center = (WIDTH / 2 - 120 + 4, CELL_SIZE + 4)

        shadowSurf2 = titleFont.render('WIN!', True, RED)
        shadowRect2 = shadowSurf2.get_rect()
        shadowRect2.center = (WIDTH / 2 + 120 + 4, CELL_SIZE + 4)

    screen.blit(shadowSurf1, shadowRect1)  # 4개의 변수가 모두다 보이도록 만든다 .
    screen.blit(shadowSurf2, shadowRect2)
    screen.blit(overSurf1, overRect1)
    screen.blit(overSurf2, overRect2)

    pygame.display.update()  # 화면을 update해준다


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
                if mainRect3.collidepoint((mousex, mousey)):
                    answer = answer_list[2]

                    return
                if mainRect2.collidepoint((mousex, mousey)):
                    answer = answer_list[1]

                    return
                if mainRect1.collidepoint((mousex, mousey)):
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
