import pygame
from pygame.locals import *
from OpenGL.GL import*
from OpenGL.GLU import*

vertices=[

(1,1,0),(1,-1,0),(0,1,1),(0,-1,1),(-1,1,0),(-1,-1,0),
(1,0.8,-1),(1,-0.8,-1),(-1,0.8,-1),(-1,-0.8,-1),(0,0.8,1),(0,-0.8,1),
(1,0.8,0),(1,-0.8,0),(-1,0.8,0),(-1,-0.8,0)


]
edges=[

(0,1),(0,2),(2,3),(1,3),(3,5),(4,2),(4,5),(10,12),(12,6),(6,8),(8,14),(14,10),(13,7),(7,9),(9,15),(15,11),(11,13),(7,9),(9,8),(8,6),(6,7)
]

surfaces1=[


(0,1,3,2),(2,3,5,4),(10,12,14),(6,8,14,12),(11,13,15),(7,9,15,13),(7,6,12,13),(9,15,14,8),(6,7,9,8),(7,9,8)

]

colors=[
(1,0,0),(0,1,0),(0,0,1),(1,1,0)
]

def hut():
	x=0
	glBegin(GL_QUADS)
	for s in surfaces1:
		glColor3fv(colors[x])
		x+=1
		if x==4:
			x=0


		for v in s:
			glVertex3fv(vertices[v])

	glEnd()		

	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv((0,1,1))	

	glEnd()		


def main():
	pygame.init()
	pygame.display.set_mode((800,600),DOUBLEBUF|OPENGL)
	gluPerspective(45,800/600, 0.1,50.0)
	glTranslatef(0.0,0.0,-4)
	glRotatef(270,270,0,0)
	glRotatef(30,0,0,-70)
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
		
		glRotatef(1,0,0,1)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)	

		hut()
		pygame.display.flip()
		pygame.time.wait(10)
main()				