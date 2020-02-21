import pygame
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*



class Pyramid():
	vertices=[(1,0,1),(1,0,-1),(-1,0,-1),(-1,0,1),(0,2,0)]
	edges=[(4,0),(4,1),(4,2),(4,3),(0,3),(1,0),(2,1),(3,2)]
	surfaces=[(4,1,0),(4,3,0),(4,2,3),(4,1,2),(0,1,2,3)]
	def __init__(self):
		self.edges=Pyramid.edges
		self.vertices=Pyramid.vertices
		self.surfaces=Pyramid.surfaces
	def draw(self):
		self.draw_side()
		glLineWidth(2)
		glBegin(GL_LINES)
		for edge in Pyramid.edges:
			for vertex in edge:
				glVertex3fv(Pyramid.vertices[vertex])
				glColor3fv((1,1,1))		
		glEnd()
	def draw_side(self):
		
		glBegin(GL_QUADS)
		for surface in self.surfaces:
			for vertex in surface:
				glVertex3fv(self.vertices[vertex])
				glColor3fv((0,0.1,1))		
		glEnd()


def main():
	pygame.init()
	pygame.display.set_mode((1200,800),DOUBLEBUF|OPENGL)	


	gluPerspective(70,1200/800,0.1,50)#degree view,aspect Ratio,z-near,z-far
	glTranslatef(0.0,-1.5,-8)
	glRotatef(50,100,0,0)
	glEnable(GL_DEPTH_TEST)
	p=Pyramid()
	vel=0.1
	rot=2
	clock=pygame.time.Clock()
	while True:
		clock.tick(120)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
		keys=pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			glTranslatef(0.0,0.0,-vel)			

		if keys[pygame.K_DOWN]:
			glTranslatef(0.0,0.0,+vel)
		if keys[pygame.K_LEFT]:
			glTranslatef(-vel,0.0,0.0)
		if keys[pygame.K_RIGHT]:
			glTranslatef(vel,0.0,0.0)
		if keys[pygame.K_f]:
			glTranslatef(0.0,-vel,0.0)
		if keys[pygame.K_b]:
			glTranslatef(0.0,vel,0.0)	
		if keys[pygame.K_r]:
			glRotatef(-rot,700,0,0)	
		if keys[pygame.K_t]:
			glRotatef(rot,700,0,0)
		if keys[pygame.K_l]:
			glRotatef(rot,0,40,0)
		
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)#refresh opengl display
		p.draw()
		pygame.display.flip()




main()