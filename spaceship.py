from turtle import Turtle


class SpaceShip:

    def __init__(self):

        self.osaro = Turtle()
        self.osaro.shape("triangle")
        self.osaro.penup()
        self.osaro.color("green")
        self.osaro.setheading(90)
        self.osaro.setpos((0, -200))

        self.attack = False
        self.bullet_list = []

    def move_left(self):
        """A function that move the spaceship left"""

        if self.osaro.xcor() < -270:
            self.osaro.setx(-278)
        else:
            new_x = self.osaro.xcor() - 20
            self.osaro.setx(new_x)

    def move_right(self):
        """A function that move the spaceship right"""

        if self.osaro.xcor() > 270:
            self.osaro.setx(278)
        else:
            new_x = self.osaro.xcor() + 20
            self.osaro.setx(new_x)
            
    def shoot(self):
        """A function that fires bullets from the spaceship"""
        self.attack = True
        osaro_pos = self.osaro.pos()

        self.bullet_list.append(Turtle())
        self.bullet_list[-1].penup()
        self.bullet_list[-1].hideturtle()
        self.bullet_list[-1].setpos(osaro_pos)
        self.bullet_list[-1].setheading(90)
        self.bullet_list[-1].forward(20)
        self.bullet_list[-1].dot(7, "green")

    def move_bullet(self):
        """A function that moves the bullets towards the aliens"""

        for bullet in self.bullet_list:

            bullet.clear()
            bullet.forward(20)
            bullet.dot(7, "green")
