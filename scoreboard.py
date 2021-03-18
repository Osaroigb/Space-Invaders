from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):

        super().__init__()

        self.user_score = 0
        self.lives = 3
        self.display_score()

    def display_score(self):
        """A function that displays the scoreboard"""

        self.penup()
        self.color("green")
        self.hideturtle()

        self.setpos(-300, -250)
        self.setheading(0)
        self.pensize(3)

        self.pendown()
        self.forward(590)
        self.penup()

        self.setpos(220, -300)
        self.write(f"Score:{self.user_score}", False, "center", ("Courier", 20, "normal"))

        self.setpos(-230, -300)
        self.write(f"Lives:{self.lives}", False, "center", ("Courier", 20, "normal"))

    def update_score(self):
        """A function that updates the score by 1 point whenever a bullet kills an alien"""

        self.clear()
        self.user_score += 1
        self.display_score()

    def update_live(self):
        """A function that reduces spaceship by 1 whenever a missile kills a spaceship"""

        self.clear()
        self.lives -= 1
        self.display_score()

    def losing_message(self):
        """A function that displays the losing message"""

        self.penup()
        self.color("red")
        self.hideturtle()

        self.setpos(0, 0)
        self.write(f"Game Over! You Lost!", False, "center", ("Courier", 35, "normal"))

    def winning_message(self):
        """A function that displays the winning message"""

        self.penup()
        self.color("green")
        self.hideturtle()

        self.setpos(0, 0)
        self.write(f"Game Over! You Won!", False, "center", ("Courier", 35, "normal"))
