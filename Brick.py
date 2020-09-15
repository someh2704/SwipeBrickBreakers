from uuid import uuid4

class Brick:
    color = ["#ff9281", "#ff7b5a", "#ff4040", "#ff0000", "#df0000"]
    def __init__(self, canvas, x, y):
        self.width = 60
        self.height = 48
        self.x = self.width*x
        self.y = 120 + self.height*y
        
        self.uuid = str(uuid4())
        self.life = 1
        self.state = "alive"
        self.color = Brick.color[0]
        
        self.canvas = canvas
        
    def display(self):
        if(self.life < 160):
            self.color = Brick.color[self.life // 40]
        else:
            self.color = Brick.color[4]
        
        self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                     fill=self.color, tag=self.uuid)
        
    def move(self):
        self.canvas.delete(self.uuid)
        self.y += self.height