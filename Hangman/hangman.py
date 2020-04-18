## Hangman : Two players:1) WordSetter 2) WordGuesser 
## 			--> setter will set the word guesser will guess the word 
## 			--> with every wrong guess one part of the hangman will be drawn 
## 			--> if the guesser guesses the word with the hangman not hanging
## 			--> he wins otherwise the setter wins


import pygame
from tkinter import *
import random
from sys import *



words_sports = ['athletics','baseball','basketball','bowling','car racing','cycling','football','golf','gymnastics','handball','hang gliding',
'hockey','horse racing','jogging','motorcycle racing','para gliding','polo','rugby','scuba diving','skiing','skin diving',
'snow-boarding','softball','squash','swimming','table tennis','tennis','trackandfield','volleyball']


words_nature = ['Canal','Bridge','Dam','Lighthouse','Island','Bay','Riverbank','Beach','Sea','Ocean','Coast','Ground',
'Dune','Desert','Cliff','Park','Meadow','Jungle','Forest','Glacier','Land','Hill','Field','Grass','Soil','Sea shell','Mushroom',
'Pebble','Rock','Stone','Smoke','Pond','River','Wave','Sky','Water','Tree','Plant','Moss','Flower','Bush','Sand',
'Mud','Stars','Planet','Mine','Path','Road','Tunnel','Volcano','Cave']


Alphabets =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
			'W','X','Y','Z']




def setter():

	rand = []
	rand.append(random.choice(words_sports))
	rand.append(random.choice(words_nature))
	choosenWord = random.choice(rand)

	return choosenWord


def open_alphabets(screen):

	font = pygame.font.SysFont('monaco', 25)
	index = 0
	alphabets_and_centers = {}
	centrex = 60
	centrey = 60 
	spaceBetween = 60
	interval = 1
	radius = 21

	for alphabet in Alphabets:

		
		if interval == 16:
			centrey = 145
			centrex = 160

		pygame.draw.circle(screen,(201, 179, 8),(centrex,centrey),radius)
		newEntry = {(centrex,centrey) : alphabet}
		alphabets_and_centers.update(newEntry)
		alphax = centrex-7
		alphay = centrey-15
		screen.blit(font.render(alphabet, True, (155, 66, 245)), (alphax,alphay))
		
		centrex += spaceBetween
		interval += 1
		index+=1

	pygame.display.update()
	return alphabets_and_centers
		



#mainloop will terminate if the guesser or the setter will win
def game_loop(screen,alphabets_and_centers):

	choosen_word = setter()




	while True:
		for event in pygame.event.get() :
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
			 	mousex,mousey = pygame.mouse.get_pos()

			 	#determine which button has been clicked and find that alphabet in the word

			 	#for entry in alphabets_and_centers:

			 	for pos,alphabet in alphabets_and_centers.items():

						dx = abs(mousex - pos[0])
						dy = abs(mousey - pos[1])

						if dx^2 + dy^2 < 21^2:
							print(alphabet," clicked")
							



			 		
			 		

pygame.init()
display_surface = pygame.display.set_mode(( 1000, 600 ))
display_surface.fill((112, 194, 133))

alphabets = open_alphabets(display_surface)
game_loop(display_surface,alphabets)

