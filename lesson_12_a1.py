import turtle

screen = turtle.getscreen()
t = turtle.Turtle()

class Worker:
    def build(self, step, sides):
        """
        input: step - size, sides (4 == square)
        """
        t.pendown()
        for _ in range(sides):
            t.forward(step)
            t.left(360 // sides)

class Foreman(Worker):
    def __init__(self, wall):
        self.wall = wall

class Roofman(Worker):
    def __init__(self, roof):
        self.roof = roof
        self.roof_base = 0

    def find_roof_base(self, base):
        t.penup()
        t.goto(0, base['size'])

class Doorman(Worker):
    def __init__(self, door):
        self.door = door
        self.door_base = 0

    def find_door_base(self, base):
        t.penup()
        t.goto(base['size'] // 2, 0)

wall_size = int(input('Введите размер для стен (макс: 100): '))

ideas = {
    'wall': {'size': wall_size},
    'roof': {'size': wall_size},
    'door': {'size': wall_size / 4}
    }

wall_builder = Foreman(wall=ideas['wall'])
wall_builder.build(step=wall_builder.wall['size'], sides=4)

roof_builder = Roofman(roof=ideas['roof'])
roof_builder.find_roof_base(ideas['wall'])
roof_builder.build(step=roof_builder.roof['size'], sides=3)

door_builder = Doorman(door=ideas['door'])
door_builder.find_door_base(ideas['wall'])
door_builder.build(step=door_builder.door['size'], sides=4)

screen.mainloop()

