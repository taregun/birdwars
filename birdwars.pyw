import pygame
import random
import time
pygame.init()
pygame.display.set_caption("Bird Wars (Radio: Tarik Ganić)")

score=0
apples = 0
player_try=1
rootFolder = __file__.replace("\\", "/")
print(rootFolder)
rootFolder = rootFolder[:rootFolder.index("/birdwars.py") + len("/birdwars.py")]
with open(rootFolder + "/other/high score.txt", "r") as file:
    his = int(file.read())
birdl = pygame.image.load(rootFolder + '/other/texture/ptica.left.png')
birdl2 = pygame.image.load(rootFolder + '/other/texture/ptica.left.png')
birdr = pygame.image.load(rootFolder + '/other/texture/ptica.right.png')
background = pygame.image.load(rootFolder + '/other/texture/bckgr.png')
game_over = pygame.image.load(rootFolder + '/other/texture/game over.jpg')
home = pygame.image.load(rootFolder + '/other/texture/home.png')
drvo = pygame.image.load(rootFolder + '/other/texture/drvo.png')
drvo2 = pygame.image.load(rootFolder + '/other/texture/drvo.png')
apple = pygame.image.load(rootFolder + '/other/texture/apple.png')
mask1 = pygame.mask.from_surface(birdl)
mask3 = pygame.mask.from_surface(birdl2)
mask4 = pygame.mask.from_surface(apple)
mask2 = pygame.mask.from_surface(birdr)
cx=800

screen_width = 1600
screen_height = 850
screen = pygame.display.set_mode((screen_width, screen_height))
run = True
x = 800
y = 300
x2=0
y2=200
applex=1600
appley=random.randint(0,500)
drvox = 800
drvox2 = 1600
bx=0
playery = 100
gravity = 0
gameover=False
screen.blit(home,(0,0))
pygame.display.update()
time.sleep(2)
pygame.font.init() 

def show_score(score,font,size,gameOver):
    my_font = pygame.font.SysFont(font, size)
    toprint ="Score:" + str(score)
    toprint2 ="High-score:"+str(his)
    toprint3 ="Apples:"+str(apples)
    if gameOver:
        scorePrint = my_font.render(toprint, False, (200, 0, 0))
        screen.blit(scorePrint, (5,5))
        scorePrint = my_font.render(toprint2, False, (200, 0, 0))
        screen.blit(scorePrint, (1055,5))
        scorePrint = my_font.render(toprint3, False, (200, 0, 0))
        screen.blit(scorePrint, (605,5))
    else:
        scorePrint = my_font.render(toprint, False, (0, 0, 0))
        screen.blit(scorePrint, (5,5))
        scorePrint = my_font.render(toprint2, False, (0, 0, 0))
        screen.blit(scorePrint, (1055,5))
        scorePrint = my_font.render(toprint3, False, (0, 0, 0))
        screen.blit(scorePrint, (605,5))
        screen.blit(apple, (480,0))
        
    scorePrint = my_font.render(toprint, False, (230, 230, 250))
    screen.blit(scorePrint, (0,0))
    scorePrint = my_font.render(toprint2, False, (230, 230, 250))
    screen.blit(scorePrint, (1050,0))
    scorePrint = my_font.render(toprint3, False, (230, 230, 250))
    screen.blit(scorePrint, (600,0))
def render_screen():
    
    screen.fill((0, 0, 250))
    screen.blit(background, (bx,602))
    screen.blit(birdl, (x, y))
    screen.blit(birdl,(x2,y2))
    screen.blit(birdr,(50,playery))
    screen.blit(apple, (applex,appley))
    screen.blit(drvo,(drvox,300))
    screen.blit(drvo2,(drvox2,300))
    show_score(score,'Comic Sans',80,gameover)
     
     
while run:
    applex=applex-7
    if applex<-1600:
        applex=1600
        appley=random.randint(0,500)

    if score>his:
        his=score
    offset = (50 - x, playery - y)
    offset2 = (50-x2, playery - y2)
    offset3 = (50-applex, playery - appley)
    render_screen()
    drvox=drvox-7
    if drvox<-283:
        drvox=2000
    drvox2=drvox2-7
    if drvox2<-283:
        drvox2=2000
    x=x-12
    x2=x2-10
    bx=bx-7
    if bx<-1600:
        bx=0
    gravity=gravity-0.2
    playery=playery-gravity*2
    if x<-200:
        x=1600
        y=random.randint(100,400)
        score=score+1
    if x2<-200:
        x2=1600
        y2=random.randint(100,400)
        score=score+1
    if mask2.overlap(mask4, offset3):
        score=score+5
        apples=apples+1
        applex=-100
    if playery<0 or playery>610 or  mask1.overlap(mask2, offset) or mask3.overlap(mask2, offset2):
            gameover=True
            screen.blit(game_over,(0,0))
            show_score(score,'Comic Sans',80,gameover)

            pygame.display.update()

            player_try=player_try+1
            x=800
            playery=0
            gravity=-2
            bx=0
            time. sleep(1)
            score=0
            apples=0
            gameover=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            gravity = 4
    pygame.display.update()

with open(rootFolder + "/other/high score.txt", "w") as file:
    file.write(str(his))

pygame.quit()