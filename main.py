import math
import time

width, height = 10, 10
screen = [[" " for _ in range(width)] for _ in range(height)]

snake = [[math.floor(width / 2), math.floor(height / 2)]]
snake_dir = 0 # 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT

def print_screen():
  screen = [[" " for _ in range(width)] for _ in range(height)]

  for segment in snake:
    print(str(segment[0]) + ", " + str(segment[1]))
    screen[segment[0]][segment[1]] = "S"

  row = ""

  for i in range(height):
    for j in range(width):
      row += screen[i][j]
      if j < width:
        row += " "
    print(row)
    row = ""

while True:
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

  if snake[0][0] < 0 or snake[0][0] > width or snake[0][1] < 0 or snake[0][1] > height:
    break
  for tail in snake:
    if tail != snake[0] and snake[0] == tail:
      break
  
  print_screen()

  time.sleep(0.05)

print("You Lost!")
