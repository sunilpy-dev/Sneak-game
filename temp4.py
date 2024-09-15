import pygame
import random
import time
pygame.init()


fps=60
#Color
white=(255,255,255) #Here we have to define the color before to use it and color takes the three value from 0 to 255 and it has RGB light which is considered for 0 to no colour and 255 for full color 
red=(255,0,0)
black=(0,0,0)
grey=(100,100,100)
darkgrey=(85,85,85)
yellow=(255,255,0 )
darkblue=(17,17,132)

screen_width=900
screen_height=600

#game interface
image = pygame.image.load('snake.jpg')
def Background_snake(image):
    size = pygame.transform.scale(image, (screen_width, screen_height))
    gamewindow.blit(size, (0, 0))

#Game ending
image1 = pygame.image.load('gameover.jpg')
def Game_over(image1):
    size = pygame.transform.scale(image1, (screen_width, screen_height))
    gamewindow.blit(size, (0, 0))



# Game loop variable
velocity=4
endindex=3
k=2
gamewindowminx=20
gamewindowmaxx=screen_width
gamewindowminy=50
gamewindowmaxy=screen_height



#Craeting game window
pygame.display.set_caption("SnakeswithSunil")
gamewindow=pygame.display.set_mode((screen_width,screen_height))

pygame.display.update()
clock=pygame.time.Clock() #it implement the time in the pygame


def plot_snake(gamewindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])

#Game fonts
font=pygame.font.SysFont(None,40) #here the first argument is font type and none means system font and second is font size
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)#here the first argument is what text we have to print on screen and second is antialiasing which used when size of screen get changes the it autoadjust and third is color whivch we have to used
    gamewindow.blit(screen_text,[x,y]) #Here the .blit is used to update the game window folowed by content and position


font1=pygame.font.SysFont(None,50) #here the first argument is font type and none means system font and second is font size
def text_screen1(text,color,x,y):
    screen_text=font1.render(text,True,color)#here the first argument is what text we have to print on screen and second is antialiasing which used when size of screen get changes the it autoadjust and third is color whivch we have to used
    gamewindow.blit(screen_text,[x,y]) #Here the .blit is used to update the game window folowed by content and position


font2=pygame.font.SysFont(None,22) #here the first argument is font type and none means system font and second is font size
def text_screen2(text,color,x,y):
    screen_text=font2.render(text,True,color)#here the first argument is what text we have to print on screen and second is antialiasing which used when size of screen get changes the it autoadjust and third is color whivch we have to used
    gamewindow.blit(screen_text,[x,y]) #Here the .blit is used to update the game window folowed by content and position


def life(lifcol,i,j1):
    posx=screen_width-150
    posy=-2
    # rect=(20,30)
    # rect1=(30,30)
    a=[0,30,60]
    while(i<j1):
        pygame.draw.circle(gamewindow,lifcol,(posx+20+a[i],posy+30),7,0,True,True,False,False,)
        pygame.draw.polygon(gamewindow,lifcol,((posx+13+a[i],posy+30),(posx+27+a[i],posy+42),(posx+41+a[i],posy+30)))
        pygame.draw.circle(gamewindow,lifcol,(posx+34+a[i],posy+30),7,0,True,True,False,False,)
        i=i+1
 

