#Justin Jim
#Bomberman
from pygame import*
from random import*
import pprint
size = width, height = 525,455
screen = display.set_mode(size)
menupic2 = 1
menupicdelay = 0
menupicycoord = 380
option = 'play'
currentscreen = 'menu'
menu = True
running = True
timeuntildoom = 0
doomflag16 = False
doomflag15 = False
doomflag14 = False           
doomflag13 = False
doomflag12 = False
doomflag11 = False
doomflag10 = False
doomflag9 = False
doomflag8 = False
doomflag7 = False
doomflag6 = False
doomflag5 = False
doomflag4 = False       
doomflag3 = False
doomflag2 = False
doomflag1 = True
doomy,doomx = 1,1
doomcounter = 0    
brickx,bricky = 35,35
playingtime = 0
#All my variables that deal with the players
everything = []
aa = 35
bb = 35
aa2 = 35
newx = 1
newy = 1
switch = 0
count1 = 0
count2 = 0
bombon = 0
movingflag2 = False
movingflag3 = False
bombcounter = 0
myClock = time.Clock()
bombdown = 0
explosion = 0
moveable = True
movewaiting = 0
moving = False
movingup = False
movingright = False
movingleft = False
movingdown = False
movingcounter = 7
bombframe = 0
rightexplosion = False
leftexplosion = False
upexplosion = False
downexplosion = False
rightexplosion1 = False
leftexplosion1 = False
upexplosion1 = False
downexplosion1 = False
rightexplosion2 = False
leftexplosion2 = False
upexplosion2 = False
downexplosion2 = False
rightexplosion3 = False
leftexplosion3 = False
upexplosion3 = False
downexplosion3 = False
alive = True
deathcounter = 0
bombon1 = 0
movecounter = 0
playerpic1 = 3
playerpic2 = 0
bombinglist = [0,0,0]
bombgridy = 0
bombgridx = 0
aieverything = []
aibombframe1 = 0
aibombcounter1 = 0
aiup1 = False
aidown1 = False
aileft1 = False
airight1 = False
aiup2 = False
aidown2 = False
aileft2 = False
airight2 = False
aiup3 = False
aidown3 = False
aileft3 = False
airight3 = False
movingflag = False
aideathcounter1 = 0
aideathcounter2 = 0
aideathcounter3 = 0
aialive1 = True
aialive2 = True
aialive3 = True
aibombframe2 = 0
aibombcounter2 = 0
aibombframe3 = 0
aibombcounter3 = 0
aibomber1 = 0
aibomber2 = 0
aibomber3 = 0
aibombon1 = 0
aibombon2 = 0
aibombon3 = 0
aibombposx1 = 0
aibombposy1 = 0
aibomby1 = 0 
aibombx1 = 0
aibombposx2 = 0
aibombposy2 = 0
aibomby2 = 0 
aibombx2 = 0
aibombposx3 = 0
aibombposy3 = 0
aibomby3 = 0 
aibombx3 = 0
aiy1 = 11
aix1 = 1
aiy2 = 11
aix2 = 13
aiy3 = 1
aix3 = 13
aicounter1 = 0
aicounter2 = 0
aicounter3 = 0
bb2 = 385
aa3 = 455
bb3 = 385
aa4 = 455
bb4 = 35
redpic1 = 3
redpic2 = 0
bluepic1 = 3
bluepic2 = 0
blackpic1 = 3
blackpic2 = 0
red = 1
blue = 2
black = 3
deathpic = 0
aideathpic1 = 0
aideathpic2 = 0
aideathpic3 = 0
randommovelist1 = []
init()
#Loading all the pictures and one song

lose = image.load("YOU LOSE.png")
win = image.load("YOU WIN.png")
backgroundpic = image.load("backgroundmenu2.bmp")
stillup = image.load("up1.PNG")
moveup1 = image.load("up2.PNG")
moveup2 = image.load("up3.png")
stillright = image.load("right1.png")
moveright1 = image.load("right2.png")
moveright2 = image.load("right3.png")
stillleft = image.load("left1.PNG")
moveleft1 = image.load("left2.PNG")
moveleft2 = image.load("left3.PNG")
stilldown = image.load("down1.PNG")
movedown1 = image.load("down2.PNG")
movedown2 = image.load("down3.png")
bomb1 = image.load("bomb1.bmp")
bomb2 = image.load("bomb2.bmp")
brick = image.load("brickwall.bmp")
brickhoriz = image.load("brickwallhoriz.bmp")
brickvert = image.load("brickwallvert.bmp")
bricktopleft = image.load("brickwalltopleft.bmp")
bricktopright = image.load("brickwalltopright.bmp")
brickbottomleft = image.load("brickwallbottomleft.bmp")
brickbottomright = image.load("brickwallbottomright.bmp")
crate = image.load("boxsprite.bmp")
explosionup = image.load("explosion2.PNG")
explosiondown = image.load("explosion1.bmp")
explosionright = image.load("explosion3.PNG")
explosionleft = image.load("explosion4.PNG")
explosionup2 = image.load("explosion22.bmp")
explosiondown2 = image.load("explosion11.bmp")
explosionright2 = image.load("explosion33.bmp")
explosionleft2 = image.load("explosion44.bmp")
explosionup3 = image.load("explosion222.bmp")
explosiondown3 = image.load("explosion111.bmp")
explosionright3 = image.load("explosion333.bmp")
explosionleft3 = image.load("explosion444.bmp")
blackdown1 = image.load("blackdown1.PNG")
blackdown2 = image.load("blackdown2.PNG")
blackdown3 = image.load("blackdown3.PNG")
blackup1 = image.load("blackup1.PNG")
blackup2 = image.load("blackup2.PNG")
blackup3 = image.load("blackup3.PNG")
blackleft1 = image.load("blackleft1.PNG")
blackleft2 = image.load("blackleft2.PNG")
blackleft3 = image.load("blackleft3.PNG")
blackright1 = image.load("blackright1.PNG")
blackright2 = image.load("blackright2.PNG")
blackright3 = image.load("blackright3.PNG")
reddown1 = image.load("reddown1.PNG")
reddown2 = image.load("reddown2.PNG")
reddown3 = image.load("reddown3.PNG")
redup1 = image.load("redup1.PNG")
redup2 = image.load("redup2.PNG")
redup3 = image.load("redup3.PNG")
redleft1 = image.load("redleft1.PNG")
redleft2 = image.load("redleft2.PNG")
redleft3 = image.load("redleft3.PNG")
redright1 = image.load("redright1.PNG")
redright2 = image.load("redright2.PNG")
redright3 = image.load("redright3.PNG")
bluedown1 = image.load("bluedown1.PNG")
bluedown2 = image.load("bluedown2.PNG")
bluedown3 = image.load("bluedown3.PNG")
blueup1 = image.load("blueup1.PNG")
blueup2 = image.load("blueup2.PNG")
blueup3 = image.load("blueup3.PNG")
blueleft1 = image.load("blueleft1.PNG")
blueleft2 = image.load("blueleft2.PNG")
blueleft3 = image.load("blueleft3.PNG")
blueright1 = image.load("blueright1.PNG")
blueright2 = image.load("blueright2.PNG")
blueright3 = image.load("blueright3.PNG")
death1 = image.load("death1.PNG")
death2 = image.load("death2.PNG")
death3 = image.load("death3.PNG")
reddeath1 = image.load("reddeath1.PNG")
reddeath2 = image.load("reddeath2.PNG")
reddeath3 = image.load("reddeath3.PNG")
bluedeath1 = image.load("bluedeath1.PNG")
bluedeath2 = image.load("bluedeath2.PNG")
bluedeath3 = image.load("bluedeath3.PNG")
blackdeath1 = image.load("blackdeath1.PNG")
blackdeath2 = image.load("blackdeath2.PNG")
blackdeath3 = image.load("blackdeath3.PNG")
instruction = image.load("instructions.bmp")

#Sprite lists and removing the green background in some indivisual explosion pictures
redmoves = [[redup1,redup2,redup3],[redright1,redright2,redright3],[redleft1,redleft2,redleft3],[reddown1,reddown2,reddown3],[reddeath1,reddeath2,reddeath3]]
bluemoves = [[blueup1,blueup2,blueup3],[blueright1,blueright2,blueright3],[blueleft1,blueleft2,blueleft3],[bluedown1,bluedown2,bluedown3],[bluedeath1,bluedeath2,bluedeath3]]
blackmoves = [[blackup1,blackup2,blackup3],[blackright1,blackright2,blackright3],[blackleft1,blackleft2,blackleft3],[blackdown1,blackdown2,blackdown3],[blackdeath1,blackdeath2,blackdeath3]]
moves = [[stillup,moveup1,moveup2],[stillright,moveright1,moveright2],[stillleft,moveleft1,moveleft2],[stilldown,movedown1,movedown2],[death1,death2,death3]]
bomb1.set_colorkey((112,192,128))
bomb2.set_colorkey((112,192,128))
bomb = [bomb1,bomb2]
explosionup.set_colorkey((112,192,128))
explosiondown.set_colorkey((112,192,128))
explosionleft.set_colorkey((112,192,128))
explosionright.set_colorkey((112,192,128))
explosionup2.set_colorkey((112,192,128))
explosiondown2.set_colorkey((112,192,128))
explosionleft2.set_colorkey((112,192,128))
explosionright2.set_colorkey((112,192,128))
explosionup3.set_colorkey((112,192,128))
explosiondown3.set_colorkey((112,192,128))
explosionleft3.set_colorkey((112,192,128))
explosionright3.set_colorkey((112,192,128))
#Getting rid of that green background in all of the sprites and making it transparent
for i in moves:
    for x in i:
        x.set_colorkey((112,192,128))
for i in redmoves:
    for x in i:
        x.set_colorkey((112,192,128))
for i in bluemoves:
    for x in i:
        x.set_colorkey((112,192,128))
for i in blackmoves:
    for x in i:
        x.set_colorkey((112,192,128))

