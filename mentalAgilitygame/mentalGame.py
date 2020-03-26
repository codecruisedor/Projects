import pygame
from sys import *
from tkinter import messagebox
import time
import random
from collections import Counter
 

#-----------------images array for placing random images on the screen---------------------------#

images = [  "D:\\PythonProjects\\mentalAgilitygame\\pictures\\boat.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\boy.jpg", 
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\bubble.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\desert.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\fantasyCastle.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\flowers.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\hoseLake.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\jellyfish.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\lake.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\lion.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\mountain.jpg",          
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\planet.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\roadOrange.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\SunSet.png",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\train.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\treeSunset.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\winterTree.jpg",
            "D:\\PythonProjects\\mentalAgilitygame\\pictures\\kingfisher.jpg", 
        ]
#-----------image positons to set imges randomly-------------------#

imagePositions = [(0,0),(100,0),(200,0),(300,0),(400,0),(500,0),
(0,100),(100,100),(200,100),(300,100),(400,100),(500,100),(0,200),(100,200),(200,200),
(300,200),(400,200),(500,200),(0,300),(100,300),(200,300),(300,300),(400,300),(500,300),
(0,400),(100,400),(200,400),(300,400),(400,400),(500,400),(0,500),(100,500),(200,500),(300,500),
(400,500),(500,500)]



#-------------loads the images on the screen---------------# 
def loadImages(rows,width,screen):

    image_positions = {}
    image_list = 2*images

    while not (not imagePositions):
        
        newImage = random.choice(image_list)
        newPos = random.choice(imagePositions)
        image_positionsNew = {newPos:newImage}
        image_positions.update(image_positionsNew)
        image_list.remove(newImage)
        imagePositions.remove(newPos)

    for pos,image in image_positions.items():
        image_to_be_loaded = pygame.image.load(image).convert_alpha()
        screen.blit(image_to_be_loaded,pos)
        pygame.display.update()

    time.sleep(5)

    x1 = 0
    y1 = 0
    widthRect = 100
    HieghtRect = 100
    

    for row in range(6):
        for cols in range(6):
            screen.fill((0,0,0),pygame.Rect((x1,y1,widthRect,HieghtRect)))
            x1 += 100
        y1 += 100
        x1 = 0

    
    drawGrid(rows,width,screen)
    pygame.display.update()
    
 
    return image_positions


#-----------initializes the main menu---------------#
def initializeMenu():

    #create button functionality of the menu
    font2 = pygame.font.SysFont('Hack Bold', 55)
    font = pygame.font.SysFont('Hack Bold', 25,italic = True)
    menuscreen = pygame.display.set_mode((600,600)) 
    GREEN = (0,255,0)
    RED = (255,0,0)
    menuscreen.fill((0,0,0))
    playButton = pygame.draw.rect(menuscreen,GREEN,(220,200,150,50),20)
    ExitButton = pygame.draw.rect(menuscreen,RED,(220,300,150,50),20) 
    menuscreen.blit(font.render('PLAY!', True, (255,0,0)), (270, 215))
    menuscreen.blit(font.render('EXIT', True, (0,255,0)), (270, 315))
    menuscreen.blit(font2.render('FIND PAIRS', True, (255,0,0)), (195, 100))
    soundImage = pygame.image.load("sound.jpg").convert_alpha()
    soundpos = (450,100)
    menuscreen.blit(soundImage , soundpos)
    mask = pygame.mask.from_surface(soundImage)
    pygame.mixer.music.load("fur_else.mp3")
    pygame.mixer.music.play()
   
    pygame.display.update()
    running = True
    volume = 1.0
    increment = 0

    while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                        
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mousepos = pygame.mouse.get_pos()
                    if playButton.collidepoint(mousepos):
                        return True
                    elif ExitButton.collidepoint(mousepos):
                        return False
                    elif mask.get_at((event.pos[0]-soundpos[0], event.pos[1]-soundpos[1])):
                        volume -= 0.2
                        pygame.mixer.music.set_volume(volume)
                                            
                              
    return 0


  

