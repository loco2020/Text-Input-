import pygame,sys
pygame.init()

s_w = 700
s_h = 600

clock = pygame.time.Clock()
win = pygame.display.set_mode((s_w,s_h))
pygame.display.set_caption("Text Input")
font = pygame.font.Font(None,25)

textBox = pygame.Rect(225,150,250,50)
selectBox = 0
text = ''

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
        	x,y = pygame.mouse.get_pos()
        	if textBox.collidepoint(x,y):
        		selectBox = 1

       	if event.type == pygame.KEYDOWN: 
       		if selectBox == 1:
       			if event.key == pygame.K_BACKSPACE:
       				text = text[:-1]
       			else:
       				text += event.unicode
                    
    textSurf = font.render(text,True,(0,0,0))
    win.blit(textSurf,textBox.midleft)
    pygame.draw.rect(win,(15,15,15),textBox,2)
    pygame.display.flip()

    win.fill((230,230,230))


pygame.quit()