#The opening menu screen that keeps running through a loop until 'Enter' is pressed, which breaks this loop by setting
#menu to false and starts my main game loop by setting running to true.
while menu:
    for evt in event.get():
        if evt.type == QUIT:
            menu = False
            quit()
    keys = key.get_pressed()    
    if keys[K_DOWN] and option == 'play': #Makes it so you can't go down further than the 'Instructions' button
        menupicycoord += 25
        option = 'instruction' #Sets the flag so you can't go above the 'Play' button
    elif keys[K_UP] and option == 'instruction':
        menupicycoord += -25
        option = 'play'        
    if keys[K_RETURN] and option == 'play': #Ends the menu loop and goes straight to the for loop which creates the playing
                                            #field and enters the main gam eloop
        menu = False
      
    if keys[K_RETURN] and option == 'instruction' and currentscreen == 'menu':
        currentscreen = 'instruction' #Blits the instruction screen if the user hits enter when the pointer is at instructions
        time.wait(100)
    elif keys[K_RETURN] and currentscreen == 'instruction':
        currentscreen = 'menu' #Blits the menu screen when you're at the instruction screen to go back
        time.wait(100)
    if currentscreen == 'menu':            
        menupicdelay += 1 #Makes the white bomberman move where the users input would be
        if menupicdelay == 10:
            menupic2+=1
            menupicdelay = 0
        if menupic2 == 3:
            menupic2 = 1
        screen.blit(backgroundpic,(0,0,525,455))
        screen.blit(moves[3][menupic2],(380,menupicycoord))
    elif currentscreen == 'instruction':
        menupicdelay += 1
        if menupicdelay == 10:
            menupic2+=1
            menupicdelay = 0
        if menupic2 == 3:
            menupic2 = 1
        screen.blit(instruction,(0,0,525,455))
        screen.blit(moves[3][menupic2],(176,18))    
    display.flip()
#Drawing the actual playing field and creating the 2D list that represents the playing field which holds positions for
#open spaces, bricks and boxes. Open spaces are represented with a 0, boxes are represented by a 3, and bricks are
#represented with a 1
for i in range(13):
    everything.append([])
    aieverything.append([])
    if i != 0:
        count1 = 0
        count2 += 35
    for y in range(15):
        aieverything[i].append(0)
        screen.blit(brick,(count1,count2))
        if i == 0 or i == 12:
            screen.blit(brickhoriz,(count1,count2)) 
        if y == 0 or y == 14:
            screen.blit(brickvert,(count1,count2))
        if y == 0 and i == 0:
            screen.blit(bricktopleft,(count1,count2))
        if i == 0 and y == 14:
            screen.blit(bricktopright,(count1,count2))
        if i == 12 and y == 0:
            screen.blit(brickbottomleft,(count1,count2))
        if i == 12 and y == 14:
            screen.blit(brickbottomright,(count1,count2))
        everything[i].append(1)
        if i != 0 and i != 12 and y != 0 and y != 14:
            if y%2 != 0 or i%2 != 0:
                screen.blit(crate,(count1,count2))
                everything[i][y] = 3
        if i == 1 and y == 2 or i == 1 and y == 1 or i == 2 and y == 1 or i == 1 and y == 13 or i == 2 and y == 13\
        or i == 1 and y == 12 or i == 11 and y == 1 or i == 11 and y == 2 or i == 10 and y == 1 or i == 11 and y == 13\
        or i == 11 and y == 12 or i == 10 and y == 13:
            draw.rect(screen,(0,200,0),(count1,count2,35,35))
            everything[i][y] = 0
        count1 += 35
        
copied = screen.copy()


#These are the four movement functions for the AI. These four functions are used by all three AI characters (and called
#upon by the movement choosing function later in the program). They take in the x and y coordinates of the characters,
#their position in the 2D list, a specific moving flag (one for each character so they can move at different times),
#a variable which tells the function which AI is using the function (like the moveflag parameter, but this one helps
#with the counters), and the two sprite variables in the sprite picture list (so you can cycle through the list with
#these variables which cycles through the pictures on the screen and makes it look like the sprites are moving). 
def airight(a,b,c,moveflag,whichai,aiframe1,aiframe2,right):
    global aicounter1,aicounter2,aicounter3,aieverything
    aiframe1 = 1 #Making sure the right directional sprite is used
    aiframe2 += 1 #Makes it look like it's walking by cycling through the list
    c += 5 #Increasing the x coordinate of the character everytime the function is called
    if aiframe2 == 3:
        aiframe2 = 1 #Resets the cycle so it doesn't go out of range (and makes it walk like 'left foot, right foot')
    if whichai == 1: #If the red guy is the one using this function. I have to be able to tell which character uses which
                    #function because I need to know which counters to increase (so all the characters can move at different
                    #directions at different times).
        aicounter1 += 1
        if aicounter1 == 7: #The characters all move in complete squres (cannot stop between two squares). These squares
                            #are 35x35. Since I'm increasing the x coordinate by 5, once this function is called 7 times
                            #the player would be at the next square, and it sets the moving variable and the right variable
                            #to false so the movement function can choose another way to move. Also increases the position
                            #of where it is on the 2D list (it actually isn't on the 2D list, but it helps make things
                            #simpler). 
            aicounter1 = 0
            aiframe2 = 0
            moveflag = False            
            b += 1
            right = False
            aieverything[a][b] = aieverything[a][b] + 1
            
            return a,b,c,moveflag,whichai,aiframe1,aiframe2,right
    elif whichai == 2: #Black guy.
        aicounter2 += 1
        if aicounter2 == 7:
            aicounter2 = 0
            aiframe2 = 0
            moveflag = False
            right = False
            b += 1
            aieverything[a][b] = aieverything[a][b] + 1
            return a,b,c,moveflag,whichai,aiframe1,aiframe2,right
    elif whichai == 3: #Blue guy. 
        aicounter3 += 1
        if aicounter3 == 7:
            aicounter3 = 0
            aiframe2 = 0
            moveflag = False
            right = False
            b += 1
            aieverything[a][b] = aieverything[a][b] + 1
            return a,b,c,moveflag,whichai,aiframe1,aiframe2,right        
    return a,b,c,moveflag,whichai,aiframe1,aiframe2,right


#The next three functions are almost mirror images of the one above, except the coordinates change in a different direction
#(ex it'll move in a negative direction for the left funtion or the y coordinate will increase instead of the x coordniate
#for the up function). 
def aiup(a,b,c,moveflag,whichai,aiframe1,aiframe2,up):
    global aicounter1,aicounter2,aicounter3,aieverything
    aiframe1 = 0
    aiframe2 += 1
    c += -5
    if aiframe2 == 3:
        aiframe2 = 1
    if whichai == 1:
        aicounter1 += 1
        if aicounter1 == 7:
            aicounter1 = 0
            aiframe2 = 0
            moveflag = False
            up = False
            a += -1
            aieverything[a][b] = aieverything[a][b] + 1
            return a,b,c,moveflag,whichai,aiframe1,aiframe2,up
    elif whichai == 2:
        aicounter2 += 1
        if aicounter2 == 7:
            aicounter2 = 0
            aiframe2 = 0
            moveflag = False
            up = False
            a += -1
            aieverything[a][b] = aieverything[a][b] + 1
            return a,b,c,moveflag,whichai,aiframe1,aiframe2,up
    elif whichai == 3:
        aicounter3 += 1
        if aicounter3 == 7:
            aiframe2 = 0
            aicounter3 = 0
            moveflag = False
            up = False
            a += -1
            aieverything[a][b] = aieverything[a][b] + 1
            return a,b,c,moveflag,whichai,aiframe1,aiframe2,up        
    return a,b,c,moveflag,whichai,aiframe1,aiframe2,up

def aileft(a,b,c,moveflag,whichai,aiframe1,aiframe2,left):
    global aicounter1,aicounter2,aicounter3,aieverything
    aiframe1 = 2
    aiframe2 += 1
    c += -5
    if aiframe2 == 3:
        aiframe2 = 1
    if whichai == 1:
        aicounter1 += 1
        if aicounter1 == 7:
            aicounter1 = 0
            aiframe2 = 0
            moveflag = False
            left = False
            b += -1
            aieverything[a][b] = aieverything[a][b] + 1
            return a,b,c,moveflag,whichai,aiframe1,aiframe2,left
    elif whichai == 2:
        aicounter2 += 1
        if aicounter2 == 7:
            aicounter2 = 0
            aiframe2 = 0
            moveflag = False
            left = False
            b += -1
            aieverything[a][b] = aieverything[a][b] + 1
            return a,b,c,moveflag,whichai,aiframe1,aiframe2,left
    elif whichai == 3:
        aicounter3 += 1
        if aicounter3 == 7:
            aicounter3 = 0
            aiframe2 = 0
            moveflag = False
            left = False
            b += -1
            aieverything[a][b] = aieverything[a][b] + 1
            return a,b,c,moveflag,whichai,aiframe1,aiframe2,left    
    return a,b,c,moveflag,whichai,aiframe1,aiframe2,left

def aidown(a,b,c,moveflag,whichai,aiframe1,aiframe2,down):
    global aicounter1,aicounter2,aicounter3,aieverything
    aiframe1 = 3
    aiframe2 += 1
    c += 5
    if aiframe2 == 3:
        aiframe2 = 1
    if whichai == 1:
        aicounter1 += 1
        if aicounter1 == 7:
            aicounter1 = 0
            aiframe2 = 0
            moveflag = False
            down = False
            a += 1
            aieverything[a][b] = aieverything[a][b] + 1
            return a,b,c,moveflag,whichai,aiframe1,aiframe2,down
    elif whichai == 2:
        aicounter2 += 1
        if aicounter2 == 7:
            aicounter2 = 0
            aiframe2 = 0
            moveflag = False
            down = False
            a += 1
            aieverything[a][b] = aieverything[a][b] + 1
            return a,b,c,moveflag,whichai,aiframe1,aiframe2,down
    elif whichai == 3:
        aicounter3 += 1
        if aicounter3 == 7:
            aicounter3 = 0
            aiframe2 = 0
            moveflag = False
            down = False
            a += 1
            aieverything[a][b] = aieverything[a][b] + 1
            return a,b,c,moveflag,whichai,aiframe1,aiframe2,down            
    return a,b,c ,moveflag,whichai,aiframe1,aiframe2,down

