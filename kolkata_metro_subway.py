import pygame
from pygame.locals import*
from OpenGL.GLU import *
from OpenGL.GL import *


vertices=[(4,-2,0),(-4,-2,0 ),(-4,-2,-100),(4,-2,-100),(6,4,0),(-6,4,0),(-6,4,-100),(6,4,-100),]
walls=[(6,4,0),(6,4,-100),(6,-2,-100),(6,-2,0),(-6,4,0),(-6,4,-100),(-6,-2,-100),(-6,-2,0),(-4,-2,-100),(4,-2,-100),(4,4,-100),(-4,4,-100)]
lights=[(-3,4,0),(-3,4,-4),(-3,4,-5),(-3,4,-9),(-3,4,-10),(-3,4,-14),(-3,4,-15),(-3,4,-19),(-3,4,-20),(-3,4,-24),(-3,4,-25),(-3,4,-29),(-3,4,-30),(-3,4,-34),(-3,4,-35),(-3,4,-39),(-3,4,-40),
(-3,4,-44),(-3,4,-45),(-3,4,-49),(-3,4,-50),(-3,4,-54),(-3,4,-55),(-3,4,-59),(-3,4,-60),(-3,4,-64),(-3,4,-65),(-3,4,-69),(-3,4,-70),(-3,4,-74),(-3,4,-75),(-3,4,-79),(-3,4,-80),(-3,4,-84),(-3,4,-85),(-3,4,-89),(-3,4,-90),
(-3,4,-94),(-3,4,-95),(-3,4,-99)]
lights2=[(3,4,0),(3,4,-4),(3,4,-5),(3,4,-9),(3,4,-10),(3,4,-14),(3,4,-15),(3,4,-19),(3,4,-20),(3,4,-24),(3,4,-25),(3,4,-29),(3,4,-30),(3,4,-34),(3,4,-35),(3,4,-39),(3,4,-40),
(3,4,-44),(3,4,-45),(3,4,-49),(3,4,-50),(3,4,-54),(3,4,-55),(3,4,-59),(3,4,-60),(3,4,-64),(3,4,-65),(3,4,-69),(3,4,-70),(3,4,-74),(3,4,-75),(3,4,-79),(3,4,-80),(3,4,-84),(3,4,-85),(3,4,-89),(3,4,-90),
(3,4,-94),(3,4,-95),(3,4,-99)]


ceilings=[(-2,4,0),(2,4,0),(2,4,-10),(-2,4,-10),(-2,4,-12),(2,4,-12),(2,4,-22),(-2,4,-22),(-2,4,-24),(2,4,-24),(2,4,-34),(-2,4,-34),(-2,4,-36),(2,4,-36),(2,4,-46),(-2,4,-46),
(-2,4,-48),(2,4,-48),(2,4,-58),(-2,4,-58),(-2,4,-60),(2,4,-60),(2,4,-70),(-2,4,-70),(-2,4,-72),(2,4,-72),(2,4,-82),(-2,4,-82),(-2,4,-84),(2,4,-84),(2,4,-94),(-2,4,-94),
(-2,4,-96),(2,4,-96),(2,4,-100),(-2,4,-100)]

margins=[(2.8,-2,0),(3.2,-2,0),(3.2,-2,-100),(2.8,-2,-100),(-2.8,-2,0),(-3.2,-2,0),(-3.2,-2,-100),(-2.8,-2,-100),(2.5,-2,0),(-2.5,-2,0),(-2.5,-2,-100),(2.5,-2,-100)]
surfaces=[(0,1,2,3)]
s1=[(4,5,6,7)]
s2=[(0,1,2,3),(4,5,6,7)]
end=[(8,9,10,11)]
s3=[(0,1),(2,3),(4,5),(6,7),(8,9),(10,11),(12,13),(14,15),(16,17),(18,19),(20,21),(22,23),
(24,25),(26,27),(28,29),(30,31),(32,33),(34,35),(36,37),(38,39)]
s4=[(0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15),(16,17,18,19),(20,21,22,23),(24,25,26,27),(28,29,30,31),(32,33,34,35)]
colors=[(0,0,1),(0,1,0),(0,0,0.2),(0.2,0,0),(0.7,0.1,0)]
s5=[(0,1,2,3),(4,5,6,7)]
s6=[(8,9,10,11)]
def base():
	glBegin(GL_QUADS)
	for surface in surfaces:
		glColor3fv(colors[1])
		for vertex in surface:
			glVertex3fv(vertices[vertex])
		

	for s in s1:
		glColor3fv(colors[0])
		for vertex in s:
			glVertex3fv(vertices[vertex])
	for s in s2:
		glColor3fv(colors[2])
		for vertex in s:
			glVertex3fv(walls[vertex])	
	for s in end:
		glColor3fv(colors[3])
		for vertex in s:
			glVertex3fv(walls[vertex])	
	for s in s4:
		glColor3fv(colors[4])
		for vertex in s:
			glVertex3fv(ceilings[vertex])
	for s in s5:
		glColor3fv((1,1,0))
		for vertex in s:
			glVertex3fv(margins[vertex])	

	for s in s6:
		glColor3fv((0.2,0.6,0))
		for vertex in s:
			glVertex3fv(margins[vertex])								
	glEnd()	
	glLineWidth(10)	
	glBegin(GL_LINES)		
	for s in s3:
		glColor3fv((1,1,1))
		for vertex in s:
			
			glVertex3fv(lights[vertex])	
	for s in s3:
		glColor3fv((1,1,1))
		for vertex in s:
			
			glVertex3fv(lights2[vertex])										
	
	glEnd()
def main():
	pygame.init()
	pygame.display.set_mode((1200,600),DOUBLEBUF|OPENGL)
	gluPerspective(45,0.8,0.08,150)
	glTranslatef(0,-2,-6)
	glRotatef(0,0,0,0)
	clock=pygame.time.Clock()
	while True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()	
		turn=2
		keys=pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			glTranslatef(0,0,turn/2)
		if keys[pygame.K_DOWN]:
			glTranslatef(0,0,-turn/2)
		if keys[pygame.K_LEFT]:
			glRotatef(0.1,0,-turn,0)
		if keys[pygame.K_RIGHT]:
			glRotatef(0.1,0,turn,0)				
				

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		base()
		pygame.display.flip()		


main()