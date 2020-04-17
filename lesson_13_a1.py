from random import randint
from turtle import Turtle, getscreen, speed, penup, goto

class Field(Turtle):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.speed(0)
        self.penup()
        self.goto(-140, 140)
        
    def build_field(self):
        for step in range(self.size):
            self.write(step, align='center')
            self.right(90)
            for num in range(8):
                self.penup()
                self.forward(10)
                self.pendown()
                self.forward(10)
            self.penup()
            self.backward(160)
            self.left(90)
            self.forward(20)

class MyTurtle(Field):
    def __init__(self, color, position):
        super().__init__(self)
        self.color(color)
        self.shape('turtle')
        self.penup()
        self.goto(position[0], position[1])
        self.pendown()
        self.score = 0

    def set_score(self, score):
        self.score += score

    def get_score(self):
        return self.score

    def winner(self, other):
        for o in other:
            o.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.pendown()
        style = ('Courier', 30, 'italic')
        self.write('WINNER', font=style, align='center')

screen = getscreen()
screen.bgcolor("green")

field_size = int(input('Какого размера будет поле (максимум 100): '))
f = Field(field_size // 7)
f.build_field()

LE = MyTurtle('blue', (-160, 100))
ML = MyTurtle('yellow', (-160, 70))
DN = MyTurtle('purple', (-160, 40))
RP = MyTurtle('red', (-160, 10))

racers = [LE, ML, DN, RP]

for r in range(field_size):
    for racer in racers:
        racer_move = randint(1, 5)
        racer.forward(racer_move)
        racer.set_score(racer_move)

final_score = 0
finalist = None

for t in racers:
    if t.get_score() > final_score:
        final_score = t.get_score()
        finalist = t

racers.pop(racers.index(finalist))
finalist.winner(racers)

screen.mainloop()