#This is the heart and guts of the AI, which is pretty simple. The thing that makes my AI work is that they are
#always in constant motion (at least when they can be). If the ai that is using this function
#(whether it be the red, black or blue guy) is not moving it makes it choose another action to do (move again or plant
#a bomb). These actions are then added to the action list (1 is moving up, 2 is moving down, 3 is moving right, 4 is moving
#left and 5 is bombing) if it is a valid action (for example the moving right function is added to the action list if there
#isn't a brick/box to the right of the player or if there isn't a bomb two spaces to the right or one space to the right,
#one space above(below)). 
def aimoving(x,y,graphx,graphy,moveflag,aibombingon,bombposx,bombposy,bomby,bombx,aibombone,whichai,aiframe1,aiframe2,up,down,left,right):
    global everything,aieverything,aiy1,aix1,aiy2,aix2,aiy3,aix3,newy,newx
    if moveflag == False:
        movinglist = []
        movinglist.append(5)#Adding the bombing function to the action list if it is a valid choice. 
        if everything[y-1][x] == 0 and everything[y-1][x+1] != 4 and everything[y-1][x-1] != 4 and everything[y-2][x] != 4\
           and everything[y-1][x+1] != 40 and everything[y-1][x-1] != 40 and everything[y-2][x] != 40\
           and everything[y-1][x+1] != 400 and everything[y-1][x-1] != 400 and everything[y-2][x] != 400\
           and everything[y-1][x+1] != 4000 and everything[y-1][x-1] != 4000 and everything[y-2][x] != 4000:
            movinglist.append(1)#Adding the up function to the action list if it is a valid choice. The 0 represents
                                #open space and anything that starts with a 4 is a bomb (ex 4 is the white players bomb
                                #and 40 is the red players bomb).
        if everything[y+1][x] == 0 and everything[y+1][x+1] != 4 and everything[y+1][x-1] != 4 and everything[y+2][x] != 4\
           and everything[y+1][x+1] != 40 and everything[y+1][x-1] != 40 and everything[y+2][x] != 40\
           and everything[y+1][x+1] != 400 and everything[y+1][x-1] != 400 and everything[y+2][x] != 400\
           and everything[y+1][x+1] != 4000 and everything[y+1][x-1] != 4000 and everything[y+2][x] != 4000:
            movinglist.append(2)#Adding the down function to the action list if it is a valid choice. 
        if everything[y][x+1] == 0 and everything[y-1][x+1] != 4 and everything[y+1][x+1] != 4 and everything[y][x+2] != 4\
           and everything[y-1][x+1] != 40 and everything[y+1][x+1] != 40 and everything[y][x+2] != 40\
           and everything[y-1][x+1] != 400 and everything[y+1][x+1] != 400 and everything[y][x+2] != 400\
           and everything[y-1][x+1] != 4000 and everything[y+1][x+1] != 4000 and everything[y][x+2] != 4000:
            movinglist.append(3)#Adding the right function to the action list if it is a valid choice. 
        if everything[y][x-1] == 0 and everything[y-1][x-1] != 4 and everything[y+1][x-1] != 4 and everything[y][x-2] != 4\
           and everything[y-1][x-1] != 40 and everything[y+1][x-1] != 40 and everything[y][x-2] != 40\
           and everything[y-1][x-1] != 400 and everything[y+1][x-1] != 400 and everything[y][x-2] != 400\
           and everything[y-1][x-1] != 4000 and everything[y+1][x-1] != 4000 and everything[y][x-2] != 4000:
            movinglist.append(4)#Adding the left function to the action list if it is a valid choice.
        #Checks if the ai is next to any player
        if (y-1,x) == (aiy1,aix1) or (y+1,x) == (aiy1,aix1) or (y,x+1) == (aiy1,aix1) or (y,x-1) == (aiy1,aix1) \
            or (y-1,x) == (aiy2,aix2) or (y+1,x) == (aiy2,aix2) or (y,x+1) == (aiy2,aix2) or (y,x-1) == (aiy2,aix2) \
            or (y-1,x) == (aiy3,aix3) or (y+1,x) == (aiy3,aix3) or (y,x+1) == (aiy3,aix3) or (y,x-1) == (aiy3,aix3) \
            or (y-1,x) == (newy,newx) or (y+1,x) == (newy,newx) or (y,x+1) == (newy,newx) or (y,x-1) == (newy,newx) :
            if randint(0,1) == 0: #If the ai is next to a player there's a 50% chance it'll lay a bomb
                if aibombingon == 0:#Makes sure the AI doesn't already have a bomb down
                    aibombingon = 1 #Sets the AIs bomb down and makes sure another one doesn't get set
                    bombposx = graphx #Keeps the coordinates of where the AI planted the bomb so he can move away and
                                        #the bomb will still be there
                    bombposy = graphy
                    bomby = y #Keeps the x and y positions of the bombs on the 2D list so you can tell if the explosion
                                #collides with anything
                    bombx = x                                        
                    aibombone = 1
                    if whichai == 1: #if the red player sets the bomb it marks it as 40 on the 2D list
                        everything[y][x] = 40 
                    elif whichai == 2:#if the black player sets the bomb it marks it as 400 on the 2D list
                        everything[y][x] = 400
                    elif whichai == 3:#if the blue player sets the bomb it marks it as 4000 on the 2D list
                        everything[y][x] = 4000
                    return x,y,graphx,graphy,moveflag,aibombingon,bombposx,bombposy,bomby,bombx,aibombone,whichai,aiframe1,aiframe2,up,down,left,right            
        if len(movinglist) == 1: #If the AI only has one position to move (trapped in a corner or something) and there is
            #a crate next to the AI, it forces it to lay a bomb.
            if everything[y-1][x] == 3 or everything[y+1][x] == 3 or everything[y][x+1] == 3 or everything[y][x-1] == 3:
                if aibombingon == 0:#Makes sure the AI doesn't already have a bomb do
                    aibombingon = 1
                    bombposx = graphx #Keeps the coordinates of where the AI planted the bomb so he can move away and
                                        #the bomb will still be there
                    bombposy = graphy
                    bomby = y #Keeps the x and y positions of the bombs on the 2D list so you can tell if the explosion
                              #collides with anything
                    bombx = x                    
                    aibombone = 1
                    if whichai == 1:#if the red player sets the bomb it marks it as 40 on the 2D list
                        everything[y][x] = 40
                    elif whichai == 2:#if the black player sets the bomb it marks it as 400 on the 2D list
                        everything[y][x] = 400
                    elif whichai == 3:#if the blue player sets the bomb it marks it as 4000 on the 2D list
                        everything[y][x] = 4000
                    return x,y,graphx,graphy,moveflag,aibombingon,bombposx,bombposy,bomby,bombx,aibombone,whichai,aiframe1,aiframe2,up,down,left,right            
        #If none of the bomb setting choices are chosen then it comes down here and a random choice is chosen from the
        #action list. 
        if len(movinglist) != 0:
            randommove1 = choice(movinglist)
        if randommove1 == 1:
            up = True
            moveflag = True
        elif randommove1 == 2:
            down = True
            moveflag = True
        elif randommove1 == 3:
            right = True
            moveflag = True
        elif randommove1 == 4:
            left = True
            moveflag = True
        elif randommove1 == 5:
            #Only plants a bomb if there is a crate next to the AI
            if everything[y-1][x] == 3 or everything[y+1][x] == 3 or everything[y][x+1] == 3 or everything[y][x-1] == 3 and len(movinglist) != 1:
                if aibombingon == 0:#Makes sure the AI doesn't already have a bomb do
                    aibombingon = 1
                    bombposx = graphx#Keeps the coordinates of where the AI planted the bomb so he can move away and
                                        #the bomb will still be there
                    bombposy = graphy
                    bomby = y
                    bombx = x#Keeps the x and y positions of the bombs on the 2D list so you can tell if the explosion
                              #collides with anything
                    aibombone = 1
                    if whichai == 1:#if the red player sets the bomb it marks it as 40 on the 2D list
                        everything[y][x] = 40
                    elif whichai == 2:#if the black player sets the bomb it marks it as 400 on the 2D list
                        everything[y][x] = 400
                    elif whichai == 3:#if the blue player sets the bomb it marks it as 4000 on the 2D list
                        everything[y][x] = 4000
    #This makes it so the AI moves in complete squares and not move in the middle of squares and inside a brick or something
    if moveflag == True:
        #Where the movement functions are called upon after they've been randomly selected from the action list
        if up == True:
            y,x,graphy,moveflag,whichai,aiframe1,aiframe2,up = aiup(y,x,graphy,moveflag,whichai,aiframe1,aiframe2,up)
        elif down == True:
            y,x,graphy,moveflag,whichai,aiframe1,aiframe2,down = aidown(y,x,graphy,moveflag,whichai,aiframe1,aiframe2,down)
        elif right == True:
            y,x,graphx,moveflag,whichai,aiframe1,aiframe2,right = airight(y,x,graphx,moveflag,whichai,aiframe1,aiframe2,right)
        elif left == True:
            y,x,graphx,moveflag,whichai,aiframe1,aiframe2,left = aileft(y,x,graphx,moveflag,whichai,aiframe1,aiframe2,left)    
    return x,y,graphx,graphy,moveflag,aibombingon,bombposx,bombposy,bomby,bombx,aibombone,whichai,aiframe1,aiframe2,up,down,left,right

