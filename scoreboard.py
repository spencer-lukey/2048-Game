# Date: April 12, 2023
# Author: Spencer Lukey



from turtle import Turtle

FONT = ("Courier", 20, "normal")

COLOURS = [
  "#b7c9c7", "#d63c31", "#e38e3b", "#e8e548", "#73db63", "#5ec489", "#5abfdb",
  "#5678c7", "#9160d1", "#ff00e1", "#d4af37"
]


class Scoreboard(Turtle):
  # in charge of updating the scoreboard at the top, as well as returning whether or not the player won/lost

  def __init__(self):
    """
    Parameters: self
    Returns: None

    Initiates the scoreboard object, inheriting the Turtle class
    """

    super().__init__()
    self.score = 0
    self.hideturtle()
    self.penup()
    self.goto(0, 300)
    self.color("white")
    self.update_scoreboard(self.score)

  def update_scoreboard(self, score):
    """
    Parameters: self, score -> int
    Returns: None

    Updates the scoreboard with the current score
    """
    self.clear()
    self.write(f"Score: {score}", align="center", font=FONT)

  def lose_game(self):
    """
    Parameters: self
    Returns: None

    Displays the game over message when the player loses
    """
    self.color("black")
    self.goto(0, 0)
    self.write("GAME OVER", align="center", font=FONT)

  def win_game(self):
    """
    Parameters: self
    Returns: None

    Displays the winning message when the player wins
    """
    self.color("black")
    self.goto(0, 0)
    self.write("YOU WIN!", align="center", font=FONT)
