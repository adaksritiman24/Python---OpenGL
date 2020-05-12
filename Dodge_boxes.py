import pygame

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import numpy as np


class Cube:
	def __init__(self):
		self.origin_vertices = np.array([
		[1,-1,-1],
		[1,1,-1],
		[-1,1,-1],
		[-1,-1,-1],
		[1,-1,1],
		[1,1,1],
		[-1,1,1],
		[-1,-1,1],
		])
		self.vertices = np.array([
		[1,-1,-1],
		[1,1,-1],
		[-1,1,-1],
		[-1,-1,-1],
		[1,-1,1],
		[1,1,1],
		[-1,1,1],
		[-1,-1,1],
		])
		self.edges =(
		(0,1),
		(0,3),
		(0,4),
		(3,2),
		(2,1),
		(1,5),
		(3,7),
		(2,6),
		(4,7),
		(4,5),
		(7,6),
		(6,5),
		)
		self.surfaces=(
		(0,1,5,4),
		(0,3,2,1),
		(0,3,7,4),
		(6,7,5,4),
		(6,2,3,7),
		(6,2,1,5),

		)
		self.x = random.randint(-10, 10)
		self.y = random.randint(-10,10)
		self.z = random.randint(-20,60)
		self.color =random.choice([(0,1,0),(1,0,1),(1,0,0),(0.5,0.5,0.5),(0,0,1),(1,1,1)])
		self.random_pos()
		self.speed = random.randint(1,3)
	def random_pos(self):
		for i in range(len(self.vertices)):
			self.vertices[i][0] = self.vertices[i][0] + self.x 
		for i in range(len(self.vertices)):
			self.vertices[i][1] = self.vertices[i][1] + self.x
		for i in range(len(self.vertices)):
			self.vertices[i][2] = self.vertices[i][2] + self.x	

	def initialize(self):
		glBegin(GL_QUADS)
		for surface in self.surfaces:
			glColor3fv(self.color)
			for vertex in surface:
				glVertex3fv(self.vertices[vertex])

		glEnd()

		glBegin(GL_LINES)
		for edge in self.edges:
			glColor3fv((1,1,1))
			for vertex in edge:
				glVertex3fv(self.vertices[vertex])

		glEnd()
	def move(self):
		for i in range(len(self.vertices)):
			self.vertices[i][2] = self.vertices[i][2] + self.speed

		if self.vertices[0][2] >= 100:
			self.x = random.randint(-10,10)
			self.z = random.randint(-20,60)
			self.y = random.randint(-10,10)
			self.vertices = np.array([
			[1+self.x,-1+self.y,-1+self.z],
			[1+self.x,1+self.y,-1+self.z],
			[-1+self.x,1+self.y,-1+self.z],
			[-1+self.x,-1+self.y,-1+self.z],
			[1+self.x,-1+self.y,1+self.z],
			[1+self.x,1+self.y,1+self.z],
			[-1+self.x,1+self.y,1+self.z],
			[-1+self.x,-1+self.y,1+self.z],
			])
m=0
n=0
def left():
	global m
	if m<20:
		glTranslatef(0.3,0.0,0)
		m= m+1

def right():
	global m
	if  m>-20:
		glTranslatef(-0.3,0.0,0)
		m= m-1

def up():
	global n
	if n<20:
		glTranslatef(0.0,-.2,0.0)
		n = n+1

def down():
	global n
	if n>-20:
		glTranslatef(0.0,.2,0)	
		n= n-1	

def main():
	clock =pygame.time.Clock()
	cubes = []
	for i in range(30):
		cubes.append(Cube())
	pygame.init()
	display =(1200,900)
	pygame.display.set_mode(display,DOUBLEBUF|OPENGL)

	gluPerspective(45, (display[0]/display[1]),0.1,200)
	glTranslatef(0.0,0.0,-100)

	glRotatef(0,0,0,0)

	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
		keys= pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			left()
		if keys[pygame.K_RIGHT]:
			right()	
		if keys[pygame.K_UP]:
			up()
		if keys[pygame.K_DOWN]:
			down()			
				
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)	

		for cube in cubes:
			cube.initialize()
			cube.move()
		pygame.display.flip()
		pygame.time.wait(1)

main()		