#This is the player movement function. 
def humanmovement():
    global keys,everything,bb,newy,newx,aa,aiy1,aix1,gg,playerpic1,playerpic2,picturedelay,moving,movingup,movingleft,movingdown,movingright,movingcounter
    #Checking which key the user is pressing
    if keys[K_UP] and moving == False:
        playerpic1 = 0
        if everything[newy-1][newx] == 0 or everything[newy-1][newx] == 20 :
            moving = True #Sets the moving flag to True and this flag won't be set false until the full square is completed
                        #by the sprite (so the player moves in complete 35x35x circles)
            movingup = True #Sets a flag so the computer knows which variables to increase or decrease
                            #(the 2D list variables and the coordinates on the screen).
    elif keys[K_RIGHT] and moving == False :
        playerpic1 = 1
        if everything[newy][newx+1] == 0 or everything[newy][newx+1] == 20:
            moving = True
            movingright = True    
    elif keys[K_DOWN] and moving == False:
        playerpic1 = 3
        if everything[newy+1][newx] == 0 or everything[newy+1][newx] == 20:
            moving = True
            movingdown = True
    elif keys[K_LEFT] and moving == False:
        playerpic1 = 2
        if everything[newy][newx-1] == 0 or everything[newy][newx-1] == 20:
            moving = True
            movingleft = True
    if moving == True: #If the moving flag is true it checks which dierction it's suppose to go in (up,down,left,right)
        if movingup == True:                       
            bb += -5 #Increases or decreases the coordinates of the player to match which direction it is going
            playerpic2+= 1 #Cycles through the sprite list to make it look like the sprite is moving                        
            if playerpic2 == 3:
                playerpic2 = 1 #Makes sure it doesn't go out of range and makes it walk like 'left foot, right foot'                                               
            movingcounter += -1 #Moving counter starts off at 7. Since the sprite moves by 5 pixels each time it will take
                                #7 pixels for it to fully complete the square (35).
            if movingcounter == 0:
                moving = False #After it compeltes the square it is free to move again and all variables are reset
                movingup = False
                movingcounter = 7
                playerpic2 = 0
                newy += -1
        elif movingright == True:                      
            aa += 5#Increases or decreases the coordinates of the player to match which direction it is going
            playerpic2+= 1 
            if playerpic2 == 3:
                playerpic2 = 1#Makes sure it doesn't go out of range and makes it walk like 'left foot, right foot'  
            movingcounter += -1#Moving counter starts off at 7. Since the sprite moves by 5 pixels each time it will take
                                #7 pixels for it to fully complete the square (35).
            if movingcounter == 0:
                moving = False#After it compeltes the square it is free to move again and all variables are reset
                movingright = False
                movingcounter = 7
                playerpic2 = 0
                newx += 1
        elif movingleft == True:            
            playerpic2+= 1
            if playerpic2 == 3:
                playerpic2 = 1#Makes sure it doesn't go out of range and makes it walk like 'left foot, right foot'  
            aa += -5#Increases or decreases the coordinates of the player to match which direction it is going
            movingcounter += -1#Moving counter starts off at 7. Since the sprite moves by 5 pixels each time it will take
                                #7 pixels for it to fully complete the square (35).
            if movingcounter == 0:
                moving = False#After it compeltes the square it is free to move again and all variables are reset
                movingleft = False
                movingcounter = 7
                newx += -1
                playerpic2 = 0
        elif movingdown == True:            
            playerpic2+= 1
            if playerpic2 == 3:
                playerpic2 = 1  #Makes sure it doesn't go out of range and makes it walk like 'left foot, right foot'                        
            bb += 5#Increases or decreases the coordinates of the player to match which direction it is going
            movingcounter += -1#Moving counter starts off at 7. Since the sprite moves by 5 pixels each time it will take
                                #7 pixels for it to fully complete the square (35).
            if movingcounter == 0:
                moving = False#After it compeltes the square it is free to move again and all variables are reset
                movingdown = False
                movingcounter = 7
                playerpic2 = 0
                newy += 1

#Figuring out if the player sets a bomb
def humanbombset():
    global keys,bombon,explosion,bombposy,bombposx,everything,bombgridy,bombgridx,moving,bombon1,aibomby1,aibombx1,aibomby2,aibombx2,aibomby3,aibombx3
    #If the player hits the space bar and the player sprite is not moving (so you can't set a bomb between two squares)
    #it sets off the bomb reactions by setting the bomb variables to True
    if keys[K_SPACE] and moving == False and (newy,newx) != (aibomby1,aibombx1) and (newy,newx) != (aibomby2,aibombx2) and (newy,newx) != (aibomby3,aibombx3):
        if bombon == 0 and bombon1 == 0:
            bombon = 1
            bombon1 = 1
            explosion = 1
            bombposy = aa
            bombposx = bb
            everything[newy][newx] = 4
            bombgridy = newy
            bombgridx = newx

#This is the bomb exploding function. It is constantly being called in the loop, but inside the function it checks if
#a bomb is set by the player or not
def humanbombon():
    global leftexplosion,upexplosion,downexplosion,bombon,bombon1,bombposy,bombposx,explosion,aibombcounter1,aibombcounter2,aibombcounter3,bombcounter,everything,rightexplosion,bombgridy,bombgridx,bombframe,newy,newx,alive,aiy1,aiy2,aiy3,aix1,aix2,aix3,aialive1,aialive2,aialive3,playerpic2,redpic2,blackpic2,bluepic2
    #This checks if a brick falls on the bomb (when the doom function is being called this is a posibility)
    #and it turns off the bomb if a brick does fall on the bomb by setting all the variables to 0.
    if everything[bombgridy][bombgridx] == 1:
        bombon = 0
        bombon1 = 0
        explosion = 0
        bombcounter = 0        
    if bombon == 1:
        #Blits the bomb sprite 
        screen.blit(bomb[bombframe],(bombposy,bombposx))            
    if explosion == 1:
        bombcounter += 1
        if bombcounter > 20:
            #This makes it cycle through the bomb sprites (makes it flash red/black) after a certian amount of time.
            bombframe += 1
            if bombframe == 2:
                bombframe = 0
        #After the counter hits 40 it starts to explode. It checks all around the bomb to see if there could be a valid
        #explosion and sets the explosion spot to true if it's vaild (ex. if there is an open space to the right of
        #the bomb the right explosion will be true)
        if bombcounter == 40:
            #Checking to see if each spot is a valid explosion
            if everything[bombgridy][bombgridx] != 1:
                draw.rect(screen,(0,200,0),(bombposy,bombposx,35,35))
            #Checks the spots and makes sure they're not bricks or other bmobs (looks weird when two explosion sprites
            #overlap each other). If the spot is valid it sets that spot to True
            if everything[bombgridy][bombgridx+1] != 1 and everything[bombgridy][bombgridx+1] != 40 and everything[bombgridy][bombgridx+1] != 400 and everything[bombgridy][bombgridx+1] != 4000:
                rightexplosion = True
                screen.blit(explosionright,(bombposy,bombposx))
            if everything[bombgridy+1][bombgridx] != 1 and everything[bombgridy+1][bombgridx] != 40 and everything[bombgridy+1][bombgridx] != 400 and everything[bombgridy+1][bombgridx] != 4000:
                downexplosion = True
                screen.blit(explosiondown,(bombposy,bombposx))                
            if everything[bombgridy][bombgridx-1] != 1 and everything[bombgridy][bombgridx-1] != 40 and everything[bombgridy][bombgridx-1] != 400 and everything[bombgridy][bombgridx-1] != 4000:
                leftexplosion = True
                screen.blit(explosionleft,(bombposy-35,bombposx))                
            if everything[bombgridy-1][bombgridx] != 1 and everything[bombgridy-1][bombgridx] != 40 and everything[bombgridy-1][bombgridx] != 400 and everything[bombgridy-1][bombgridx] != 4000:
                upexplosion = True
                screen.blit(explosionup,(bombposy,bombposx-35))
            #This is to see if the bomb explosion will set off another bomb. Each bomb is unique (4 is player, 40 is
            #red ai, 400 is black ai and 4000 is blue ai) so I check to see if it explodes next to any of these bombs.
            #If it does I set the bombcounter that relates to the correct bomb to the point where it explodes.
            if everything[bombgridy][bombgridx+1] == 40 and aibombcounter1 <39: #Checks to the right if it's red guys bomb       
                aibombcounter1 = 39 
            elif everything[bombgridy][bombgridx+1] == 400 and aibombcounter2 <39: #Checks to the right if it's black guys bomb 
                aibombcounter2 = 39
            elif everything[bombgridy][bombgridx+1] == 4000 and aibombcounter3 <39: #Checks to the right if it's blue guys bomb 
                aibombcounter3 = 39                
            if everything[bombgridy+1][bombgridx] == 40 and aibombcounter1 <39:  #Checks below to see if it's red guys bomb             
                aibombcounter1 = 39
            elif everything[bombgridy+1][bombgridx] == 400 and aibombcounter2 <39:#Checks below to see if it's black guys bomb 
                aibombcounter2 = 39
            elif everything[bombgridy+1][bombgridx] == 4000 and aibombcounter3 <39:#Checks below to see if it's blue guys bomb 
                aibombcounter3 = 39                
            if everything[bombgridy][bombgridx-1] == 40 and aibombcounter1 <39: #Checks to the left if it's red guys bomb                
                aibombcounter1 = 39
            elif everything[bombgridy][bombgridx-1] == 400 and aibombcounter2 < 39:#Checks to the left if it's black guys bomb 
                aibombcounter2 = 39
            elif everything[bombgridy][bombgridx-1] == 4000 and aibombcounter3 < 39:#Checks to the left if it's blue guys bomb 
                aibombcounter3 = 39                
            if everything[bombgridy-1][bombgridx] == 40 and aibombcounter1 <39: #Checks above to see if it's red guys bomb
                aibombcounter1 = 39
            elif everything[bombgridy-1][bombgridx] == 400 and aibombcounter2 <39: #Checks above to see if it's black guys bomb
                aibombcounter2 = 39
            elif everything[bombgridy-1][bombgridx] == 4000 and aibombcounter3 < 39: #Checks above to see if it's blue guys bomb
                aibombcounter3 = 39
        #If the bombcounter is greater than 40 (after it explodes and cycles through the three explosion frames) it checks
        #if there is anyone in the explosions path. If there is, it sets their living variable to False. All living variables
        #are checked every single time in the loop and it determines whether to draw the certain sprite and whether or not
        #to call their moving/bomb functions or not. 
        
        if bombcounter >= 40:
            if (bombgridy,bombgridx) == (newy,newx): #Checks to see if the bomb explodes ontop of the white player
                alive = False 
                playerpic2 = 0
            if (bombgridy,bombgridx) == (aiy1,aix1):#Checks to see if the bomb explodes ontop of the red player
                aialive1 = False
                redpic2 = 0
            if (bombgridy,bombgridx) == (aiy2,aix2):#Checks to see if the bomb explodes ontop of the black player
                aialive2 = False
                blackpic2 = 0
            if (bombgridy,bombgridx) == (aiy3,aix3):#Checks to see if the bomb explodes ontop of the blue player
                aialive3 = False
                bluepic2 = 0                
            if (bombgridy,bombgridx+1) == (newy,newx):#Checks to see if the bomb explodes to the right of the white player
                alive = False
                playerpic2 = 0
            if (bombgridy,bombgridx+1) == (aiy1,aix1):#Checks to see if the bomb explodes to the right of the red player
                aialive1 = False
                redpic2 = 0
            if (bombgridy,bombgridx+1) == (aiy2,aix2):#Checks to see if the bomb explodes to the right of the black player
                aialive2 = False
                blackpic2 = 0
            if (bombgridy,bombgridx+1) == (aiy3,aix3):#Checks to see if the bomb explodes to the right of the blue player
                aialive3 = False
                bluepic2 = 0                                
            if (bombgridy,bombgridx-1) == (newy,newx):#Checks to see if the bomb explodes to the left of the white player
                alive = False
                playerpic2 = 0
            if (bombgridy,bombgridx-1) == (aiy1,aix1):#Checks to see if the bomb explodes to the left of the red player
                aialive1 = False
                redpic2 = 0
            if (bombgridy,bombgridx-1) == (aiy2,aix2):#Checks to see if the bomb explodes to the left of the black player
                aialive2 = False
                blackpic2 = 0
            if (bombgridy,bombgridx-1) == (aiy3,aix3):#Checks to see if the bomb explodes to the left of the blue player
                aialive3 = False
                bluepic2 = 0
            if (bombgridy+1,bombgridx) == (newy,newx):#Checks to see if the bomb explodes below the white player
                alive = False
                playerpic2 = 0
            if (bombgridy+1,bombgridx) == (aiy1,aix1):#Checks to see if the bomb explodes below the red player
                aialive1 = False
                redpic2 = 0
            if (bombgridy+1,bombgridx) == (aiy2,aix2):#Checks to see if the bomb explodes below the black player
                aialive2 = False
                blackpic2 = 0
            if (bombgridy+1,bombgridx) == (aiy3,aix3):#Checks to see if the bomb explodes below the blue player
                aialive3 = False
                bluepic2 = 0
            if (bombgridy-1,bombgridx) == (newy,newx):#Checks to see if the bomb explodes above the white player
                alive = False
                playerpic2 = 0
            if (bombgridy-1,bombgridx) == (aiy1,aix1):#Checks to see if the bomb explodes above the red player
                aialive1 = False
                redpic2 = 0
            if (bombgridy-1,bombgridx) == (aiy2,aix2):#Checks to see if the bomb explodes above the black player
                aialive2 = False
                blackpic2 = 0
            if (bombgridy-1,bombgridx) == (aiy3,aix3):#Checks to see if the bomb explodes above the blue player
                aialive3 = False
                bluepic2 = 0
            bombon = 0
        if bombcounter == 41: #Cycles through the explosion pictures to make it look like the explosion is bigger if the respective flag is set to true
            if rightexplosion == True:
                screen.blit(explosionright2,(bombposy,bombposx))
            if downexplosion == True:
                screen.blit(explosiondown2,(bombposy,bombposx))
            if leftexplosion == True:
                screen.blit(explosionleft2,(bombposy-35,bombposx))
            if upexplosion == True:
                screen.blit(explosionup2,(bombposy,bombposx-35))
        if bombcounter == 44: #Cycles through the explosion pictures to make it look like the explosion is bigger if the respective flag is set to true

            if rightexplosion == True:
                screen.blit(explosionright3,(bombposy,bombposx))
            if downexplosion == True:
                screen.blit(explosiondown3,(bombposy,bombposx))
            if leftexplosion == True:
                screen.blit(explosionleft3,(bombposy-35,bombposx))
            if upexplosion == True:
                screen.blit(explosionup3,(bombposy,bombposx-35))                                        
        if bombcounter == 46: #Cycles through the explosion pictures to make it look like the explosion is bigger if the respective flag is set to true
         
            if rightexplosion == True:
                draw.rect(screen,(0,200,0),(bombposy+35,bombposx,35,35))
                rightexplosion = False
                everything[bombgridy][bombgridx+1] = 0
            if downexplosion == True:
                draw.rect(screen,(0,200,0),(bombposy,bombposx+35,35,35))
                downexplosion = False
                everything[bombgridy+1][bombgridx] = 0
            if leftexplosion == True:
                draw.rect(screen,(0,200,0),(bombposy-35,bombposx,35,35))
                leftexplosion = False
                everything[bombgridy][bombgridx-1] = 0
            if upexplosion == True:
                draw.rect(screen,(0,200,0),(bombposy,bombposx-35,35,35))
                upexplosion = False
                everything[bombgridy-1][bombgridx] = 0
            #Resets all the variables so that another bomb can be planted
            draw.rect(screen,(0,200,0),(bombposy,bombposx,35,35))
            bombon1 = 0
            bombframe = 0            
            explosion = 0
            bombcounter = 0
            everything[bombgridy][bombgridx] = 0

