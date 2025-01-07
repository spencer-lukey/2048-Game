# Date: April 12, 2023
# Author: Spencer Lukey



from turtle import Turtle, Screen
from blocks import Blocks, GAME_ON, COLOURS
from scoreboard import Scoreboard


def init_position(Turtle):
  """
  Parameters: None
  Returns: setup_t -> object, start_posx -> int, start_posy -> int

  Sets up the drawing screen turtle object
  """
  setup_t = Turtle()
  start_posx = -200
  start_posy = 200
  return setup_t, start_posx, start_posy


def screen_setup(setup_t, start_posx, start_posy):
  """
  Parameters: setup_t -> object, start_posx -> int, start_posy -> int
  Returns: None

  Sets up the drawing screen lines and background
  """
  screen = Screen()
  screen.setup(width=600, height=800)
  screen.bgcolor("black")
  screen.title("2048 Game!")
  screen.tracer(0)
  screen.listen()

  setup_t.hideturtle()
  setup_t.penup()
  setup_t.pencolor("white")
  setup_t.color("white")
  setup_t.setx(start_posx)
  setup_t.sety(start_posy)

  # set up the grid to play game in
  for i in range(5):
    setup_t.pendown()
    setup_t.forward(400)
    setup_t.penup()
    setup_t.goto(start_posx, (start_posy - 100))
    start_posy -= 100

  start_posx = -200
  start_posy = 200
  setup_t.goto(start_posx, start_posy)
  for j in range(5):
    setup_t.pendown()
    setup_t.setheading(270)
    setup_t.forward(400)
    setup_t.penup()
    setup_t.goto((start_posx + 100), start_posy)
    start_posx += 100

  return screen


def draw_legend(colours):
  """
  Parameters: colours -> list
  Returns: None

  Draws the colour legend at the top of the screen
  """
  value = 2
  x_cord = -195
  legend_t = Turtle()
  for colour in COLOURS:
    legend_t.hideturtle()
    legend_t.penup()
    legend_t.color(colour)
    if value >= 1024:
      legend_t.goto((x_cord + 45), 200)
      x_cord += 55
    elif value >= 128:
      legend_t.goto((x_cord + 30), 200)
      x_cord += 40
    elif value >= 16:
      legend_t.goto((x_cord + 20), 200)
      x_cord += 30
    else:
      legend_t.goto((x_cord + 10), 200)
      x_cord += 20

    legend_t.write(f"{value}", align="center", font=("Courier", 15, "normal"))
    value *= 2


def set_listeners(screen, blocks_manager):
  """
  Parameters: None
  Returns: None

  Initializes screen listeners for keyboard inputs
  """
  screen.listen()
  screen.onkey(fun=blocks_manager.move_up, key="Up")
  screen.onkey(fun=blocks_manager.move_up, key="w")
  screen.onkey(fun=blocks_manager.move_down, key="Down")
  screen.onkey(fun=blocks_manager.move_down, key="s")
  screen.onkey(fun=blocks_manager.move_left, key="Left")
  screen.onkey(fun=blocks_manager.move_left, key="a")
  screen.onkey(fun=blocks_manager.move_right, key="Right")
  screen.onkey(fun=blocks_manager.move_right, key="d")


def main():
  """
  Parameters: None
  Returns: None

  Controls the game flow
  """
  turt, x, y = init_position(Turtle)
  screen = screen_setup(turt, x, y)
  blocks_manager = Blocks()
  scoreboard = Scoreboard()

  set_listeners(screen, blocks_manager)
  draw_legend(COLOURS)
  game_on = blocks_manager.GAME_ON

  while game_on:
    highest_score = blocks_manager.update_score()
    scoreboard.score = highest_score
    scoreboard.update_scoreboard(highest_score)
    screen.update()

    if -1 in blocks_manager.current_block_choices:
      scoreboard.lose_game()
      blocks_manager.GAME_ON = False
    else:
      if scoreboard.score == 2048:
        screen.clear()
        scoreboard.win_game()
        blocks_manager.GAME_ON = False

  screen.exitonclick()


if __name__ == "__main__":
  main()
