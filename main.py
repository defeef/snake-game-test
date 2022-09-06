import math
import time
import random

width, height = 10, 10
screen = [[" " for _ in range(width)] for _ in range(height)]

snake = [[math.floor(width / 2), math.floor(height / 2)]]
snake_dir = 0 # 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT
apple = [1, 1]

def print_screen():
  screen = [[" " for _ in range(width)] for _ in range(height)]

  for segment in snake:
    screen[segment[0]][segment[1]] = "S"
  screen[apple[0]][apple[1]] = "A"

  row = ""

  print("+" + "-" * width * 2 + "+")
  for i in range(height):
    for j in range(width):
      row += screen[i][j]
      if j < width:
        row += " "
    print("|" + row + "|")
    row = ""
  print("+" + "-" * width * 2 + "+")
  print(str(apple))

while True:
  movement = input()
  if movement == "w":
    snake_dir = 0
  elif movement == "d":
    snake_dir = 1
  elif movement == "s":
    snake_dir = 2
  elif movement == "a":
    snake_dir = 3

  if snake_dir == 0:
    snake[0][0] -= 1
  elif snake_dir == 1:
    snake[0][1] += 1
  elif snake_dir == 2:
    snake[0][0] += 1
  elif snake_dir == 3:
    snake[0][1] -= 1

  for i in range(len(snake) - 1, 0, -1):
    snake[i] = snake[i - 1]
  
  if snake[0] == apple:
    while apple in snake:
      apple[0], apple[1] = random.randint(0, width - 1), random.randint(0, width - 1)

  if snake[0][0] < 0 or snake[0][0] > width - 1 or snake[0][1] < 0 or snake[0][1] > height - 1:
    break
  for tail in snake:
    if tail != snake[0] and snake[0] == tail:
      break

  print_screen()

  time.sleep(0.05)

print("You Lost!")