#The Red AI's bomb exploding function which is very much like the human bombing function. Comments will be simplifid, refer to humanbombon() for
#a better explanation.
def aibombing1():
    global movingflag,aibomber1,aiexplosion1,aibombon1,bombcounter,aibombcounter2,aibombcounter3,aibombcounter1,alive,newy,newx,aibombframe1,aibombposx1,aibombposy1,aibomby1,aibombx1,rightexplosion1,leftexplosion1,downexplosion1,upexplosion1,aix1,aix2,aix3,aiy1,aiy2,aiy3,aialive1,aialive2,aialive3,redpic2,blackpic2,bluepic2,playerpic2
    aiexplosion1 = 1 #sets the flag to set off the explosion counter
    if aibombon1 == 1:       
        screen.blit(bomb[aibombframe1],(aibombposx1,aibombposy1))    
    if aiexplosion1 == 1:        
        aibombcounter1 += 1
        if aibombcounter1 > 20:
            aibombframe1 += 1 #makes it flash red
            if aibombframe1 == 2:
                aibombframe1 = 0
        if aibombcounter1 == 40: #Explodes - checks if areas are valid for explosion
            if everything[aibomby1][aibombx1] != 1:
                draw.rect(screen,(0,200,0),(aibombposx1,aibombposy1,35,35))            
            if everything[aibomby1][aibombx1+1] != 1 and everything[aibomby1][aibombx1+1] != 4 and everything[aibomby1][aibombx1+1] != 400 and everything[aibomby1][aibombx1+1] != 4000:
                rightexplosion1 = True
                screen.blit(explosionright,(aibombposx1,aibombposy1))                
            if everything[aibomby1+1][aibombx1] != 1 and everything[aibomby1+1][aibombx1] != 4 and everything[aibomby1+1][aibombx1] != 400 and everything[aibomby1+1][aibombx1] != 4000:
                downexplosion1 = True
                screen.blit(explosiondown,(aibombposx1,aibombposy1))                
            if everything[aibomby1][aibombx1-1] != 1 and everything[aibomby1][aibombx1-1] != 4 and everything[aibomby1][aibombx1-1] != 400 and everything[aibomby1][aibombx1-1] != 4000:
                leftexplosion1 = True
                screen.blit(explosionleft,(aibombposx1-35,aibombposy1))                
            if everything[aibomby1-1][aibombx1] != 1 and everything[aibomby1-1][aibombx1] != 4 and everything[aibomby1-1][aibombx1] != 400 and everything[aibomby1-1][aibombx1] != 4000:
                upexplosion1 = True
                screen.blit(explosionup,(aibombposx1,aibombposy1-35))
            aibombon1 = 0
            #Checking to see if the bomb explodes to any other bombs (4 for white players bomb, 40 for red guy, 400 for black guy, 4000 for blue guy)
            #and if the bobm does explode next to another bomb it sets the respective counter to the point where it explodes as well creating a chain
            if everything[aibomby1][aibombx1+1] == 4 and bombcounter <39:                
                bombcounter = 39
            elif everything[aibomby1][aibombx1+1] == 400 and aibombcounter2 <39:
                aibombcounter2 = 39
            elif everything[aibomby1][aibombx1+1] == 4000 and aibombcounter3 <39:
                aibombcounter3 = 39
            if everything[aibomby1+1][aibombx1] == 4 and bombcounter <39:                
                bombcounter = 39
            elif everything[aibomby1+1][aibombx1] == 400 and aibombcounter2 <39:
                aibombcounter2 = 39
            elif everything[aibomby1+1][aibombx1] == 4000 and aibombcounter3 <39:
                aibombcounter3 = 39
            if everything[aibomby1][aibombx1-1] == 4 and bombcounter <39:                
                bombcounter = 39
            elif everything[aibomby1][aibombx1-1] == 400 and aibombcounter2 < 39:
                aibombcounter2 = 39
            elif everything[aibomby1][aibombx1-1] == 4000 and aibombcounter3 < 39:
                aibombcounter3 = 39
            if everything[aibomby1-1][aibombx1] == 4 and bombcounter <39:                
                bombcounter = 39
            elif everything[aibomby1-1][aibombx1] == 400 and aibombcounter2 <39:
                aibombcounter2 = 39
            elif everything[aibomby1-1][aibombx1] == 4000 and aibombcounter3 < 39:
                aibombcounter3 = 39
        #Checks to see if there is a player in the way of any of the explosions. If there is, it sets their living flag to False (if the living flag is false
        #it goes through the death sprite cycle and then stops blitting the picture)
        if aibombcounter1 >= 40:
            if (aibomby1,aibombx1) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby1,aibombx1) == (newy,newx):
                alive = False
                playerpic2 = 0
            if (aibomby1,aibombx1) == (aiy2,aix2):
                aialive2 = False
                blacpic2 = 0
            if (aibomby1,aibombx1) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0                        
            if (aibomby1,aibombx1+1) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby1,aibombx1+1) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby1,aibombx1+1) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby1,aibombx1+1) == (newy,newx):
                alive = False
                playerpic2 = 0                
            if (aibomby1,aibombx1-1) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby1,aibombx1-1) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby1,aibombx1-1) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby1,aibombx1-1) == (newy,newx):
                alive = False
                playerpic2 = 0
            if (aibomby1+1,aibombx1) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby1+1,aibombx1) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby1+1,aibombx1) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby1+1,aibombx1) == (newy,newx):
                alive = False
                playerpic2 = 0
            if (aibomby1-1,aibombx1) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby1-1,aibombx1) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby1-1,aibombx1) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby1-1,aibombx1) == (newy,newx):
                alive = False
                playerpic2 = 0
        #Explosion cycle which makes the explosion bigger (if the direction is valid)
        if aibombcounter1 == 41:
            if rightexplosion1 == True:
                screen.blit(explosionright2,(aibombposx1,aibombposy1))
            if downexplosion1 == True:
                screen.blit(explosiondown2,(aibombposx1,aibombposy1))
            if leftexplosion1 == True:
                screen.blit(explosionleft2,(aibombposx1-35,aibombposy1))
            if upexplosion1 == True:
                screen.blit(explosionup2,(aibombposx1,aibombposy1-35))
        #Explosion cycle which makes the explosion bigger (if the direction is valid)
        if aibombcounter1 == 44:
            if rightexplosion1 == True:
                screen.blit(explosionright3,(aibombposx1,aibombposy1))
            if downexplosion1 == True:
                screen.blit(explosiondown3,(aibombposx1,aibombposy1))
            if leftexplosion1 == True:
                screen.blit(explosionleft3,(aibombposx1-35,aibombposy1))
            if upexplosion1 == True:
                screen.blit(explosionup3,(aibombposx1,aibombposy1-35))
        #Explosion cycle which makes the explosion bigger (if the direction is valid)
        if aibombcounter1 == 46:            
            if rightexplosion1 == True:
                draw.rect(screen,(0,200,0),(aibombposx1+35,aibombposy1,35,35))
                everything[aibomby1][aibombx1+1] = 0
                rightexplosion1 = False
            if downexplosion1 == True:
                draw.rect(screen,(0,200,0),(aibombposx1,aibombposy1+35,35,35))
                everything[aibomby1+1][aibombx1] = 0
                downexplosion1 = False
            if leftexplosion1 == True:
                everything[aibomby1][aibombx1-1] = 0
                draw.rect(screen,(0,200,0),(aibombposx1-35,aibombposy1,35,35))
                leftexplosion1 = False
            if upexplosion1 == True:
                everything[aibomby1-1][aibombx1] = 0
                draw.rect(screen,(0,200,0),(aibombposx1,aibombposy1-35,35,35))
                upexplosion1 = False                                                
            draw.rect(screen,(0,200,0),(aibombposx1,aibombposy1,35,35))
            #Resets all the variables so another bomb can be set
            aibombon1 = 0
            aibombframe1 = 0            
            aiexplosion1 = 0
            aibombcounter1 = 0
            aibomber1 = 0
            everything[aibomby1][aibombx1] = 0

