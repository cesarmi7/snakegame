import os
import random
import msvcrt
import time

game_over = False

width = 20
height = 20
x, y, fruit_x, fruit_y, score = 0, 0, 0, 0, 0
tail_x, tail_y = [0] * 100, [0] * 100
n_tail = 0

class Direction:
    STOP = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

dir = Direction.STOP

def setup():
    global game_over, dir, x, y, fruit_x, fruit_y, score
    game_over = False
    dir = Direction.STOP
    x = width // 2
    y = height // 2
    fruit_x = random.randint(0, width - 1)
    fruit_y = random.randint(0, height - 1)
    score = 0

def draw():
    global game_over, n_tail, tail_x, tail_y
    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(width + 2):
        print("#", end="")
    print()

    for i in range(height):
        for j in range(width):
            if j == 0:
                print("#", end="")

            if i == y and j == x:
                print("O", end="")
            elif i == fruit_y and j == fruit_x:
                print("F", end="")
            else:
                print_char = False

                for k in range(n_tail):
                    if tail_x[k] == j and tail_y[k] == i:
                        print("o", end="")
                        print_char = True

                if not print_char:
                    print(" ", end="")

            if j == width - 1:
                print("#")
    
    for i in range(width + 2):
        print("#", end="")
    print()
    
    print("Score:", score)

def input():
    global dir, game_over
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'a':
            dir = Direction.LEFT
        elif key == b'd':
            dir = Direction.RIGHT
        elif key == b'w':
            dir = Direction.UP
        elif key == b's':
            dir = Direction.DOWN
        elif key == b'x':
            game_over = True

def logic():
    global x, y, dir, n_tail, tail_x, tail_y, game_over, score, fruit_x, fruit_y

    prev_x = tail_x[0]
    prev_y = tail_y[0]
    prev2_x, prev2_y = 0, 0
    tail_x[0] = x
    tail_y[0] = y

    for i in range(1, n_tail):
        prev2_x = tail_x[i]
        prev2_y = tail_y[i]
        tail_x[i] = prev_x
        tail_y[i] = prev_y
        prev_x = prev2_x
        prev_y = prev2_y

    if dir == Direction.LEFT:
        x -= 1
    elif dir == Direction.RIGHT:
        x += 1
    elif dir == Direction.UP:
        y -= 1
    elif dir == Direction.DOWN:
        y += 1

    if x >= width:
        x = 0
    elif x < 0:
        x = width - 1
    if y >= height:
        y = 0
    elif y < 0:
        y = height - 1

    for i in range(n_tail):
        if tail_x[i] == x and tail_y[i] == y:
            game_over = True

    if x == fruit_x and y == fruit_y:
        score += 10
        fruit_x = random.randint(0, width - 1)
        fruit_y = random.randint(0, height - 1)
        n_tail += 1

def main():
    setup()
    while not game_over:
        draw()
        input()
        logic()
        time.sleep(0.03)

if __name__ == "__main__":
    main()
