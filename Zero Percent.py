from gamelib import *

game=Game(580,400,"Zero Percent")

'''Maps'''
Festival=Image("images//Festival.png",game)
Town=Image("images//Tunnel.png",game)
Town.resizeBy(-40)
Festival.resizeBy(10)
WalkingLink = Animation("images//Linkanimation.png",11,game,288/12,256/8)
WalkingLink.resizeBy(50)
WalkingLink.moveTo(game.width/2, game.height-100)
Son= Animation("images//sonis.png",3,game,172/3,183/3,3,3)
Son2= Animation("images//sonis.png",3,game,172/3,183/3,3)

Heart1=("images//Heart1.png",game)
Heart2=("images//Heart2.png",game)
Heart3=("images//Heart3.png",game)








WalkingLink2 = Animation("images\\Walkinglink2.png",11,game,285/12,27)
WalkingLink2.resizeBy(50)
WalkingLink2.moveTo(game.width/2, game.height-100)
Linksword1 = Animation("images\\Swordlink1.png",6,game,293/7,37/1)
Linksword1.resizeBy(50)
Linksword1.moveTo(game.width/2, game.height-100)



Linksword3 = Animation("images\\Swordlink3.png",6,game,244/6.05,32/1)
Linksword3.resizeBy(50)
Linksword3.moveTo(WalkingLink.x,WalkingLink.y)


Son2.resizeBy(-30)
Son2.moveTo(Son.x,Son.y)
Son2.visible=False
WalkingLink3 = Animation("images\\Walkinglink3.png",11,game,285/12,28)
WalkingLink3.resizeBy(50)
WalkingLink3.moveTo(game.width/2, game.height-100)

