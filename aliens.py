from turtle import Turtle
from random import choice


class Invaders:

    def __init__(self):

        self.attack = False
        self.x_move = 15
        self.alien_list = []
        self.missile_list = []
        self.build_invaders()

    def create_alien(self, axis_x, axis_y):
        """A function that creates a red alien invader at a specified position"""

        self.alien_list.append(Turtle("turtle"))
        self.alien_list[-1].penup()
        self.alien_list[-1].color("red")
        self.alien_list[-1].setpos(axis_x, axis_y)
        self.alien_list[-1].setheading(270)

    def build_invaders(self):
        """A function that builds out all the aliens"""

        self.alien_list.clear()
        x_pos = -140

        for i in range(7):
            self.create_alien(x_pos, 280)
            self.create_alien(x_pos, 250)
            self.create_alien(x_pos, 220)
            self.create_alien(x_pos, 190)

            x_pos += 45

    def move(self):
        """A function that moves the aliens left and right"""

        count = 0

        for alien in self.alien_list:

            new_x = alien.xcor() + self.x_move
            alien.setx(new_x)

            if alien.xcor() > 275:

                count += 1

                if len(self.alien_list) <= 10:
                    self.x_move *= -1
                    self.move_down()

                if count % 4 == 0:
                    self.x_move *= -1
                    self.move_down()

            elif alien.xcor() < -275:

                self.alien_list[0].setx(-260)
                self.x_move *= -1

    def move_down(self):
        """A function that moves the aliens towards the spaceship"""

        for alien in self.alien_list:
            alien.forward(10)

    def shoot(self):
        """A function that fires a missile from a random alien"""

        rand_alien = choice(self.alien_list)

        self.attack = True
        sos_pos = rand_alien.pos()

        self.missile_list.append(Turtle())
        self.missile_list[-1].penup()
        self.missile_list[-1].hideturtle()
        self.missile_list[-1].setpos(sos_pos)
        self.missile_list[-1].setheading(270)
        self.missile_list[-1].forward(20)
        self.missile_list[-1].dot(7, "red")

    def move_missile(self):
        """A function that moves all the missiles towards the spaceship"""

        for missile in self.missile_list:
            missile.clear()
            missile.forward(20)
            missile.dot(7, "red")
