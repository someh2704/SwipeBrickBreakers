from Ball import Ball
from Brick import Brick
from random import randint, sample

class GameObject:
    def __init__(self, canvas):
        self.canvas = canvas
        self.stage = 1
        self.ball_list = [Ball(self.canvas)] 
        self.brick_list = [Brick(self.canvas, randint(0, 5), 0)]
        
    def display(self):
        for ball in self.ball_list:
            ball.display()
            
        for brick in self.brick_list:
            brick.display()
        
    def brick_move(self):
        for brick in self.brick_list:
            brick.move()

    def delete(self):
        for brick in self.brick_list:
            y = (brick.y - 120) / brick.height
            print(y, end = ' ')
            if brick.life == 0:
                brick.state = "dead"
            
            elif int((brick.y - 120) / brick.height) == 10:
                brick.state = "dead"
        print('-' * 10)
        next_list = []
        
        for brick in self.brick_list:
            if brick.state == "alive":
                next_list.append(brick)
                
        self.brick_list = next_list[:]
    
    def create_brick(self):
        self.stage += 1
        temp = sample([0, 1, 2, 3, 4, 5], randint(1, 5))
        print(temp)
        for num in temp:
            self.brick_list.append(Brick(self.canvas, num, 0))
    
    def next_stage(self):
        self.create_brick()