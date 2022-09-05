import math
import time

width, height = 10, 10
screen = [[" " for _ in range(width)] for _ in range(height)]

snake = [[math.floor(width), math.floor(height)]]
snake_dir = 0 # 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT

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

  time.sleep(0.05)

print("You Lost!")
