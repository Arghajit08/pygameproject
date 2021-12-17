#Creating GameWindow
import pygame
pygame.mixer.init()
pygame.mixer.music.load
pygame.init()
gameWindow=pygame.display.set_mode((600,600))
pygame.display.set_caption("Reach Me If You Can")
normal=(0,0,0)
bot=(255,0,0)

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,35)
def text(text,color,x,y):
	screen_text=font.render(text,True,color)
	gameWindow.blit(screen_text,(x,y))
#Creating Maze
def rec(x,y,color,normal,bot,gameWindow):
	if(x==300):
		pygame.draw.rect(gameWindow,bot,pygame.Rect(x-10,y+10,10,10))
	else:
		for i in range(x,y+1,10):
			pygame.draw.rect(gameWindow,color,pygame.Rect(x,i,10,10))
			pygame.draw.rect(gameWindow,color,pygame.Rect(y,i,10,10))
			pygame.draw.rect(gameWindow,color,pygame.Rect(i,x,10,10))
			pygame.draw.rect(gameWindow,color,pygame.Rect(i,y,10,10))
			pygame.draw.rect(gameWindow,normal,pygame.Rect(y-10,y,10,10))
		if(x!=280):
			pygame.draw.rect(gameWindow,color,pygame.Rect(y-20,y-10,10,10))
		x+=20
		y-=20
		rec(x,y,color,normal,bot,gameWindow)
def home(gameWindow,bot,normal):
	exit=False
	while not exit:
		gameWindow.fill(normal)
		text("REACH ME IF YOU CAN",bot,150,250)
		text("PRESS SPACE BAR TO PLAY",bot,130,280)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_SPACE:
					GameLoop()
		pygame.display.update()
		clock.tick(60)
#Creating Game Loop
def GameLoop():
	#Creating Gamespecific Part
	exit=False
	gameover=False
	posx=580
	posy=590
	fps=30
	velx=0
	vely=0

	#Creating Colour
	color=(135,245,44)
	normal=(0,0,0)
	bot=(255,0,0)
	white=(255,255,255)
	a=0
	b=0
	c=0
	d=0
	x=[]
	y=[]
	z=[]
	k=[]
	po=[]
	mo=[]
	xo=[]
	fo=[]
	mod=10
	sod=580
	tod=560
	for i in range(0,20):
		por=20
		if mod==300 or sod==300:
			break
		else:
			x.append((mod,sod))
			mo.append((mod,sod+10))
			y.append((mod,mod))
			po.append((mod-10,mod))
			z.append((sod,mod))
			xo.append((sod,mod-10))
			mod+=por
			sod-=por
	sod=580
	for i in range(0,20):
		if sod==300 or tod==300:
			break
		else:
			k.append((tod,sod))
			fo.append((tod+10,sod))
			tod-=20
			sod-=20
	k.append((580,590))


	gameover=False
	while not exit:
		a=0
		b=0
		c=0
		d=0
		#Erasing previous position
		gameWindow.fill(normal)
		#KeyHandling
		for i in pygame.event.get(): #All Events
			if i.type == pygame.QUIT:
				exit=True
			if i.type == pygame.KEYDOWN:
				if i.key == pygame.K_RIGHT:
					posx+=0
					m=posy
					velx=10
					vely=0
					a+=1
					b=0
					c=0
					d=0
				if i.key == pygame.K_LEFT:
					posx-=0
					m=posy
					velx=-10
					vely=0
					b+=1
					a=0
					c=0
					d=0
				if i.key == pygame.K_UP:
					posy-=0
					n=posx
					vely=-10
					velx=0
					c+=1#it is getting updated due to display.update
					a=0
					b=0
					d=0
				if i.key == pygame.K_DOWN:
					posy+=0
					n=posx
					vely=10
					velx=0
					d+=1
					a=0
					b=0
					c=0
		rec(0,590,color,normal,bot,gameWindow)
		if(a==1): #and #(posx in :#and update position is the corner position or not if not exit true for all
			if(posx,posy) not in x:
				gameover=True
		if(b==1):
			if(posx,posy) not in z:
				gameover=True
		if(c==1):
			if(posx,posy) not in k:
				gameover=True
		if(d==1):
			if(posx,posy) not in y:#now we have to correctly update a,b,c,d using display update or loop
				gameover=True
		if((posx,posy) in xo) or ((posx,posy) in mo) or ((posx,posy) in po) or ((posx,posy) in fo):
			gameover=True
		posx+=velx
		posy+=vely
		pygame.draw.rect(gameWindow,bot,(posx,posy,10,10))
		if gameover==True:
			gameWindow.fill(white)
			text("COULDN'T REACH ME!!",bot,150,250)
			text("RESTART",bot,220,310)
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					exit==True
				elif event.type==pygame.KEYDOWN:
					if event.key==pygame.K_SPACE:
						home(gameWindow,bot,normal)
				else:
					pass
		if gameover==False and (posx,posy)==(290,300):
			gameWindow.fill(white)
			text("FINALLY U REACHED ME!!",bot,150,300)
		pygame.display.update()
		clock.tick(fps)
home(gameWindow,bot,normal)
#Creating Exit Part
pygame.quit()
quit()