def welcome():
    pygame.mixer.music.set_volume(.3)
    pygame.mixer.music.load('background music.mp3') #here we have just loaded the music
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(.3)
    game_exit=False
    while (not game_exit):
        Background_snake(image)

        #polygon drawn
        pygame.draw.rect(gamewindow,black,(240,420,screen_width-550,screen_height-450))
        pygame.draw.polygon(gamewindow,yellow,((370+10,290-10),(370+10,370-10),(440+10,325-10)))
        pygame.draw.polygon(gamewindow,(1,190,10),((380+10,295-10),(380+10,363-10),(440+10,325-10)))

        #boundary drawn
        pygame.draw.line(gamewindow,black,(370+10,290-10),(370+10,370-10))
        pygame.draw.line(gamewindow,black,(440+10,325-10),(370+10,370-10))
        pygame.draw.line(gamewindow,black,(440+10,325-10),(370+10,290-10))

        #inside playbutton
        pygame.draw.line(gamewindow,black,(380+10,295-10),(380+10,363-10))

        #texarea
        pygame.draw.line(gamewindow,white,(240,420),(240,420+screen_height-450),width=2)
        pygame.draw.line(gamewindow,white,(240,420),(240+screen_width-550,420),width=2)
        pygame.draw.line(gamewindow,white,(240+screen_width-550,420),(240+screen_width-550,420+screen_height-450),width=2)
        pygame.draw.line(gamewindow,white,(240+screen_width-550,420+screen_height-450),(240,420+screen_height-450),width=2)

        #polygon text
        text_screen2(" 1. You Have Only 3 Lives To Create Highscore",white,int(screen_width/2-(len("Welcome to Snake Game")*20)/2)+10,int(screen_height/1.3-55/2))
        text_screen2(" 2. Each Collision Cost You One LIFE",white,int(screen_width/2-(len("Welcome to Snake Game")*20)/2)+10,int(screen_height/1.23-55/2))
        # text_screen2("     LIFE",white,int(screen_width/2-(len("Welcome to Snake Game")*20)/2)+10,int(screen_height/1.14-55/2))
        text_screen2(" 3. After Collision Game Restart Till Last Life",white,int(screen_width/2-(len("Welcome to Snake Game")*20)/2)+10,int(screen_height/1.17-55/2))
        text_screen2("     And Speed Get's Increased",white,int(screen_width/2-(len("Welcome to Snake Game")*20)/2)+10,int(screen_height/1.12-55/2))
        text_screen2(" 4. On Each 100 Score Speed Get's Increas",white,int(screen_width/2-(len("Welcome to Snake Game")*20)/2)+10,int(screen_height/1.07-55/2))
        text_screen2("-----------------------BEST OF LUCK----------------------",yellow,int(screen_width/2-(len("Welcome to Snake Game")*20)/2)+10,int(screen_height/1.03-55/2))


        text_screen1("Welcome to Snakes",black,int(screen_width/2-(len("Welcome to Snake Game")*20)/2)+10,int(screen_height/2.36-55/2))
        text_screen1("PLAY",black,int(screen_width/1.6-(len("Welcome to Snake Game")*20)/2)+10,int(screen_height/1.48-55/2))
        # text_screen("Press Space bar to PLAY",black,int(screen_width/2-(len("Press Space bar to PLAY")*20)/2),int(screen_height/2-55/2)+40)
        mousex,mousey=pygame.mouse.get_pos()# it give me the exact postion of the mouse


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_exit=True
            if(mousex>380 and mousey>280):
                keypressed=pygame.mouse.get_pressed() #it checked that if the mouse courser is clicked or not
                if keypressed[0]: #here i have been checked it with the left key pressing
                    pygame.mixer.music.stop()
                    game_loop(velocity,endindex,k,gamewindowminx,gamewindowmaxx,gamewindowminy,gamewindowmaxy) #here we have provided that if the space bar is taped then run game loop

        pygame.display.update()
        clock.tick(fps)


