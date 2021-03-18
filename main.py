# import required modules
from turtle import Screen
from time import sleep
from spaceship import SpaceShip
from aliens import Invaders
from scoreboard import ScoreBoard

# setting up the game screen
game_screen = Screen()
game_screen.setup(width=600, height=650)
game_screen.bgcolor("black")
game_screen.title("Space Invaders")
game_screen.tracer(0)
game_screen.listen()

# setup and display each game component
space_ship = SpaceShip()

aliens = Invaders()
scores = ScoreBoard()
game_on = True
loops = 0


def end_game():
    """A function that ends the game abruptly"""

    global game_on
    game_on = False


# move the spaceship left and right on key presses
game_screen.onkey(space_ship.move_left, "Left")
game_screen.onkey(space_ship.move_right, "Right")

game_screen.onkey(space_ship.move_left, "a")
game_screen.onkey(space_ship.move_right, "d")

# fire missiles with space bar
game_screen.onkey(space_ship.shoot, "space")

# ends the game when the up key is pressed
game_screen.onkey(end_game, "e")


while game_on:

    game_screen.update()
    sleep(0.2)
    aliens.move()

    loops += 1

    # end the game once all the aliens have been destroyed
    if scores.user_score == 28 and len(aliens.alien_list) == 0:
        game_on = False
        scores.winning_message()

    # end the game once all the spaceship lives has been lost
    if scores.lives == 0:
        game_on = False
        scores.losing_message()

    if loops % 7 == 0 and len(aliens.alien_list) != 0:
        aliens.shoot()  # shoot a missile from a random alien after every few seconds

    if space_ship.attack:
        space_ship.move_bullet()

    if aliens.attack:
        aliens.move_missile()

    for missile in aliens.missile_list:

        if missile.distance(space_ship.osaro) < 15:

            # missile disappears if it hits the spaceship
            missile_index = aliens.missile_list.index(missile)
            aliens.missile_list.pop(missile_index)
            missile.clear()
            missile.hideturtle()

            space_ship.osaro.hideturtle()
            sleep(1)

            # reduce spaceship life by 1
            scores.update_live()

            # reset spaceship to initial position
            space_ship.osaro.setpos((0, -200))
            space_ship.osaro.showturtle()

        if missile.ycor() <= -250:

            # missile disappears when it touches scoreboard
            missile_index = aliens.missile_list.index(missile)
            aliens.missile_list.pop(missile_index)
            missile.clear()
            missile.hideturtle()

        for bullet in space_ship.bullet_list:

            if bullet.distance(missile) < 15:

                # collision with bullet makes missile disappear
                missile_index = aliens.missile_list.index(missile)
                aliens.missile_list.pop(missile_index)
                missile.clear()
                missile.hideturtle()

                # collision with missile makes bullet disappear
                bullet_index = space_ship.bullet_list.index(bullet)
                space_ship.bullet_list.pop(bullet_index)
                bullet.clear()
                bullet.hideturtle()

    for alien in aliens.alien_list:

        # spaceship loose a life when alien invaders close in on it
        if alien.ycor() <= -180:

            space_ship.osaro.hideturtle()
            sleep(1)

            # reduce spaceship life by 1
            scores.update_live()

            # reset spaceship to initial position
            space_ship.osaro.setpos((0, -200))
            space_ship.osaro.showturtle()

        for bullet in space_ship.bullet_list:

            if bullet.distance(alien) < 15:

                # bullet disappears when it hits an alien
                bullet_index = space_ship.bullet_list.index(bullet)
                space_ship.bullet_list.pop(bullet_index)
                bullet.clear()
                bullet.hideturtle()

                # and the alien dies and disappears
                alien_index = aliens.alien_list.index(alien)
                aliens.alien_list.pop(alien_index)
                alien.hideturtle()

                scores.update_score()  # increase the user score by 1

game_screen.exitonclick()