WalkingLink4 = Animation("images\\Walkinglink4.png",11,game,285/12,28)
WalkingLink4.resizeBy(50)
WalkingLink4.moveTo(game.width/2, game.height-100)
Son.resizeBy(-30)
Son.moveTo(game.width/1.88, game.height-380)
Road= Image("images//Road.png",game)
Road.resizeBy(10)
Border1=Image("images//border1.png",game)
Border2=Image("images//border3.png",game)
Border1.visible=False
Border2.visible=False
Sherk = Animation("images\\NPC2.png",6,game,368/8.1,56,5)
Sherk.resizeBy(10)
Sherk.setSpeed(0,-90)
Sherk.moveTo(100,150)
Sherk1= Animation("images//NPC1.png",4,game,139/4,47/1,2)
Sherk.moveTo(Sherk1.x,Sherk1.y)
Sherk.visible=True
Sherk1.visible=True
screen = 1
Linksword1.draw()
Linksword1.resizeBy(30)
Sherk1.resizeBy(20)
Roll= Animation("images//LinkRoll.png",5, game,178/7,23/1)
Roll.resizeBy(50)
linkroll = Animation("images\\LinkRoll.png",6,game,178/6,23)
linkroll.resizeBy(50)
Shrek = Animation("images\\Shrek.png",1,game, 44/1.2,48)
while not game.over:
    Sherk1.visible=True
    Sherk1.draw()
    Sherk.draw()
    

    game.processInput()
    if screen == 1:
        Festival.draw()
        Border1.moveTo(game.height-20,game.width-100)
        Border2.moveTo(game.height-200,game.width-100)
        Sherk1.moveTo(Border1.x-20, Border1.y)
        
    elif screen == 2:
        Road.draw()
        Border2.moveTo(game.height-10,game.width-100)
        Border1.moveTo(game.height-370, game.width-100)
       
    elif screen== 3: 
        Border2.moveTo(game.height+175,game.width-300)
        Border1.moveTo(game.height-400, game.width-100)
        Town.draw()
        if Sherk1.isOffScreen("all"):
            Sherk1.moveTo(WalkingLink.x-100,WalkingLink.y)
        game.drawText("Health :" + str(Sherk1.health), 250, 350)    
    if WalkingLink.collidedWith(Sherk1) or WalkingLink2.collidedWith(Sherk1):
        Sherk1.visible=False
        Sherk.visible=True
        WalkingLink.health-=1
    if WalkingLink3.collidedWith(Sherk1):
        Sherk1.visible=False
        Sherk.visible=True
        WalkingLink.health-=1
    if WalkingLink4.collidedWith(Sherk1):
        Sherk1.visible=False
        Sherk.visible=True
        WalkingLink.health-=1  
    else:
        Sherk1.visible=True
        Sherk.visible=False
        
        
    if WalkingLink.health < 0:
        Sherk1.resizeBy(10)
        game.quit()
    if Sherk1.health <0:
        WalkingLink.resizeBy(5)
        game.quit()
    WalkingLink.draw()
    Son.draw()
    Son2.draw()
    Border1.draw()
    Border2.draw()
    
    
        
        

    
    
    
    
    if WalkingLink2.collidedWith (Border1,"rectangle")or WalkingLink2.collidedWith (Border2,"rectangle"):
        WalkingLink2.moveTo(game.width/2, game.height-100)
    if WalkingLink.collidedWith (Border2,"rectangle")or WalkingLink.collidedWith(Border1,"rectangle"):
        WalkingLink.moveTo(game.width/2, game.height-100)
    if WalkingLink4.collidedWith (Border2,"rectangle")or WalkingLink4.collidedWith(Border1,"rectangle"):
        WalkingLink4.moveTo(game.width/2, game.height-100)    
        
        
        
 
    if keys.Pressed[K_a]: 
       WalkingLink4.nextFrame()
       WalkingLink4.x-=2
       WalkingLink4.visible= True
       WalkingLink2.visible = False
       WalkingLink3.visible = False
       Linksword1.visible=False
       Linksword3.visible=False
       linkroll.visible=False
       WalkingLink3.moveTo(WalkingLink4.x,WalkingLink4.y)
       WalkingLink2.moveTo(WalkingLink4.x,WalkingLink4.y)
       WalkingLink.visible=False
       WalkingLink.moveTo(WalkingLink2.x,WalkingLink2.y)
       Linksword1.moveTo(WalkingLink4.x,WalkingLink4.y)
       Linksword3.moveTo(WalkingLink4.x,WalkingLink4.y)

    elif keys.Pressed[K_d]:
       WalkingLink2.nextFrame()
       WalkingLink2.x+=2
       WalkingLink2.visible= True
       WalkingLink4.visible= False
       WalkingLink3.visible= False
       WalkingLink.visible=False
       Linksword1.visible=False
       Linksword3.visible=False
       linkroll.visible=False
       WalkingLink.moveTo(WalkingLink2.x,WalkingLink2.y)
       WalkingLink4.moveTo(WalkingLink2.x,WalkingLink2.y)
       WalkingLink3.moveTo(WalkingLink2.x,WalkingLink2.y)
       WalkingLink2.moveTo(WalkingLink2.x,WalkingLink2.y)
       WalkingLink.visible=False
       WalkingLink.moveTo(WalkingLink2.x,WalkingLink2.y)
       Linksword1.moveTo(WalkingLink2.x,WalkingLink2.y)
       Linksword3.moveTo(WalkingLink2.x,WalkingLink2.y)
    
    elif keys.Pressed[K_s]:
        WalkingLink3.nextFrame()
        WalkingLink3.y+=2
        WalkingLink3.visible=True
        WalkingLink2.visible=False 
        WalkingLink4.visible= False
        WalkingLink.visible=False
        Linksword1.visible=False
        Linksword3.visible=False
        linkroll.visible=False
        WalkingLink.moveTo(WalkingLink3.x,WalkingLink3.y)
        WalkingLink4.moveTo(WalkingLink3.x,WalkingLink3.y)
        WalkingLink2.moveTo(WalkingLink3.x,WalkingLink3.y)
        WalkingLink3.moveTo(WalkingLink3.x,WalkingLink3.y)
        Linksword1.moveTo(WalkingLink3.x,WalkingLink3.y)
        Linksword3.moveTo(WalkingLink3.x,WalkingLink3.y)
       



        
    elif keys.Pressed[K_w]:
        WalkingLink.nextFrame()
        WalkingLink.y-=2
        WalkingLink.visible=True
        WalkingLink3.visible=False
        WalkingLink2.visible=False 
        WalkingLink4.visible= False
        Linksword1.visible=False
        Linksword3.visible=False
        linkroll.visible=False
        WalkingLink4.moveTo(WalkingLink.x,WalkingLink.y)
        WalkingLink2.moveTo(WalkingLink.x,WalkingLink.y)
        WalkingLink3.moveTo(WalkingLink.x,WalkingLink.y)
        Linksword1.moveTo(WalkingLink.x,WalkingLink.y)
        Linksword3.moveTo(WalkingLink.x,WalkingLink.y)
        
        
    elif keys.Pressed[K_j]:
        Linksword3.nextFrame()
        Linksword3.visible= True
        WalkingLink.visible=False
        WalkingLink2.visible=False
        WalkingLink3.visible=False
        WalkingLink4.visible=False    
        Linksword1.moveTo(Linksword3.x,Linksword3.y)
        WalkingLink4.moveTo(Linksword3.x,Linksword3.y)
        WalkingLink2.moveTo(Linksword3.x,Linksword3.y)
        WalkingLink3.moveTo(Linksword3.x,Linksword3.y)
    #The Roll is NON-FUNCTION    
    elif keys.Pressed[K_q]:
        linkroll.nextFrame()
        linkroll.x -= 4
        linkroll.setSpeed(5,90)
        linkroll.visible=False
        WalkingLink.visible=False
        WalkingLink3.visible=False
        WalkingLink2.visible=False 
        WalkingLink4.visible= False
        Linksword3.visible=False
        linkroll.moveTo(WalkingLink.x,WalkingLink.y)
        linkroll.moveTo(WalkingLink2.x,WalkingLink2.y)
        linkroll.moveTo(WalkingLink3.x,WalkingLink3.y)
        linkroll.moveTo(WalkingLink4.x,WalkingLink4.y)
        linkroll.moveTo(Linksword3.x,Linksword3.y)
    else:
        WalkingLink.visible=True
        WalkingLink.draw()  
    if WalkingLink.collidedWith(Son) or WalkingLink2.collidedWith(Son): 
        Son.moveTo(game.width/3, game.height-380)
        Son2.moveTo(Son.x,Son.y)
        Son.visible=False
        Son2.visible=True 
        screen = 2
        Sherk1.visible=False 
        WalkingLink.moveTo(game.width/2, game.height-100)
        WalkingLink.visible= True
        WalkingLink2.moveTo(game.width/2, game.height-100)
    if WalkingLink.x<300 and  WalkingLink.collidedWith(Son):
        WalkingLink.moveTo(game.width/2, game.height-100)
    if WalkingLink.x>200 and  WalkingLink.collidedWith(Son):
        WalkingLink.moveTo(game.width/2, game.height-100)
    if WalkingLink.collidedWith(Son2) or WalkingLink2.collidedWith(Son2):
        Son2.visible=False
        Son.setSpeed(20,-180)
        Son2.setSpeed(20,-180)
        screen = 3
        Sherk.moveTo(Sherk1.x,Sherk1.y)
        WalkingLink.moveTo(game.width/2, game.height-100)
        Sherk1.setSpeed(5,-90)
    Sherk1.move(False)
    Sherk.moveTo(Sherk1.x,Sherk1.y)

    if Linksword3.collidedWith(Sherk1) or Linksword3.collidedWith(Sherk):
        Shrek.nextFrame()
        Shrek.moveTo(Sherk1.x,Sherk1.y)
        Shrek.moveTo(Sherk.x,Sherk.y)
        Sherk1.visible=False
        Sherk.visible=False
        Sherk1.health-=1
    else:
        Sherk1.visible=True
        
    
    game.drawText("Health :" + str(WalkingLink.health), 200,5)
    
  
       
        
    
     
           
    game.update(200)
game.quit()    
        
