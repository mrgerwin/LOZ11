from pygame_functions9 import *
"""
1.8.1 Bug Fixes
-When link gets hit, he doesn't end up inside of a wall or off the scene
"""
HUD_Height = 32
tile_size = 32
screen_width=tile_size*32
screen_height=tile_size*24 + HUD_Height

screenSize(screen_width,screen_height)
HealthLabel = makeLabel("Health = 6", 32, 50, 8, "white", "system")
RupeeLabel = makeLabel("Rupee = 0", 32, 200, 8, "white", "system")
setAutoUpdate(False)
link = Player()
sword = Sword(link)
heart1 = Heart()
rupee = Rupee()
brupee = BlueRupee()


heart1.move(64, 350)
rupee.move(128, 350)
brupee.move(96, 350)



scene1 = Scene(link, "ZeldaMapTilesBrown.png", "map.txt", 6,8)
showBackground(scene1)
showSprite(heart1)
showSprite(rupee)
showSprite(brupee)
showSprite(link)
scene1.Items=[heart1, rupee, brupee]
for enemy in scene1.Enemies:
    showSprite(enemy)

showLabel(HealthLabel)
showLabel(RupeeLabel)

nextFrame = clock()
frame = 0

while True:
    if clock() >nextFrame:
        frame= (frame + 1)%2
        nextFrame += 80
        pause(10)
        
        for wall in scene1.Wall_Tiles:
            if touching(wall, link):
                link.speed = -link.speed
                link.move(frame)
                link.speed = - link.speed
        
        if keyPressed("down"):
            
            link.orientation =0
            link.move(frame)
        elif keyPressed("up"):
            link.orientation =1
            link.move(frame)
        elif keyPressed("right"):
            link.orientation =2
            link.move(frame)
        elif keyPressed("left"):
            link.orientation =3
            link.move(frame)
        elif keyPressed("space"):
            changeSpriteImage(link, link.orientation + 8)
        #Sword Swing Code
            sword.swing()
            for enemy in scene1.Enemies:
                if touching(sword, enemy):
                    if enemy.health == 1:
                        scene1.Enemies.remove(enemy)
                        link.kills += 1
                        itemDrop = dropChart(link.kills)
                        print(itemDrop)
                        if itemDrop == 0:
                            aRupee = Rupee()
                            aRupee.move(enemy.rect.x, enemy.rect.y)
                            scene1.Items.append(aRupee)
                            showSprite(aRupee)
                        elif itemDrop == 1:
                            aHeart = Heart()
                            aHeart.move(enemy.rect.x, enemy.rect.y)
                            scene1.Items.append(aHeart)
                            showSprite(aHeart)
                        elif itemDrop == 2:
                            pass
                            #To Do Program Fairy
                        elif itemDrop == 3:
                            pass
                            #To Do Program Bomb
                        elif itemDrop == 4:
                            pass
                            #To Do Program Timer
                        elif itemDrop ==5:
                            aBRupee = BlueRupee()
                            aBRupee.move(x,y)
                            scene1.Items.append(aBRupee)
                            showSprite(aBRupee)
                    enemy.hit()
        if not keyPressed("space") or keyPressed("left") or keyPressed("right") or keyPressed("up") or keyPressed("down"):
            hideSprite(sword)
        if keyPressed("h"):
            changeSpriteImage(link, frame+12)
        
        for enemy in scene1.Enemies:
            enemy.move(frame)            
            if touching(enemy, link):
                link.hit(scene1.Wall_Tiles)
            for wall in scene1.Wall_Tiles:
                while touching(enemy, wall) or enemy.rect.x > screen_width or enemy.rect.y>screen_height or enemy.rect.x<0 or enemy.rect.y<0:
                    enemy.turn()
                    enemy.move(frame)
        for item in scene1.Items:
            item.animate(frame)
            if touching(item, link):
                link.collect(item)
                scene1.Items.remove(item)
                killSprite(item)
                changeLabel(HealthLabel, "Health = " + str(link.health))
                changeLabel(RupeeLabel, "Rupee = " + str(link.rupee))
        updateDisplay()

endWait()