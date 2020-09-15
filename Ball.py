class Ball:
    delay = 0
    
    def __init__(self, canvas):
        self.state = "move"
        self.speed = 5
        self.size = 20
        self.x = 180
        self.y = 600 - (self.size/2 + 1)
        self.dx = 0
        self.dy = 0
        
        self.delay = Ball.delay = 0.5 # 비동기적으로 움직일떄 딜레이
        Ball.delay += 0.5
        
        self.canvas = canvas
        
        self.canvas.create_oval(self.x - self.size/2, self.y - self.size/2, self.x + self.size/2, self.y + self.size/2,
                                fill="yellow", tag="ball")
         
    def display(self):
        if self.state != "move":
            return
        
        self.canvas.create_oval(self.x - self.size/2, self.y - self.size/2, self.x + self.size/2, self.y + self.size/2,
                                fill="yellow", tag="ball")
    