#The BLACK AI's bomb exploding function which is very much like the human bombing function. Comments will be simplifid, refer to humanbombon() for
#a better explanation.
def aibombing2():
    global movingflag2,aibomber2,aiexplosion2,aibombon2,aibombcounter2,aibombcounter1,bombcounter,aibombcounter3,alive,newy,newx,aibombframe2,aibombposx2,aibombposy2,aibomby2,aibombx2,rightexplosion2,leftexplosion2,downexplosion2,upexplosion2,aiy1,aiy2,aiy3,aix1,aix2,aix3,newy,newx,aialive1,aialive2,aialive3,playerpic2,blackpic2,redpic2,bluepic2
    aiexplosion2 = 1        
    if aibombon2 == 1:       
        screen.blit(bomb[aibombframe2],(aibombposx2,aibombposy2))    
    if aiexplosion2 == 1:        
        aibombcounter2 += 1
        if aibombcounter2 > 20:
            aibombframe2 += 1
            if aibombframe2 == 2:
                aibombframe2 = 0
        if aibombcounter2 == 40:
            if everything[aibomby2][aibombx2] != 1: 
                draw.rect(screen,(0,200,0),(aibombposx2,aibombposy2,35,35))            
            if everything[aibomby2][aibombx2+1] != 1 and everything[aibomby2][aibombx2+1] != 4 and everything[aibomby2][aibombx2+1] != 40 and everything[aibomby2][aibombx2+1] != 4000:
                rightexplosion2 = True
                screen.blit(explosionright,(aibombposx2,aibombposy2))
            if everything[aibomby2+1][aibombx2] != 1 and everything[aibomby2+1][aibombx2] != 4 and everything[aibomby2+1][aibombx2] != 40 and everything[aibomby2+1][aibombx2] != 4000:
                downexplosion2 = True
                screen.blit(explosiondown,(aibombposx2,aibombposy2))
            if everything[aibomby2][aibombx2-1] != 1 and everything[aibomby2][aibombx2-1] != 4 and everything[aibomby2][aibombx2-1] != 40 and everything[aibomby2][aibombx2-1] != 4000:
                leftexplosion2 = True
                screen.blit(explosionleft,(aibombposx2-35,aibombposy2))                
            if everything[aibomby2-1][aibombx2] != 1 and everything[aibomby2-1][aibombx2] != 4 and everything[aibomby2-1][aibombx2] != 40 and everything[aibomby2-1][aibombx2] != 4000:
                upexplosion2 = True
                screen.blit(explosionup,(aibombposx2,aibombposy2-35))                
            aibombon2 = 0            
            if everything[aibomby2][aibombx2+1] == 4 and bombcounter < 39:
                bombcounter = 39
            elif everything[aibomby2][aibombx2+1] == 40 and aibombcounter1 < 39:
                aibombcounter1 = 39
            elif everything[aibomby2][aibombx2+1] == 4000 and aibombcounter3 < 39:
                aibombcounter3 = 39
            if everything[aibomby2+1][aibombx2] == 4 and bombcounter < 39:
                bombcounter = 39
            elif everything[aibomby2+1][aibombx2] == 40 and aibombcounter1 < 39:
                aibombcounter1 = 39
            elif everything[aibomby2+1][aibombx2] == 4000 and aibombcounter3 < 39:
                aibombcounter3 = 39
            if everything[aibomby2][aibombx2-1] == 4 and bombcounter < 39:
                bombcounter = 39
            elif everything[aibomby2][aibombx2-1] == 40 and aibombcounter1 < 39:
                aibombcounter1 = 39
            elif everything[aibomby2][aibombx2-1] == 4000 and aibombcounter3 < 39:
                aibombcounter3 = 39
            if everything[aibomby2-1][aibombx2] == 4 and bombcounter < 39:
                bombcounter = 39
            elif everything[aibomby2-1][aibombx2] == 40 and aibombcounter1 < 39:
                aibombcounter1 = 39
            elif everything[aibomby2-1][aibombx2] == 4000 and aibombcounter3 < 39:
                aibombcounter3 = 39
        if aibombcounter2 >= 40:
            if (aibomby2,aibombx2) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby2,aibombx2) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby2,aibombx2) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby2,aibombx2) == (newy,newx):
                alive = False
                playerpic2 = 0                                               
            if (aibomby2,aibombx2+1) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby2,aibombx2+1) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby2,aibombx2+1) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby2,aibombx2+1) == (newy,newx):
                alive = False
                playerpic2 = 0                
            if (aibomby2,aibombx2-1) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby2,aibombx2-1) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby2,aibombx2-1) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby2,aibombx2-1) == (newy,newx):
                alive = False
                playerpic2 = 0                
            if (aibomby2+1,aibombx2) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby2+1,aibombx2) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby2+1,aibombx2) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby2+1,aibombx2) == (newy,newx):
                alive = False
                playerpic2 = 0                
            if (aibomby2-1,aibombx2) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby2-1,aibombx2) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby2-1,aibombx2) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby2-1,aibombx2) == (newy,newx):
                alive = False
                playerpic2 = 0            
        if aibombcounter2 == 41:
            if rightexplosion2 == True:
                screen.blit(explosionright2,(aibombposx2,aibombposy2))
            if downexplosion2 == True:
                screen.blit(explosiondown2,(aibombposx2,aibombposy2))
            if leftexplosion2 == True:
                screen.blit(explosionleft2,(aibombposx2-35,aibombposy2))
            if upexplosion2 == True:
                screen.blit(explosionup2,(aibombposx2,aibombposy2-35))
        if aibombcounter2 == 44:
            if rightexplosion2 == True:
                screen.blit(explosionright3,(aibombposx2,aibombposy2))
            if downexplosion2 == True:
                screen.blit(explosiondown3,(aibombposx2,aibombposy2))
            if leftexplosion2 == True:
                screen.blit(explosionleft3,(aibombposx2-35,aibombposy2))
            if upexplosion2 == True:
                screen.blit(explosionup3,(aibombposx2,aibombposy2-35))                                        
        if aibombcounter2 == 46:            
            if rightexplosion2 == True:
                draw.rect(screen,(0,200,0),(aibombposx2+35,aibombposy2,35,35))
                rightexplosion2 = False
                everything[aibomby2][aibombx2+1] = 0
            if downexplosion2 == True:
                draw.rect(screen,(0,200,0),(aibombposx2,aibombposy2+35,35,35))
                downexplosion2 = False
                everything[aibomby2+1][aibombx2] = 0
            if leftexplosion2 == True:
                draw.rect(screen,(0,200,0),(aibombposx2-35,aibombposy2,35,35))
                everything[aibomby2][aibombx2-1] = 0
                leftexplosion2 = False
            if upexplosion2 == True:
                draw.rect(screen,(0,200,0),(aibombposx2,aibombposy2-35,35,35))
                upexplosion2 = False
                everything[aibomby2-1][aibombx2] = 0
            draw.rect(screen,(0,200,0),(aibombposx2,aibombposy2,35,35))
            aibombon2 = 0
            aibombframe2 = 0            
            aiexplosion2 = 0
            aibombcounter2 = 0
            aibomber2 = 0
            everything[aibomby2][aibombx2] = 0

