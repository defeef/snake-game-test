import math
import time

width, height = 10, 10
screen = [[" " for _ in range(width)] for _ in range(height)]

snake = [math.floor(width), math.floor(height)]
snake_dir = 0 # 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT

while True:
  

  time.sleep(0.05)
