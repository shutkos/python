import random
import sys

ALLOWED_GAME_MODES = {'beginner', 'medium', 'expert'}
PREDEFINED_MODES = {
    'beginner': (8, 8, 10),
    'medium': (16, 16, 40),
    'expert': (16, 30, 99),
}


def generate_maze(max_rows, max_cols, max_mines):
    arr = [[0 for row in range(max_rows)] for column in range(max_cols)]
    arr[0][0] = -1
    for num in range(max_mines):
        x = random.randint(1, max_rows - 1)
        y = random.randint(1, max_cols - 1)

        if arr[x][y] != -1:
            arr[x][y] = -1
            if (0 <= x <= max_rows - 2) and (0 <= y <= max_cols - 1):
                if arr[y][x + 1] != -1:
                    arr[y][x + 1] += 1  # центр право

            if (1 <= x <= max_rows - 1) and (0 <= y <= max_cols - 1):
                if arr[y][x - 1] != -1:
                    arr[y][x - 1] += 1  # центр лево

            if (1 <= x <= max_rows - 1) and (1 <= y <= max_cols - 1):
                if arr[y - 1][x - 1] != -1:
                    arr[y - 1][x - 1] += 1  # верх лево

            if (0 <= x <= max_rows - 2) and (1 <= y <= max_cols - 1):
                if arr[y - 1][x + 1] != -1:
                    arr[y - 1][x + 1] += 1  # верх право

            if (0 <= x <= max_rows - 1) and (1 <= y <= max_cols - 1):
                if arr[y - 1][x] != -1:
                    arr[y - 1][x] += 1  # верх центр

            if (0 <= x <= max_rows - 2) and (0 <= y <= max_cols - 2):
                if arr[y + 1][x + 1] != -1:
                    arr[y + 1][x + 1] += 1  # низ право

            if (1 <= x <= max_rows - 1) and (0 <= y <= max_cols - 2):
                if arr[y + 1][x - 1] != -1:
                    arr[y + 1][x - 1] += 1  # низ лево

            if (0 <= x <= max_rows - 1) and (0 <= y <= max_cols - 2):
                if arr[y + 1][x] != -1:
                    arr[y + 1][x] += 1  # низ центр

    return arr


def print_maze(maze_matrix):
    for i in range(len(maze_matrix)):
        for j in range(len(maze_matrix[0])):
            item = "*" if maze_matrix[i][j] == -1 else str(maze_matrix[i][j])
            print(item, end=' ')
        print()


def main(mode='beginner'):
    print_maze(generate_maze(*PREDEFINED_MODES[mode]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('Only one parameter is allowed.')

    game_mode = sys.argv[1]
    if game_mode not in ALLOWED_GAME_MODES:
        raise ValueError('Only beginner, medium and expert models are allowed')

    main(game_mode)