#The BLUE AI's bomb exploding function which is very much like the human bombing function. Comments will be simplifid, refer to humanbombon() for
#a better explanation.
def aibombing3():
    global movingflag3,aibomber3,aiexplosion3,aibombon3,aibombcounter3,bombcounter,aibombcounter2,aibombcounter1,newy,newx,alive,aibombframe3,aibombposx3,aibombposy3,aibomby3,aibombx3,rightexplosion3,leftexplosion3,downexplosion3,upexplosion3,aiy1,aiy2,aiy3,aix1,aix2,aix3,newy,newx,aialive1,aialive2,aialive3,playerpic2,redpic2,blackpic2,bluepic2
    aiexplosion3 = 1        
    if aibombon3 == 1:       
        screen.blit(bomb[aibombframe3],(aibombposx3,aibombposy3))    
    if aiexplosion3 == 1:        
        aibombcounter3 += 1
        if aibombcounter3 > 20:
            aibombframe3 += 1
            if aibombframe3 == 2:
                aibombframe3 = 0
        if aibombcounter3 == 40:
            if everything[aibomby3][aibombx3] != 1:                
                draw.rect(screen,(0,200,0),(aibombposx3,aibombposy3,35,35))            
            if everything[aibomby3][aibombx3+1] != 1 and everything[aibomby3][aibombx3+1] != 4 and everything[aibomby3][aibombx3+1] != 40 and everything[aibomby3][aibombx3+1] != 400:
                rightexplosion3 = True
                screen.blit(explosionright,(aibombposx3,aibombposy3))                
            if everything[aibomby3+1][aibombx3] != 1 and everything[aibomby3+1][aibombx3] != 4 and everything[aibomby3+1][aibombx3] != 40 and everything[aibomby3+1][aibombx3] != 400:
                downexplosion3 = True
                screen.blit(explosiondown,(aibombposx3,aibombposy3))                
            if everything[aibomby3][aibombx3-1] != 1 and everything[aibomby3][aibombx3-1] != 4 and everything[aibomby3][aibombx3-1] != 40 and everything[aibomby3][aibombx3-1] != 400:
                leftexplosion3 = True
                screen.blit(explosionleft,(aibombposx3-35,aibombposy3))                
            if everything[aibomby3-1][aibombx3] != 1 and everything[aibomby3-1][aibombx3] != 4 and everything[aibomby3-1][aibombx3] != 40 and everything[aibomby3-1][aibombx3] != 400:
                upexplosion3 = True
                screen.blit(explosionup,(aibombposx3,aibombposy3-35))                
            aibombon3 = 0            
            if everything[aibomby3][aibombx3+1] == 4 and bombcounter < 39:
                bombcounter = 39
            elif everything[aibomby3][aibombx3+1] == 40 and aibombcounter1 < 39:
                aibombcounter1 = 39
            elif everything[aibomby3][aibombx3+1] == 400 and aibombcounter2 < 39:
                aibombcounter2 = 39
            if everything[aibomby3+1][aibombx3] == 4 and bombcounter < 39:
                bombcounter = 39
            elif everything[aibomby3+1][aibombx3] == 40 and aibombcounter1 < 39:
                aibombcounter1 = 39
            elif everything[aibomby3+1][aibombx3] == 4000 and aibombcounter2 < 39:
                aibombcounter2 = 39
            if everything[aibomby3][aibombx3-1] == 4 and bombcounter < 39:
                bombcounter = 39
            elif everything[aibomby3][aibombx3-1] == 40 and aibombcounter1 < 39:
                aibombcounter1 = 39
            elif everything[aibomby3][aibombx3-1] == 4000 and aibombcounter2 < 39:
                aibombcounter2 = 39
            if everything[aibomby3-1][aibombx3] == 4 and bombcounter < 39:
                bombcounter = 39
            elif everything[aibomby3-1][aibombx3] == 40 and aibombcounter1 < 39:
                aibombcounter1 = 39
            elif everything[aibomby3-1][aibombx3] == 4000 and aibombcounter2 < 39:
                aibombcounter2 = 39
        if aibombcounter3 >= 40:
            if (aibomby3,aibombx3) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby3,aibombx3) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby3,aibombx3) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby3,aibombx3) == (newy,newx):
                alive = False
                playerpic2 = 0            
            if (aibomby3,aibombx3+1) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby3,aibombx3+1) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby3,aibombx3+1) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby3,aibombx3+1) == (newy,newx):
                alive = False
                playerpic2 = 0                
            if (aibomby3,aibombx3-1) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby3,aibombx3-1) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby3,aibombx3-1) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby3,aibombx3-1) == (newy,newx):
                alive = False
                playerpic2 = 0
            if (aibomby3+1,aibombx3) == (aiy1,aix1):
                aialive1 = False
                redpic2 = 0
            if (aibomby3+1,aibombx3) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby3+1,aibombx3) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby3+1,aibombx3) == (newy,newx):
                alive = False
                playerpic2 = 0
            if (aibomby3-1,aibombx3) == (aiy1,aix1):
                aialive1 = False
                redpic2  = 0
            if (aibomby3-1,aibombx3) == (aiy2,aix2):
                aialive2 = False
                blackpic2 = 0
            if (aibomby3-1,aibombx3) == (aiy3,aix3):
                aialive3 = False
                bluepic2 = 0
            if (aibomby3-1,aibombx3) == (newy,newx):
                alive = False
                playerpic2 = 0            
        if aibombcounter3 == 41:
            if rightexplosion3 == True:
                screen.blit(explosionright2,(aibombposx3,aibombposy3))
            if downexplosion3 == True:
                screen.blit(explosiondown2,(aibombposx3,aibombposy3))
            if leftexplosion3 == True:
                screen.blit(explosionleft2,(aibombposx3-35,aibombposy3))
            if upexplosion3 == True:
                screen.blit(explosionup2,(aibombposx3,aibombposy3-35))
        if aibombcounter3 == 44:
            if rightexplosion3 == True:
                screen.blit(explosionright3,(aibombposx3,aibombposy3))
            if downexplosion3 == True:
                screen.blit(explosiondown3,(aibombposx3,aibombposy3))
            if leftexplosion3 == True:
                screen.blit(explosionleft3,(aibombposx3-35,aibombposy3))
            if upexplosion3 == True:
                screen.blit(explosionup3,(aibombposx3,aibombposy3-35))                                        
        if aibombcounter3 == 46:            
            if rightexplosion3 == True:
                draw.rect(screen,(0,200,0),(aibombposx3+35,aibombposy3,35,35))
                rightexplosion3 = False
                everything[aibomby3][aibombx3+1] = 0
            if downexplosion3 == True:
                draw.rect(screen,(0,200,0),(aibombposx3,aibombposy3+35,35,35))
                downexplosion3 = False
                everything[aibomby3+1][aibombx3] = 0
            if leftexplosion3 == True:
                draw.rect(screen,(0,200,0),(aibombposx3-35,aibombposy3,35,35))
                leftexplosion3 = False
                everything[aibomby3][aibombx3-1] = 0
            if upexplosion3 == True:
                draw.rect(screen,(0,200,0),(aibombposx3,aibombposy3-35,35,35))
                upexplosion3 = False
                everything[aibomby3-1][aibombx3] = 0
            draw.rect(screen,(0,200,0),(aibombposx3,aibombposy3,35,35))
            aibombon3 = 0
            aibombframe3 = 0            
            aiexplosion3 = 0
            aibombcounter3 = 0
            aibomber3 = 0            
            everything[aibomby3][aibombx3] = 0

#This is the doom function. When it is called upon it lays the bricks in a spiraling motion (this probably could have been done more elegantly, but it
#was a last minute thing - the first time I tried to do this I had 16 screen.blits instead of flags, so this is the lesser of two evils)
def doom():
    global everything,aiy1,aix1,aiy2,aix2,aiy3,aix3,newy,newx,bombon1,bombframe,explosion,bombcounter,aibombon1,aibombframe1,aiexplosion1,aibombcounter1,aibomber1,aibombon2,aibombframe2,aiexplosion2,aibombcounter2,aibomber2,aibombon3,aibombframe3,aiexplosion3,aibombcounter3,aibomber3,timeuntildoom,doomcounter,doomy,doomx,alive,aialive1,aialive2,aialive3,brickx,bricky,doomx,doomy,doomflag1,doomflag2,doomflag3,doomflag4,doomflag5,doomflag6,doomflag7,doomflag8,doomflag9,doomflag10,doomflag11,doomflag12,doomflag13,doomflag14,doomflag15,doomflag16
    doomcounter += 1
    #Draws only one brick (and then the screen is copied right after that)
    screen.blit(brick,(brickx,bricky))
    #If the brick lands on a bomb it deactivates the bomb by setting the bomb variables to None
    if everything[doomy][doomx] == 4:
        bombon1 = None
        bombframe = None            
        explosion = None
        bombcounter = None
        bombon = None
        bombposy = None
        bombposx = None
    if everything[doomy][doomx] == 40:
        aibombon1 = None
        aibombx1 = None
        aibomby1 = None
        aibomber1 = None
    if everything[doomy][doomx] == 400:
        aibombon2 = None
        aibombx2 = None
        aibomby2 = None
        aibomber2 = None
    if everything[doomy][doomx] == 4000:
        aibombon3 = None
        aibombx3 = None
        aibomby3 = None
        aibomber3 = None
    #Makes the position on the 2D list where the brick falls 1 - which represents a brick
    everything[doomy][doomx] = 1
    #The first row
    if doomflag1 == True:
        brickx += 35
        doomx += 1
    #The bricks then start falling in a downards motion
    elif doomflag2 == True:
        bricky += 35
        doomy += 1
    #The bricks fall to the left
    elif doomflag3 == True:
        brickx += -35
        doomx += -1
    #The bricks fall going up
    elif doomflag4 == True:
        bricky += -35
        doomy += -1
    #Bricks fall going right again skipping every other brick (since there is already a brick in every other spot)
    elif doomflag5 == True:
        brickx += 70
        doomx += 2
    #Bricks fall going down (skipping)
    elif doomflag6 == True:       
        bricky += 70
        doomy += 2
    #Bricks fall going left (skipping)
    elif doomflag7 == True:
        brickx += -70
        doomx += -2
    #Bricks fall going up (skipping)
    elif doomflag8 == True:
        bricky += -70
        doomy += -2
    #Bricks fall going right
    elif doomflag9 == True:
        brickx += 35
        doomx += 1
    #Bricks fall giong down
    elif doomflag10 == True:
        bricky += 35
        doomy += 1
    #Bricks fall going left
    elif doomflag11 == True:
        brickx += -35
        doomx += -1
    #Bricks fall going up
    elif doomflag12 == True:
        bricky += -35
        doomy += -1
    elif doomflag13 == True:
        brickx += 70
        doomx += 2
    #Bricks fall going right (skipping)
    elif doomflag14 == True:
        bricky += 70
        doomy += 2
    #Bricks fall going down (skipping)
    elif doomflag15 == True:
        brickx += -70
        doomx += -2
    #Bricks fall going left (skipping)
    elif doomflag16 == True:
        bricky += -70
        doomy += -2
    #These check when to change the direction of the falling bricks. 
    if doomcounter == 12:
        doomflag1 = False
        doomflag2 = True
    elif doomcounter == 22:
        doomflag2 = False
        doomflag3 = True
    elif doomcounter == 34:
        doomflag3 = False
        doomflag4 = True
    elif doomcounter == 43:
        doomflag4 = False
        doomflag5 = True
    elif doomcounter == 49:
        doomflag5 = False
        doomflag6 = True
        doomx += -1
        doomy += 1
        brickx += -35
        bricky += 35
    elif doomcounter == 53:
        doomflag6 = False
        doomflag7 = True
        doomy += -1
        doomx += 1
        bricky += -35
        brickx += 35
    elif doomcounter == 59:
        doomflag7 = False
        doomflag8 = True
        doomx += 1
        doomy += 1
        brickx += 35
        bricky += 35
    elif doomcounter == 63:
        doomflag8 = False
        doomflag9 = True
    elif doomcounter == 72:
        doomflag9 = False
        doomflag10 = True
    elif doomcounter == 78:
        doomflag10 = False
        doomflag11 = True
    elif doomcounter == 86:
        doomflag11 = False
        doomflag12 = True
    elif doomcounter == 91:
        doomflag12 = False
        doomflag13 = True
    elif doomcounter == 95:
        doomflag13 = False
        doomflag14 = True
        doomy += 1
        doomx += -1  
        bricky = 105
        brickx = 350
    elif doomcounter == 98:
        doomflag14 = False
        doomflag15 = True
        doomy += -1
        doomx += 1
        bricky += -35
        brickx += 35
    elif doomcounter == 102:
        doomflag15 = False
        doomflag16 = True
        doomy += -1
        doomx += 1
        bricky += -35
        brickx += 35
    elif doomcounter == 104:
        doomflag16 = False
    timeuntildoom = 0                                



