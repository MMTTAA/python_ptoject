from ast import Try, While
import random
import os
from time import sleep
from warnings import catch_warnings


class Girl:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def right(self):
        self.x += 1

    def down(self):
        self.y += 1
    
    def move(self, x, y):
        self.y += y
        self.x += x

girl = Girl(-10,-10)

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def right(self):
        self.x += 1

    def left(self):
        self.x -= 1

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1
    
    def move(self, x, y):
        self.y += y
        self.x += x

class Commanderg:
    def move (self,who):
        x = random.randrange(0,2)
        y = random.randrange(0,2)
        who.move(x,y)

commanderg = Commanderg()


class Commander:
    def move(self, who):
        x = random.randint(-1, 1) # -1, 0, 1
        y = random.randint(-1, 1) # -1, 0, 1
        who.move(x, y)


commander = Commander()

robots = []
for i in range(5):
    robots.append(Robot(0, 0))

while True:
 
    os.system('CLS')

    catch = False
    
    for y in range(-10,11):
        for x in range(-10,11):
            foundg = False
            foundr = False 

            for robot in robots:
                if robot.x == x and robot.y == y:
                    foundr = True
                if robot.x == girl.x and robot.y == girl.y:
                    catch = True

            if girl.x == x and girl.y == y:
                foundg = True

            if foundr == True:
                print('🤖', end='')
            elif foundg == True: 
                print('👩', end='')
            else:
                print('🌵', end='')

            

        print('')

    if girl.x == 11 or girl.y == 11:
        print("Девочка выжила, вы победили!")
        break

    for robot in robots:
        commander.move(robot)

    commanderg.move(girl)

     
   
    if catch == True:
        print("Игра окончена, девочку поймали!")
        break

    sleep(0.5)