#Game loop
def game_loop(velocity,endindex,k,gamewindowminx,gamewindowmaxx,gamewindowminy,gamewindowmaxy):
    with open('higscore.txt','r') as f:
        highscore=f.read()

    #Game variable
    game_exit=False
    game_quit=False
    snake_x=45
    snake_y=60
    score=0
    flag=0
    # velocity_x=5
    # velocity_y=5
    velocity_x=0 #First we set the velocity to zero so that it will only add when user press any key
    velocity_y=0
    food_x=random.randint(60,int(screen_width/2))
    food_y=random.randint(70,int(screen_height/2)) #To amke our food to be plotted between the screen and do not go on the edges so we have changed the tata
    snake_size=20
    init_velocity=velocity
    snake_length=1
    snake_list=[]
    
    while not game_exit:

        if(game_quit):
            with open('higscore.txt','w') as f:
                f.write(str(highscore)) #we use it to fetch the highscore data

            # gamewindow.fill(white)
            Game_over(image1)
            # pygame.mixer.music.set_volume(1)
            # pygame.mixer.music.load('oversoundmp3.mp3') #here we have just loaded the music
            # pygame.mixer.music.play()
            # pygame.mixer.music.set_volume(1)
            text_screen("Press Enter to continue",white,int(screen_width/1.4-(len("Game Over! Press Enter to continue")*20)/2),int(screen_height/1.1-55/2)) #Now here it would not directly respond to the screen due to imidiate running of next code below it which is code for gameplay
            #to make that if we cut the window to close it we have to also intialize the exit poin code here
            for event in pygame.event.get(): #It handel the events that happen throgh the mouse and the keyboard
                if event.type==pygame.QUIT: #It simply make the quit button to be work and it help to get exit
                    game_exit=True

                #Now to make game to be available again to play we have to give keydown code here
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN: #It make the game to be run again if we enter the enter
                        welcome() #here we have provided that if w enter the enter the it will run the welcome function
            

        else: #Now here we have wriiten that else condition so it will only execute if the upeer case is false
            for event in pygame.event.get(): #It handel the events that happen throgh the mouse and the keyboard
                if event.type==pygame.QUIT: #It simply make the quit button to be work and it help to get exit
                    game_exit=True

                if event.type==pygame.KEYDOWN:
                    if(flag==1):
                        velocity=velocity+0.2
                        init_velocity=velocity
                        flag=0

                    #right movemnet
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity #It make our object to move in the screen by that much amount we have added on each press
                        velocity_y=0

                    if event.key==pygame.K_d:
                        velocity_x=init_velocity #It make our object to move in the screen by that much amount we have added on each press
                        velocity_y=0
                    
                    #left movement
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity #Here we have set the velocity to change when user presses any key but here also an error due to velocity in y is not define so in terms of pressing these keys it will move diagonaly
                        velocity_y=0

                    if event.key==pygame.K_a:
                        velocity_x=-init_velocity #Here we have set the velocity to change when user presses any key but here also an error due to velocity in y is not define so in terms of pressing these keys it will move diagonaly
                        velocity_y=0
                        
                    #Down movement
                    if event.key==pygame.K_DOWN: #Here in pygame if you want to move your subject up then - the value from your position
                        velocity_y=init_velocity
                        velocity_x=0 #It will make the y direction velocity zero so that it will move only in one direction

                    if event.key==pygame.K_s: #Here in pygame if you want to move your subject up then - the value from your position
                        velocity_y=init_velocity
                        velocity_x=0 #It will make the y direction velocity zero so that it will move only in one direction

                    #Up movement
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0

                    if event.key==pygame.K_w:
                        velocity_y=-init_velocity
                        velocity_x=0
                    # print(init_velocity)

                    # if event.key==pygame.K_q: #Its a cheat code to beat score by pressing the q key in keyboard
                    #     score+=10

            snake_x+=velocity_x
            snake_y+=velocity_y
            #To amke game smooth put as less thing in less possible
            if abs(snake_x-food_x)<17 and abs(snake_y-food_y)<17 :
                score+=10
                pygame.mixer.music.load('sneakeatmp3.mp3') #here we have just loaded the music
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1.2)
                if(score%100==0 and score!=0):
                    flag=1
                else:
                    flag=0
                # print("Score: ",score*10)
                # text_screen("Score: "+str(score*10),red,5,5) #Here we have given all three argument to our textscreen function first is string which is main contenet and second is color and third is x,y but due to we have filled the screen with the white after it we have to move this below it
                snake_length+=2 #Here it is refer for the cordinats
                food_x=random.randint(60,int(screen_width-40))
                food_y=random.randint(100,int(screen_height-40))
                if score>int(highscore):
                    highscore=score #here we changed the higscore when our score is greater then the highscore

            gamewindow.fill(black)
            pygame.draw.rect(gamewindow,grey,[0,0,screen_width,50])
            pygame.draw.rect(gamewindow,grey,[0,0,20,screen_height])
            pygame.draw.rect(gamewindow,grey,[screen_width-20,0,screen_width,screen_height]) 
            pygame.draw.rect(gamewindow,grey,[0,screen_height-20,screen_width,20])
            text_screen("Life:",white,screen_width-202,15)
            life(red,0,endindex)
            text_screen("Score: "+str(score) + "   HighScore: "+str(highscore),yellow,30,15) #and dispalyed here the highscore
            pygame.draw.rect(gamewindow,red,[food_x,food_y,int(snake_size)/1.3,int(snake_size)/1.3]) #We are creating this at the screen time


            head=[] #Here we are giving the intials for the head of snake
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head) #Here we have given the empty list a initial thing for the head position

            if len(snake_list)>snake_length:
                del snake_list[0] #It checks for the that if our list length exceeded the snake lenght then it will automaticaly delete the first one head

            if(head in snake_list[:-1]):
                pygame.mixer.music.set_volume(.2)
                pygame.mixer.music.load('crashmp3.mp3') #here we have just loaded the music
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(.2)
                col=[darkgrey,(211,211,211,2),(106,137,167,2),darkblue]
                j=0
                life(grey,k,endindex)
                while(j<3):
                    gamewindow.fill(col[random.randint(0,3)])
                    pygame.draw.rect(gamewindow,grey,[0,0,screen_width,50])
                    pygame.draw.rect(gamewindow,grey,[0,0,20,screen_height])
                    pygame.draw.rect(gamewindow,grey,[screen_width-20,0,screen_width,screen_height]) 
                    pygame.draw.rect(gamewindow,grey,[0,screen_height-20,screen_width,20])
                    plot_snake(gamewindow,white,snake_list,snake_size)
                    pygame.draw.rect(gamewindow,red,[food_x,food_y,int(snake_size)/1.3,int(snake_size)/1.3])
                    text_screen("Life:",white,screen_width-202,15)
                    life(red,0,endindex-1)
                    text_screen("Score: "+str(score) + "   HighScore: "+str(highscore),yellow,30,15)
                    pygame.display.update()
                    time.sleep(.08)
                    j+=1
                k=k-1
                endindex-=1
                if(k<0):
                    game_quit=True
                else:
                    gamewindowminx+=1
                    gamewindowmaxx-=1
                    gamewindowminy-=1
                    gamewindowmaxy-=1
                    with open('higscore.txt','w') as f:
                        f.write(str(highscore))
                    game_loop(velocity+1,endindex,k,gamewindowminx,gamewindowmaxx,gamewindowminy,gamewindowmaxy)

            if(snake_x<=gamewindowminx or snake_x>=(gamewindowmaxx-40) or snake_y<=gamewindowminy or snake_y>=(gamewindowmaxy-40)):
                pygame.mixer.music.set_volume(.2)
                pygame.mixer.music.load('crashmp3.mp3') #here we have just loaded the music
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(.2)
                # pygame.mixer.music.load('healthlessmp3.mp3') #here we have just loaded the music
                # pygame.mixer.music.play()
                col=[darkgrey,(211,211,211,2),(106,137,167,2),darkblue]
                j=0
                life(grey,k,endindex)
                while(j<3):
                    gamewindow.fill(col[random.randint(0,3)])
                    pygame.draw.rect(gamewindow,grey,[0,0,screen_width,50])
                    pygame.draw.rect(gamewindow,grey,[0,0,20,screen_height])
                    pygame.draw.rect(gamewindow,grey,[screen_width-20,0,screen_width,screen_height]) 
                    pygame.draw.rect(gamewindow,grey,[0,screen_height-20,screen_width,20])
                    plot_snake(gamewindow,white,snake_list,snake_size)
                    pygame.draw.rect(gamewindow,red,[food_x,food_y,int(snake_size)/1.3,int(snake_size)/1.3])
                    text_screen("Life:",white,screen_width-202,15)
                    life(red,0,endindex-1)
                    text_screen("Score: "+str(score) + "   HighScore: "+str(highscore),yellow,30,15)
                    pygame.display.update()
                    time.sleep(0.08)
                    j+=1
                k=k-1
                endindex-=1
                if(k<0):
                    game_quit=True
                    pygame.mixer.music.set_volume(1)
                    pygame.mixer.music.load('oversoundmp3.mp3') #here we have just loaded the music
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(1)
                else:
                    gamewindowminx+=1
                    gamewindowmaxx-=1
                    gamewindowminy-=1
                    gamewindowmaxy-=1
                    with open('higscore.txt','w') as f:
                        f.write(str(highscore))
                    game_loop(velocity+1,endindex,k,gamewindowminx,gamewindowmaxx,gamewindowminy,gamewindowmaxy)
                # print("Game Over") #We have remove to make our game less proccessing on faltu work

            # pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size]) #Here the arguments are passed like surface,color,list of position in x,in y,rectangle width,height
            plot_snake(gamewindow,white,snake_list,snake_size) #by this function we can create the snake body dynamicaly
        pygame.display.update() #For each time with changes in the window or loop in pygame we need to handel it by updating it


        clock.tick(fps) #The fps here decides how fast your game gonna respond

    pygame.quit() #It simply quit the game when exit happen 
    quit()
welcome() #Here we have settel the welcome screen to be dispaly first
# game_loop()