#This is the function that controls the player. It calls on the movement function, bomb setting function and checks
#to see whether or not the character is alive or not. If the character is alive is calls the normal functions
#(moving and bomb setting), if it ever dies it blits the death sprite, and then sets the alive flag to None
#so the body disappears
def humanplayer():
    global alive,newy,newx,deathcounter,deathpic,bombposy,bombposx,bombcounter,explosion
    if alive == True:
        humanbombset()
        humanmovement()
        screen.blit(moves[playerpic1][playerpic2],(aa,bb))
    elif alive == False:
        newy,newx = -1,-1        
        screen.blit(moves[4][deathpic],(aa,bb))
        deathcounter += 1
        if deathcounter == 15:
            deathpic += 1
        elif deathcounter == 30:
            deathpic += 1
        elif deathcounter == 45:            
            draw.rect(screen,(0,200,0),(aa,bb,35,35))
            newy,newx = None,None
            alive = None
            bombposy,bombposx = None,None
            bombcounter,explosion = None,None
#This is the function that controls the red player AI. It calls on the movement function, bomb setting function and checks
#to see whether or not the character is alive or not. If the character is alive is calls the normal functions
#(moving and bomb setting), if it ever dies it blits the death sprite, and then sets the alive flag to None
#so the body disappears
def redplayerai():
    global aialive1,aix1,aiy1,aa2,bb2,movingflag,aibomber1,aibombposx1,aibombposy1,aibomby1,aibombx1,aibombon1,red,redpic1,redpic2,aiup1,aidown1,aileft1,airight1,aideathcounter1,aideathpic1
    if aialive1 == True:
        aix1,aiy1,aa2,bb2,movingflag,aibomber1,aibombposx1,aibombposy1,aibomby1,aibombx1,aibombon1,red,redpic1,redpic2,aiup1,aidown1,aileft1,airight1 = aimoving(aix1,aiy1,aa2,bb2,movingflag,aibomber1,aibombposx1,aibombposy1,aibomby1,aibombx1,aibombon1,red,redpic1,redpic2,aiup1,aidown1,aileft1,airight1 )
        screen.blit(redmoves[redpic1][redpic2],(aa2,bb2,35,35))
    elif aialive1 == False:
        aiy1,aiy1 = -1,-1        
        screen.blit(redmoves[4][aideathpic1],(aa2,bb2,35,35))
        aideathcounter1 += 1
        if aideathcounter1 == 15:
            aideathpic1 += 1
        elif aideathcounter1 == 30:
            aideathpic1 += 1
        elif aideathcounter1 == 45:            
            draw.rect(screen,(0,200,0),(aa2,bb2,35,35))
            aiy1,aix1 = None,None
            aibomby1,aibombx1 = None,None
            aialive1 = None
#This is the function that controls the black player AI. It calls on the movement function, bomb setting function and checks
#to see whether or not the character is alive or not. If the character is alive is calls the normal functions
#(moving and bomb setting), if it ever dies it blits the death sprite, and then sets the alive flag to None
#so the body disappears
def blackplayerai():
    global aialive2,aix2,aiy2,aa3,bb3,movingflag2,aibomber2,aibombposx2,aibombposy2,aibomby2,aibombx2,aibombon2,black,blackpic1,blackpic2,aiup2,aidown2,aileft2,airight2, aideathcounter2, aideathpic2
    if aialive2 == True:
        aix2,aiy2,aa3,bb3,movingflag2,aibomber2,aibombposx2,aibombposy2,aibomby2,aibombx2,aibombon2,black,blackpic1,blackpic2,aiup2,aidown2,aileft2,airight2 = aimoving(aix2,aiy2,aa3,bb3,movingflag2,aibomber2,aibombposx2,aibombposy2,aibomby2,aibombx2,aibombon2,black,blackpic1,blackpic2,aiup2,aidown2,aileft2,airight2 )
        screen.blit(blackmoves[blackpic1][blackpic2],(aa3,bb3,35,35))
    elif aialive2 == False:
        aiy2,aiy2 = -1,-1        
        screen.blit(blackmoves[4][aideathpic2],(aa3,bb3,35,35))
        aideathcounter2 += 1
        if aideathcounter2 == 15:
            aideathpic2 += 1
        elif aideathcounter2 == 30:
            aideathpic2 += 1
        elif aideathcounter2 == 45:            
            draw.rect(screen,(0,200,0),(aa3,bb3,35,35))
            aiy2,aix2 = None,None
            aibomby2,aibombx2 = None,None
            aialive2 = None
#This is the function that controls the blue player AI. It calls on the movement function, bomb setting function and checks
#to see whether or not the character is alive or not. If the character is alive is calls the normal functions
#(moving and bomb setting), if it ever dies it blits the death sprite, and then sets the alive flag to None
#so the body disappears
def blueplayerai():
    global aialive3,aix3,aiy3,aa4,bb4,movingflag3,aibomber3,aibombposx3,aibombposy3,aibomby3,aibombx3,aibombon3,blue,bluepic1,bluepic2,aiup3,aidown3,aileft3,airight3,aideathcounter3,aideathpic3
    if aialive3 == True:
        aix3,aiy3,aa4,bb4,movingflag3,aibomber3,aibombposx3,aibombposy3,aibomby3,aibombx3,aibombon3,blue,bluepic1,bluepic2,aiup3,aidown3,aileft3,airight3 = aimoving(aix3,aiy3,aa4,bb4,movingflag3,aibomber3,aibombposx3,aibombposy3,aibomby3,aibombx3,aibombon3,blue,bluepic1,bluepic2,aiup3,aidown3,aileft3,airight3 )    
        screen.blit(bluemoves[bluepic1][bluepic2],(aa4,bb4,35,35))
    elif aialive3 == False:
        aiy3,aiy3 = -1,-1                
        screen.blit(bluemoves[4][aideathpic3],(aa4,bb4,35,35))
        aideathcounter3 += 1
        if aideathcounter3 == 15:
            aideathpic3 += 1
        elif aideathcounter3 == 30:
            aideathpic3 += 1
        elif aideathcounter3 == 45:            
            draw.rect(screen,(0,200,0),(aa4,bb4,35,35))
            aiy3,aiy3 = None,None
            aibomby3,aibombx3 = None,None
            aialive3 = None

#This checks to see if the bomb flags from the AI bombing variables are set off. If they are, then it calls on the bombing
#function. 
def allaibombing():
    if aibomber1 == 1:
        aibombing1()
    if aibomber2 == 1:
        aibombing2()
    if aibomber3 == 1:
        aibombing3()

#This is the counter that keeps track of the total time the game has been running. When it reaches a certain time
#(when the counter hits 2k) it starts the doom function which makes bricks fall
def doomsday():
    global timeuntildoom,playingtime
    playingtime += 1
    if playingtime > 2000:
        timeuntildoom += 1
        if timeuntildoom == 10:
            doom()

#This is checking if any of the falling bricks from the doomsday function kill any of the players
def superdeathchecker():
    global alive,aialive1,aialive2,aialive3
    if alive == True:
        if everything[newy][newx] == 1:
            alive = False
    if aialive1 == True:
        if everything[aiy1][aix1] == 1:
            aialive1 = False
    if aialive2 == True:
        if everything[aiy2][aix2] == 1:
            aialive2 = False
    if aialive3 == True:
        if everything[aiy3][aix3] == 1:
            aialive3 = False

#This keeps checking if the player is alive and the other three players are dead (win) or if the player is dead (lose)
def conclusion():
    global aialive1,aialive2,aialive3
    if alive == None:
        screen.blit(lose,(-10,50))
        display.flip()
        time.wait(2000)
        quit()
    elif aialive1 == None and aialive2 == None and aialive3 == None:
        screen.blit(win,(-10,50))
        display.flip()
        time.wait(2000)
        quit()

#MAIN GAME LOOP <(^_^<)
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
            quit()
    screen.set_clip(Rect(35,35,490,490-35-35))
    keys = key.get_pressed()
    superdeathchecker()
    humanplayer()
    redplayerai()
    blackplayerai()            
    blueplayerai()        
    display.flip()
    screen.blit(copied,Rect(0,0,525,525))
    humanbombon()
    allaibombing()
    doomsday()
    conclusion()
    copied = screen.copy()
    myClock.tick(30)
    