#-------------------draws the grid-------------------------#
def drawGrid(rows,w,screen):
        spacebtween = (w-200)//rows
        x = 0
        y = 0
       
        for i in range(rows):
            x= x + spacebtween
            y= y + spacebtween
            pygame.draw.line(screen,(255,255,255),(x,0),(x,w-200))
            pygame.draw.line(screen,(255,255,255),(0,y),(w-200,y))
        pygame.display.update()    



#----------------blackOutScreen------------------------------#

def blackOutScreen(screen,OpenedImages,images):
   
    for key,value in images.items():
        if value not in OpenedImages:
            screen.fill((0,0,0),pygame.Rect(key[0],key[1],100,100))
            pygame.display.update()
    drawGrid(6,800,screen)
    

#-----------------------the main method--------------------#
def main():
       
        screenWidth = 800
        screenHight = 800
        rows = 6
        background_colour = (0,0,0)
    
        screen = pygame.display.set_mode((screenWidth,screenHight))
        pygame.display.set_caption('mentalGame')
        screen.fill(background_colour)
        drawGrid(rows,screenWidth,screen)
        image_positions = {}
        image_positions = loadImages(rows,screenWidth,screen) 
        Scorefont = pygame.font.SysFont('Hack Bold', 25,italic = True)
        textScore = Scorefont.render('Score : ', False, (255, 255, 0))
        screen.blit(textScore,(675,200))
        
        

        turnsResult = Scorefont.render('Turns : ', False, (255, 255, 0))
        screen.blit(turnsResult,(675,250))


        
        clicked_counter = 0
        OpenedImages = []
        Score = 0
        turns=0
        FirstImage = False
        running = True
        pygame.display.flip()
        pygame.display.update()

        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                    mousepos = pygame.mouse.get_pos()
                    clicked_counter+=1

                    if Score == 18:
                        messagebox.showinfo(title='Game Won!', message='You completed the game in '+turns+'Turns')

                    if clicked_counter%2!=0:
                        FirstImage = True
                    else:
                        FirstImage = False
                    
                    if FirstImage:
                        
                        for key_pos,image in image_positions.items(): 
                            if key_pos[0] <= mousepos[0] <= key_pos[0]+100 and key_pos[1] <= mousepos[1] <= key_pos[1]+100:
                                image_loaded = pygame.image.load(image).convert_alpha()
                                screen.blit(image_loaded,key_pos)
                                pygame.display.update()
                                OpenedFirstImage = image
     
                    else:
                        for key_pos,image in image_positions.items(): 
                            
                            if key_pos[0] <= mousepos[0] <= key_pos[0]+100 and key_pos[1] <= mousepos[1] <= key_pos[1]+100:
                                image_loaded = pygame.image.load(image).convert_alpha()
                                screen.blit(image_loaded,key_pos)
                                pygame.display.update()
                                OpenedSecondImage = image
                                turns+=1
                                screen.fill(pygame.Color("black"), (745, 250, 50, 50))
                                turnsResult = Scorefont.render(str(turns), False, (255, 255, 0))
                                screen.blit(turnsResult,(745,250))

                                if OpenedFirstImage == OpenedSecondImage:
                                    time.sleep(0)
                                else:
                                    time.sleep(2)
                                if OpenedFirstImage == OpenedSecondImage:

                                    Score+=1
                                    screen.fill(pygame.Color("black"), (775, 200, 50, 50))
                                    textResult = Scorefont.render(str(Score), False, (255, 255, 0))
                                    screen.blit(textResult,(745,200))
                                    OpenedImages.append(OpenedFirstImage) 
                                    pygame.display.flip()
                                    
                                else:
                                    blackOutScreen(screen,OpenedImages,image_positions)
                        
                           
            
                           
                    pygame.display.update()      

        pygame.quit()            

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()      
pygame.mixer.init()
playGame = initializeMenu()
if(playGame):
    main()
else:
    pygame.quit()   
    