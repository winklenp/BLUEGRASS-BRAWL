import pygame
import time
import math
import sys
import game
import gameOver

BGCOLOR=(255,255,255)

def main2():
    pygame.init()
    titlescreen = titleScreen()
    titlescreen.runtitleScreen()




class titleScreen:
    def __init__(self):
        self.width = 1000
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background1 = Background("background.jpg", [0,0])
        self.screen.fill(BGCOLOR) 
        self.newfont = pygame.font.Font("CountryGold.ttf", 100)
        self.newfont1 = pygame.font.Font("CountryGold.ttf", 40)
        self.newfont2 = pygame.font.Font("CountryGold.ttf", 35)
        self.myfont = pygame.font.SysFont("monospace", 40)
        self.myfont2 =  pygame.font.SysFont("timesnewroman", 25)
        self.titletext = self.newfont.render("Bluegrass Brawl",1,pygame.Color("black"))
        pygame.display.set_caption('Bluegrass Brawl') 
        pygame.mixer.init()
        pygame.mixer.set_num_channels(4)
        if pygame.mixer.get_busy() != True:
            self.song = pygame.mixer.Sound("sounds/bluegrassSong.wav")
            self.song.set_volume(0.6)
            pygame.mixer.Sound.play(self.song, 20)


    def boxDraw(self, x, y, width, height, text, textx):
        button = pygame.rect.Rect(x, y, width, height)
        buttontext = self.newfont2.render(text, 1, pygame.Color("black"))
        pygame.draw.rect(self.screen, pygame.Color("black"),button,4)
        centerpoint=(textx,y+13)
        self.screen.blit(buttontext, centerpoint)
        posx, posy = pygame.mouse.get_pos()
        if posx > x and posx< x+width and posy > y and posy < y+height:
            highlight = pygame.rect.Rect(x-5, y-5, width+10, height+10)
            pygame.draw.rect(self.screen, pygame.Color("white"), highlight, 5)

    def menuBoxes(self):
        self.boxDraw(440,190,120,60,"Play", 465)
        self.boxDraw(440,270,120,60, "HowTo",448)
        self.boxDraw(440,350,120,60, "Info", 466)
        self.boxDraw(440, 430, 120, 60, "Credits", 445)
        self.boxDraw(440, 510, 120, 60, "Quit", 463)

    def checkForQuit(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 440 and p1x < 560 and p1y > 510 and p1y < 570:
            sys.exit()

    def checkForPlay(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 440 and p1x < 560 and p1y > 190 and p1y < 250:
            char = characterscreen()
            char.runCharacterScreen()



    def checkForCredits(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 440 and p1x < 560 and p1y > 430 and p1y < 490:
            c = CreditsScreen1(self.screen)
            c.runCreditScreen()
    def checkForHowTo(self):
        p1x, p1y, = pygame.mouse.get_pos()
        if p1x > 440 and p1x < 560 and p1y > 270 and p1y <330:
            h = HowToButton(self.screen)
            h.runHowToScreen()
    def checkForInfo(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 440 and p1x < 560 and p1y > 350 and p1y < 410:
            i = InfoButton(self.screen)
            i.runInfoScreen()
    

    def runtitleScreen(self):
        pygame.key.set_repeat(500, 30)
        while 1:
            t=time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.checkForPlay()
                    self.checkForCredits()
                    self.checkForInfo()
                    self.checkForHowTo()
                    self.checkForQuit()

            pygame.display.update()
            self.screen.blit(self.background1.image, (0, 0))
            self.screen.blit(self.titletext, (160, 30))
            self.menuBoxes()
            time.sleep(max(0.017-(time.time()-t),0))


        

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("background.jpg")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class CreditsScreen1:
    def __init__(self, screen):
        self.width = 1000
        self.screen = screen
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background1 = Background("background.jpg", [0,0])
        self.screen.fill(BGCOLOR)
        self.newfont = pygame.font.Font("CountryGold.ttf",65)
        self.newfont4 = pygame.font.Font("CountryGold.ttf", 25)
        self.newfont3 = pygame.font.Font("CountryGold.ttf", 40)
        self.newfont2 = pygame.font.Font("CountryGold.ttf", 35)
        self.newfont5 = pygame.font.Font("CountryGold.ttf",27)
        self.credits = self.newfont2.render("Developed By:", 1, pygame.Color("black"))
        self.credits2 = self.newfont5.render("Samuel Dickinson", 1, pygame.Color("black"))
        self.credits3 = self.newfont5.render("Reed Phillips", 1, pygame.Color("black"))
        self.credits4 = self.newfont5.render("Cooper Standard", 1, pygame.Color("black"))
        self.credits5 = self.newfont5.render("Noah Winkler", 1, pygame.Color("black"))
        self.credits6 = self.newfont5.render("With Special Thanks To:", 1, pygame.Color("black"))
        self.credits7 = self.newfont4.render("All The Artists Whose Work We Used", 1, pygame.Color("black"))
        self.credits8 = self.newfont4.render("The Developers of Python", 1, pygame.Color("black"))
        self.credits9 = self.newfont4.render("The Developers of Pygame", 1, pygame.Color("black"))
        self.credits10 = self.newfont4.render("Dr. Matt Boutell", 1, pygame.Color("black"))
        self.credits11 = self.newfont4.render("Larry Gates", 1, pygame.Color("black"))
        self.credits12 = self.newfont4.render("Alyssa Crawford", 1, pygame.Color("black"))
        self.credits13 = self.newfont4.render("And All Of The Operation Catapult Faculty", 1, pygame.Color("black"))

        self.centerline = pygame.rect.Rect(499,0,3,700)
        self.credittext = self.newfont.render("Credits", 1, pygame.Color("black"))
    def runCreditScreen(self):
        pygame.key.set_repeat(500, 30)
        while 1:
            t=time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.checkForBack():
                        t = titleScreen()
                        t.runtitleScreen()
            self.screen.blit(self.background1.image, (0,0))
            self.screen.blit(self.credits, (385, 120))
            self.screen.blit(self.credits2, (10, 190))
            self.screen.blit(self.credits3, (310, 190))
            self.screen.blit(self.credits4, (527, 190))
            self.screen.blit(self.credits5, (807, 190))
            self.screen.blit(self.credits6, (337, 310))
            self.screen.blit(self.credits7, (280, 480))
            self.screen.blit(self.credits8, (340, 520))
            self.screen.blit(self.credits9, (338, 560))
            self.screen.blit(self.credits10, (400, 360))
            self.screen.blit(self.credits11, (430, 400))
            self.screen.blit(self.credits12, (406, 440))
            self.screen.blit(self.credits13, (240, 600))

            self.screen.blit(self.credittext, (388, 10))
            #pygame.draw.rect(self.screen, pygame.Color("white"), self.centerline)
            self.boxDraw(10, 10, 120, 60, "Back", 32)
            pygame.display.update()
            time.sleep(max(0.017 - (time.time() - t), 0))
    def boxDraw(self, x, y, width, height, text, textx):
        button = pygame.rect.Rect(x, y, width, height)
        buttontext = self.newfont2.render(text, 1, pygame.Color("black"))
        pygame.draw.rect(self.screen, pygame.Color("black"),button,4)
        centerpoint=(textx,y+13)
        self.screen.blit(buttontext, centerpoint)
        posx, posy = pygame.mouse.get_pos()
        if posx > x and posx< x+width and posy > y and posy < y+height:
            highlight = pygame.rect.Rect(x-5, y-5, width+10, height+10)
            pygame.draw.rect(self.screen, pygame.Color("white"), highlight, 5)


    def checkForBack(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 10 and p1x < 120 and p1y > 10 and p1y < 70:
            return True



class HowToButton:
    def __init__(self, screen):
        self.width = 1000
        self.height = 700
        self.screen = screen
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background1 = Background("background.jpg", [0,0])
        self.screen.fill(BGCOLOR)
        self.newfont = pygame.font.Font("CountryGold.ttf", 50)
        self.newfont2 = pygame.font.Font("CountryGold.ttf", 35)
        self.newfont3 = pygame.font.Font("CountryGold.ttf", 40)
        self.dividingline = pygame.Rect(0,350,1000,0)
        self.playeronetext = self.newfont.render("Player 1", 1, pygame.Color("black"))
        self.playertwotext = self.newfont.render("Player 2", 1, pygame.Color("black"))
        self.centerline = pygame.rect.Rect(499, 0, 3, 700)
        self.player1line = pygame.Rect(420, 49, 150, 0)
        self.player2line = pygame.Rect(420, 399, 150, 0)

    def player1stuff(self):
        self.textDraw(425, 5, "Player 1", 40)
        self.textDraw(310, 75, "Move Right: D", 25)
        self.textDraw(515, 75, "Move Left: A", 25)
        self.textDraw(450, 115, "Jump: W", 25)
        self.textDraw(445, 155, "Attack: Z", 25)
        self.textDraw(355, 195, "Move Attack: Move and Z", 25)
        self.textDraw(350, 235, "Special Attack: F OR Shift", 25)
        self.textDraw(270, 275, "Jump Attack: Jump and F OR Jump and Shift", 25)
        self.textDraw(245, 315, "Projectile Attack: Move and F OR Move and Shift", 25)

    def player2stuff(self):
        self.textDraw(425,355,"Player 2",40)
        self.textDraw(320, 425, "Move Right: J", 25)
        self.textDraw(515, 425, "Move Left: L", 25)
        self.textDraw(450, 465, "Jump: I", 25)
        self.textDraw(445, 505, "Attack: N", 25)
        self.textDraw(355, 545, "Move Attack: Move and N", 25)
        self.textDraw(350, 585, "Special Attack: ; OR B", 25)
        self.textDraw(270, 625, "Jump Attack: Jump and B OR Jump and B ", 25)
        self.textDraw(250, 665, "Projectile Attack: Move and ; OR Move and B", 25)



    def checkForBack(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 10 and p1x < 120 and p1y > 10 and p1y < 70:
            return True

    def boxDraw(self, x, y, width, height, text, textx):
        button = pygame.rect.Rect(x, y, width, height)
        buttontext = self.newfont2.render(text, 1, pygame.Color("black"))
        pygame.draw.rect(self.screen, pygame.Color("black"),button,4)
        centerpoint=(textx,y+13)
        self.screen.blit(buttontext, centerpoint)
        posx, posy = pygame.mouse.get_pos()
        if posx > x and posx< x+width and posy > y and posy < y+height:
            highlight = pygame.rect.Rect(x-5, y-5, width+10, height+10)
            pygame.draw.rect(self.screen, pygame.Color("white"), highlight, 5)

    def textDraw(self, x, y, text, fontsize):
        font = pygame.font.Font("CountryGold.ttf", fontsize)
        drawntext = font.render(text, 1, pygame.Color("black"))
        self.screen.blit(drawntext, (x,y))

    def runHowToScreen(self):
        pygame.key.set_repeat(500, 30)
        while 1:
            t=time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.checkForBack():
                        return

            self.screen.blit(self.background1.image, (0,0))
            #pygame.draw.rect(self.screen,pygame.Color("Black"), self.dividingline, 5)
            #pygame.draw.rect(self.screen, pygame.Color("white"), self.centerline, 5)
            pygame.draw.rect(self.screen, pygame.Color("black"), self.player1line, 5)
            pygame.draw.rect(self.screen, pygame.Color("black"), self.player2line, 5)
            self.player1stuff()
            self.player2stuff()
            self.boxDraw(10, 10, 120, 60, "Back", 32)
            pygame.display.update()
            time.sleep(max(0.017-(time.time()-t),0))

class InfoButton:
    def __init__(self, screen):
        self.width = 1000
        self.height = 700
        self.screen = screen
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background1 = Background("background.jpg", [0, 0])
        self.screen.fill(BGCOLOR)
        self.newfont = pygame.font.Font("CountryGold.ttf", 25)
        self.newfont2 = pygame.font.Font("CountryGold.ttf", 35)
        self.newfont3 = pygame.font.Font("CountryGold.ttf", 40)
        self.centerline = pygame.rect.Rect(499, 0, 3, 700)
        self.dividingline = pygame.Rect(0, 350, 1000, 0)




    def boxDraw(self, x, y, width, height, text, textx):
        button = pygame.rect.Rect(x, y, width, height)
        buttontext = self.newfont2.render(text, 1, pygame.Color("black"))
        pygame.draw.rect(self.screen, pygame.Color("black"), button, 4)
        centerpoint = (textx, y + 13)
        self.screen.blit(buttontext, centerpoint)
        posx, posy = pygame.mouse.get_pos()
        if posx > x and posx < x + width and posy > y and posy < y + height:
            highlight = pygame.rect.Rect(x - 5, y - 5, width + 10, height + 10)
            pygame.draw.rect(self.screen, pygame.Color("white"), highlight, 5)

    def textDraw(self, x, y, text, fontsize):
        font = pygame.font.Font("CountryGold.ttf", fontsize)
        drawntext = font.render(text, 1, pygame.Color("black"))
        self.screen.blit(drawntext, (x,y))

    def infoText(self):
        self.textDraw(451, 10, "Info", 55)
        self.textDraw(5, 120, "Flying pitchforks, helmets with rockets, and axe swinging woodsmen: this is Bluegrass Brawl.", 22)
        self.textDraw(5, 170, "Bluegrass Brawl is a fighting game drawing inspiration from classics of the genre, such as", 22)
        self.textDraw(5, 220, "Super Smash Brothers: Brawl and Street Fighter. Common features of games in this genre", 22)
        self.textDraw(5, 270, "include muscular and intense characters fighting to the death in epic battle arenas, where", 22)
        self.textDraw(5, 320, "only one fighter survives to be crowned the winner, or as some might say, take it all the way", 22)
        self.textDraw(5, 370, "to the top. Our approach to the fighting game includes a cast of eight unique characters", 22)
        self.textDraw(5, 420, "each with their own individual and specialized attacks. We include two opposing sides:", 22)
        self.textDraw(5, 470, "simple minded country folk, lead by Bluegrass Billy, and the evil villains, lead by Metal Man.", 22)
        self.textDraw(5, 520, "In this classic example of a battle between good and evil, the outcome depends on the", 22)
        self.textDraw(5, 570, "individual skill of the players. Players are able to choose their own characters at the start", 22)
        self.textDraw(5, 620, "of every game, resulting in many fun and dynamic match-ups.",22)
        self.textDraw(5, 670, "", 22)
        self.textDraw(5, 720, "", 22)


    def runInfoScreen(self):
        pygame.key.set_repeat(500, 30)
        while 1:
            t = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.checkForBack():
                        return
            self.screen.blit(self.background1.image, (0, 0))
            self.boxDraw(10, 10, 120, 60, "Back", 32)
            pygame.draw.rect(self.screen, pygame.Color("Black"), self.dividingline, 5)
            pygame.draw.rect(self.screen, pygame.Color("white"), self.centerline, 5)
            self.infoText()
            pygame.display.update()
            time.sleep(max(0.017 - (time.time() - t), 0))

    def checkForBack(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 10 and p1x < 120 and p1y > 10 and p1y < 70:
            return True

class characterscreen:
    def __init__(self):
        self.width = 1000#This line is very important
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background1 = Background("background.jpg", [0, 0])
        self.screen.fill(BGCOLOR)
        self.newfont = pygame.font.Font("CountryGold.ttf", 100)
        self.newfont1 = pygame.font.Font("CountryGold.ttf", 40)
        self.newfont2 = pygame.font.Font("CountryGold.ttf", 35)
        self.newfont3 = pygame.font.Font("CountryGold.ttf", 40)
        self.myfont = pygame.font.SysFont("monospace", 40)
        self.myfont2 = pygame.font.SysFont("timesnewroman", 25)
        self.player1=-1
        self.player2=-1
        self.buttons=[]
        self.buttons.append(Button(100, 150, 300, 60, "Bluegrass Billy", 130))
        self.buttons.append(Button(100, 300, 300, 60, "Country Carl", 140))
        self.buttons.append(Button(100, 450, 300, 60, "Singin' Susan", 145))
        self.buttons.append(Button(100, 600, 300, 60, "Backwoods Bob", 125))
        self.buttons.append(Button(600, 150, 300, 60, "Metal Man", 663))
        self.buttons.append(Button(600, 300, 300, 60, "Sinister Stan", 650))
        self.buttons.append(Button(600, 450, 300, 60, "Evil Emily", 670))
        self.buttons.append(Button(600, 600, 300, 60, "Monstrous Mike", 626))
        self.images=[]
        self.images.append(CharacterImage("BluegrassBilly",60,150,130//4,266//4))
        self.images.append(CharacterImage("CountryCarl",20,290,200 // 2, 140 // 2))
        self.images.append(CharacterImage("SinginSusan",30,450,160 // 2, 124 // 2))
        self.images.append(CharacterImage("BackwoodsBob",30,600,160 // 2, 124 // 2))
        self.images.append(CharacterImage("MetalMan",530,150,160 // 2, 124 // 2))
        self.images.append(CharacterImage("SinisterStan",520,300,160 // 2, 124 // 2))
        self.images.append(CharacterImage("EvilEmily",530,450,144 // 2, 124 // 2))
        self.images.append(CharacterImage("MonstrousMike",520,595,210 // 2, 130 // 2))

    def runCharacterScreen(self):
        pygame.key.set_repeat(500, 30)
        while 1:
            t = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.checkForBack():
                        return
                    self.checkSelection()
                    if self.player1>=0 and self.player2>=0:
                        if self.checkForPlayButton():
                            return
            self.screen.blit(self.background1.image, (0, 0))
            self.drawcharacterboxes()
            if self.player1>=0:
                self.drawPicked1()
            if self.player2>=0:
                self.drawPicked2()
            if self.player1>=0 and self.player2>=0:
                self.PlayButton()
            pygame.display.update()
            time.sleep(max(0.017 - (time.time() - t), 0))

    def PlayButton(self):
        self.boxDrawer(425, 370, 150, 60, "Play", 465)

    def drawPicked1(self):
        self.boxDrawer(200,20,150,60,"Player 1",210)
        self.images[self.player1].render(self.screen,360,20)

    def drawPicked2(self):
        self.boxDrawer(650,20,150,60,"Player 2",660)
        self.images[self.player2].render(self.screen,550,20)

    def checkSelection(self):
        if self.player1>=0 and self.player2>=0:
            return
        posx, posy = pygame.mouse.get_pos()
        select=-1
        for i in range(len(self.buttons)):
            if self.buttons[i].contains(posx,posy):
                select=i
                break
        if select>=0:
            if self.player1==-1:
                self.player1=select
            else:
                self.player2=select


    def checkForPlayButton(self):
        posx, posy = pygame.mouse.get_pos()
        if posx > 425 and posx < 575 and posy > 370 and posy < 430:
            g = game.Game(self.player1,self.player2)
            winner = g.runGame()
            go = gameOver.GameOver(self.screen,winner)
            pressedbutton = go.runGameOver()
            if pressedbutton == "PlayAgain":
                char = characterscreen()
                char.runCharacterScreen()
            if pressedbutton == "MM":
                t = titleScreen()
                t.runtitleScreen()
            if pressedbutton == "Credits":
                c = CreditsScreen1(self.screen)
                c.runCreditScreen()
            return True

    def boxDrawer(self, x, y, width, height, text, textx):
        button = pygame.rect.Rect(x, y, width, height)
        buttontext = self.newfont2.render(text, 1, pygame.Color("black"))
        pygame.draw.rect(self.screen, pygame.Color("black"), button, 4)
        centerpoint = (textx, y + 13)
        self.screen.blit(buttontext, centerpoint)
        posx, posy = pygame.mouse.get_pos()
        if posx > x and posx < x + width and posy > y and posy < y + height:
            highlight = pygame.rect.Rect(x - 5, y - 5, width + 10, height + 10)
            pygame.draw.rect(self.screen, pygame.Color("white"), highlight, 5)
    def drawcharacterboxes(self):
        self.back = self.newfont3.render("Back", 1, pygame.Color("black"))
        self.boxDrawer(10,10, 120, 60, "Back", 32)
        for i in self.images:
            i.render(self.screen)
        for b in self.buttons:
            b.render(self)
    def checkForBack(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 10 and p1x < 120 and p1y > 10 and p1y < 70:
            return True
class Button:
    def __init__(self,x,y,width,height,text,textx):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
        self.textx=textx
    def render(self, charScreen):
        charScreen.boxDrawer(self.x,self.y,self.width,self.height,self.text,self.textx)
    def contains(self,x,y):
        return x>=self.x and y>=self.y and x<=self.x+self.width and y<=self.y+self.height

class CharacterImage:
    def __init__(self, file, x, y, width, height):
        self.image=pygame.transform.scale(pygame.image.load("CharacterFiles/CharacterModels/"+file+"/lookingRight.png"),(width,height))
        self.x=x
        self.y=y
    def render(self,screen,x=-1,y=-1):
        if x==-1 and y==-1:
            x=self.x
            y=self.y
        screen.blit(self.image,(x,y))
main2()








#testing
