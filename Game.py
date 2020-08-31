from tkinter import *
from Ball import *
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Swipe Brick Breakers")
        
        self.width = 360
        self.height = 720
        
        self.under = 600
        self.top = 120
        
        self.score = 0
        self.maxScore = 0
        
        self.canvas = Canvas(self.tk, width=self.width, height=self.height)
        self.canvas.pack()
        
        self.maxScore_var = StringVar()
        self.score_var = StringVar()
        
        self.maxScore_label = Label(self.tk, font=("나눔고딕", 15), textvariable=self.maxScore_var)
        self.score_label = Label(self.tk, font=("나눔고딕", 15), textvariable=self.score_var)
        
        
        self.score_label.pack()
        self.maxScore_label.pack()
        
        self.score_label.place(x=120, y=0)
        self.maxScore_label.place(x=120, y=30)
        
        self.ballList = [Ball(self.canvas)]
        
    def move(self):
        for ball in self.ballList:
            ball.move()
            time.sleep()
        
    def display(self):
        self.maxScore_var.set(f"최고점수: {self.maxScore}")
        self.score_var.set(f"현재점수: {self.score}")
        
        self.canvas.delete("ball")
        
        for ball in self.ballList:
            ball.display()
        
        self.tk.update()
    
    def mainLoop(self):
        
        self.canvas.create_line(0, self.top, self.width, self.top, width=3)
        self.canvas.create_line(0, self.under, self.width, self.under, width=3)
        
        while True:
            self.display()
            time.sleep(0.005)
            
            
if __name__ == '__main__':
    g = Game()
    g.mainLoop()