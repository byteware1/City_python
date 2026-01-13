import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("2 Homes, Road, and Tree - OOP Style")

class Drawer:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(10)
    
    def rectangle(self, color, x, y, width, height):
        t = self.t
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()
    
    def triangle(self, color, x, y, width, height):
        t = self.t
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.goto(x + width/2, y + height)
        t.goto(x + width, y)
        t.goto(x, y)
        t.end_fill()
    
    def circle(self, color, x, y, radius):
        t = self.t
        t.penup()
        t.goto(x, y - radius)  # center correction
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
    
    def line(self, color, x, y, length, pensize=1):
        t = self.t
        t.pensize(pensize)
        t.pencolor(color)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(length)
        t.pensize(1)
        t.pencolor("black")

class Road:
    def __init__(self, drawer):
        self.drawer = drawer
    
    def draw(self, x=-300, y=-100, width=600, height=80):
        d = self.drawer
        d.rectangle("gray", x, y, width, height)
        # Draw stripes
        stripe_width = 40
        for i in range(x, x + width, 80):
            d.line("white", i, y + 40, stripe_width, pensize=3)

class House:
    def __init__(self, drawer, body_color, roof_color, x, y, width=120, height=100, roof_height=60):
        self.d = drawer
        self.body_color = body_color
        self.roof_color = roof_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.roof_height = roof_height
    
    def draw(self):
        d = self.d
        # House body
        d.rectangle(self.body_color, self.x, self.y, self.width, self.height)
        # Roof
        d.triangle(self.roof_color, self.x, self.y + self.height, self.width, self.roof_height)
        # Windows
        d.rectangle("white", self.x + 15, self.y + 45, 15, 15)
        d.rectangle("white", self.x + 55, self.y + 45, 15, 15)
        # Door
        d.rectangle("brown", self.x + 30, self.y, 30, 40)

class Tree:
    def __init__(self, drawer, trunk_x=-10, trunk_y=-100):
        self.d = drawer
        self.trunk_x = trunk_x
        self.trunk_y = trunk_y
    
    def draw(self):
        d = self.d
        # Trunk
        d.rectangle("brown", self.trunk_x, self.trunk_y, 20, 60)
        # Foliage
        d.circle("green", self.trunk_x + 10, self.trunk_y + 90, 30)
        d.circle("green", self.trunk_x - 10, self.trunk_y + 50, 30)
        d.circle("green", self.trunk_x + 30, self.trunk_y + 50, 30)

# --- Draw scene ---
drawer = Drawer()

# Road
road = Road(drawer)
road.draw()

# Houses
house1 = House(drawer, "orange", "red", -250, -20)
house1.draw()
house2 = House(drawer, "yellow", "brown", 100, -10, roof_height=50)
house2.draw()

# Tree
tree = Tree(drawer)
tree.draw()

# Hide turtle
drawer.t.hideturtle()
turtle.done()
