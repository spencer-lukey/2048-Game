# Date: April 12, 2023
# Author: Spencer Lukey



from turtle import Turtle
import random

GAME_ON = True

COLOURS = [
  "#b7c9c7", "#d63c31", "#e38e3b", "#e8e548", "#73db63", "#5ec489", "#5abfdb",
  "#5678c7", "#9160d1", "#ff00e1", "#d4af37"
]
MOVE_DISTANCE = 100
POSITIONS = {
  1: (-150, 150),
  2: (-50, 150),
  3: (50, 150),
  4: (150, 150),
  5: (-150, 50),
  6: (-50, 50),
  7: (50, 50),
  8: (150, 50),
  9: (-150, -50),
  10: (-50, -50),
  11: (50, -50),
  12: (150, -50),
  13: (-150, -150),
  14: (-50, -150),
  15: (50, -150),
  16: (150, -150)
}

BLOCK_CHOICES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


class Blocks(Turtle):
  #  create, delete, manage, and move the blocks

  def __init__(self):
    """
    Parameters: self
    Returns: None

    Initializes the Blocks class, inheriting the Turtle class
    as the foundation for creating and moving blocks
    """

    super().__init__()
    self.blocks_list = []
    self.current_block_choices = [
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
    ]

    # start game with 3 blocks on the screen
    for i in range(3):
      self.create_block()

  def create_block(self):
    """
    Parameters: self
    Returns: None

    Creates a block at a random position on the screen
    """
    if len(self.current_block_choices) > 0:
      new_block = Turtle("square")
      new_block.penup()
      possible_colors = random.randint(0, 2)

      # Set the color of the block
      color = COLOURS[possible_colors]
      new_block.color(color)

      # Add square to proper co-ord
      new_block.shapesize(4.9, 4.9, 1)
      self.refresh_block_choices(self.current_block_choices)
      position = random.choice(self.current_block_choices)
      new_block.goto(POSITIONS[position])
      self.refresh_block_choices(self.current_block_choices)

      # Add to blocks list, check to see if block is in spot to add
      self.blocks_list.append([color, position, new_block])
      self.refresh_block_choices(self.current_block_choices)
    else:
      self.current_block_choices.append(-1)

  def refresh_block_choices(self, current_block_choices):
    """
    Parameters: self, current_block_choices -> list
    Returns: None

    Refreshes the new list of block positions that can be used
    """
    # Reset the blocks positions, delete the new positions
    new_block_choices = BLOCK_CHOICES.copy()
    for block in self.blocks_list:
      value = block[
        1]  # value = position on the grid (1 - 16) starting from left to right, top to bottom
      new_block_choices.remove(value)
    self.current_block_choices = new_block_choices

  def update_score(self):
    """
    Parameters: self
    Returns: high_score -> int

    Iterates through all of the blocks to sum up the value of each block
    Returns the total value (sum of all block values)
    """
    total_score = 0
    for block in self.blocks_list:
      index = COLOURS.index(block[0])
      total_score += 2**index  # adds each block's value to total score
    return total_score

  def move_up(self):
    """
    Parameters: self
    Returns: None

    Moves the blocks up until they hit the top of the screen or another block
    """
    # Can move a total of three times
    # Bug in movement for rest of move functions, should loop through the first row, second, etc.
    for block in self.blocks_list:
      for i in range(9):
        self.refresh_block_choices(self.current_block_choices)
        if (block[1] - 4) <= 0:
          break

        # If no block in the way = move
        elif (block[1] - 4) in self.current_block_choices:
          block[1] -= 4
          block[2].goto(POSITIONS[block[1]])

        # If block in the way (same color) = move + delete
        elif (block[1] - 4) not in self.current_block_choices:
          for square in self.blocks_list:

            if (block[1] - 4) == square[1]:
              if block[0] == square[0]:
                block[1] -= 4
                colour_index = COLOURS.index(block[0])
                block[2].color(COLOURS[colour_index + 1])
                block[0] = COLOURS[colour_index + 1]
                # Move block to new position
                block[2].goto(POSITIONS[block[1]])

                # Remove old block from list
                self.blocks_list.remove(square)
                square[2].hideturtle()
                square[2].goto(-300, -400)
                self.refresh_block_choices(self.current_block_choices)

              else:
                continue
            else:
              continue
        else:
          continue
    # End function with adding new block
    self.create_block()

  def move_down(self):
    """
    Parameters: self
    Returns: None

    Moves the blocks down until they hit the bottom of the screen or another block
    """
    # Reverse the blocks list to loop through
    # Bug in movement for rest of move functions, should loop through the last row, second to last, etc.
    for block in self.blocks_list:
      for i in range(9):
        self.refresh_block_choices(self.current_block_choices)
        if (block[1] + 4) > 16:
          break

        # If no block in the way = move
        elif (block[1] + 4) in self.current_block_choices:
          block[1] += 4
          block[2].goto(POSITIONS[block[1]])

        # If block in the way (same color) = move + delete
        elif (block[1] + 4) not in self.current_block_choices:
          for square in self.blocks_list:

            if (block[1] + 4) == square[1]:
              if block[0] == square[0]:
                block[1] += 4
                colour_index = COLOURS.index(block[0])
                block[2].color(COLOURS[colour_index + 1])
                block[0] = COLOURS[colour_index + 1]
                # Move block to new position
                block[2].goto(POSITIONS[block[1]])

                # Remove old block from list
                self.blocks_list.remove(square)
                square[2].hideturtle()
                square[2].goto(-300, -400)
                self.refresh_block_choices(self.current_block_choices)
                continue
              else:
                continue
            else:
              continue
        else:
          continue
    # End function with adding new block
    self.create_block()

  def move_left(self):
    """
    Parameters: self
    Returns: None

    Moves the blocksleft until they hit the left side of the screen or another block
    """
    # Bug in movement for rest of move functions, should loop through the first column, second, etc
    for block in self.blocks_list:
      for i in range(3):
        self.refresh_block_choices(self.current_block_choices)
        if (block[1] % 4 == 1):
          break

        # If no block in the way = move
        elif (block[1] - 1) in self.current_block_choices:
          block[1] -= 1
          block[2].goto(POSITIONS[block[1]])

        # If block in the way (same color) = move + delete
        elif (block[1] - 1) not in self.current_block_choices:
          for square in self.blocks_list:

            if (block[1] - 1) == square[1]:
              if block[0] == square[0]:
                block[1] -= 1
                colour_index = COLOURS.index(block[0])
                block[2].color(COLOURS[colour_index + 1])
                block[0] = COLOURS[colour_index + 1]
                # Move block to new position
                block[2].goto(POSITIONS[block[1]])

                # Remove old block from list
                self.blocks_list.remove(square)
                square[2].hideturtle()
                square[2].goto(-300, -400)
                self.refresh_block_choices(self.current_block_choices)
                continue
              else:
                continue
            else:
              continue
        else:
          continue
    # End function with adding new block
    self.create_block()

  def move_right(self):
    """
    Parameters: self
    Returns: None

    Moves the blocks right until they hit the right side of the screen or another block
    """

    # Bug in movement for rest of move functions, should loop through the last column, second to last, etc.
    for block in self.blocks_list:
      for i in range(9):
        self.refresh_block_choices(self.current_block_choices)
        if (block[1] % 4 == 0):
          break

        # If no block in the way = move
        elif (block[1] + 1) in self.current_block_choices:
          block[1] += 1
          block[2].goto(POSITIONS[block[1]])

        # If block in the way (same color) = move + delete
        elif (block[1] + 1) not in self.current_block_choices:
          for square in self.blocks_list:

            if (block[1] + 1) == square[1]:
              if block[0] == square[0]:
                block[1] += 1
                colour_index = COLOURS.index(block[0])
                block[2].color(COLOURS[colour_index + 1])
                block[0] = COLOURS[colour_index + 1]
                # Move block to new position
                block[2].goto(POSITIONS[block[1]])

                # Remove old block from list
                self.blocks_list.remove(square)
                square[2].hideturtle()
                square[2].goto(-300, -400)
                self.refresh_block_choices(self.current_block_choices)
                continue
              else:
                continue
            else:
              continue
        else:
          continue
    # End function with adding new block
    self.create_block()
