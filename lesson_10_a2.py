import pickle
from random import uniform

#CONSTANT DATA

OBSTACLE_PERCENT = 50

def build_field(n):
    """
    input: n - positive integer
    output: grid - list of lists represented field
    example:
    n = 3
    [['_', '_', '_']
     ['_', '_', '_']
     ['_', '_', '_']]
    """
    tmp = []
    field = []
    for i in range(n):
        tmp.append('_')
    for j in range(n):
        field.append(tmp[:])
    return field

def set_start_location(f):
    """
    input: f - field
    output: field with added x position (x - player)
    [['x', '_', '_']
     ['_', '_', '_']
     ['_', '_', '_']]
    """
    f[0][0] = 'x'
    return f

def show_field(f):
    """
    input: f - field
    prints field in terminal
    """
    for i in f:
        print(' '.join(i))

def move_up(field, position):
    """
    input: field - field
    output: modified field with changed x position
    """
    x, y = position

    field[x - 1][y] = 'x'
    field[x][y] = '_'

    return field


def move_down(field, position):
    """
    input: field - field
    output: modified field with changed x position
    """
    x, y = position

    if x + 1 > len(field) - 1:
        field[0][y] = 'x'
        field[x][y] = '_'
    else:
        field[x + 1][y] = 'x'
        field[x][y] = '_'

    return field


def move_left(field, position):
    """
    input: field - field
    output: modified field with changed x position
    """
    x, y = position

    field[x][y - 1] = 'x'
    field[x][y] = '_'

    return field

def move_right(field, position):
    """
    input: field - field
    output: modified field with changed x position
    """
    x, y = position

    if y + 1 > len(field) - 1:
        field[x][0] = 'x'
        field[x][y] = '_'
    else:
        field[x][y + 1] ='x'
        field[x][y] = '_'

    return field

def direction_dispatcher(direction, field, position):
    """
    input: direction - string
           field - list of lists (2d field)
           position - tuple, represented as coordinates of player at the field (0, 0) -> top, left corner
    output: field - list of lists, with changed player (x) position
    This function used as dispatcher of movement
    """
    obstacle = check_obstacle(direction, field, position)

    if direction == 'up' and not obstacle:
        field = move_up(field, position)
    elif direction == 'right' and not obstacle:
        field = move_right(field, position)
    elif direction == 'down' and not obstacle:
        field = move_down(field, position)
    elif direction == 'left' and not obstacle:
        field = move_left(field, position)
    elif obstacle:
        blocked_direction(direction)

    return field


def blocked_direction(direction):
    """
    input: direction as string
    output: None, used as print() built-in function
    """
    print(f'Oops... Move to {direction} is blocked!')

def find_position(field):
    """
    input: field - list of lists (2d field)
    output: tuple - represented as coordinates of player at the field (0, 0) -> top, left corner
    """
    pos_x = 0
    pos_y = 0
    field_length = range(len(field))

    for x in field_length:
        for y in field_length:
            if field[x][y] == 'x':
                pos_x = x
                pos_y = y
                break

    return pos_x, pos_y

def check_obstacle(direction, field, position):
    """
    input: direction - string
           field - list of lists (2d field)
           position - tuple, represented as coordinates of player at the field (0, 0) -> top, left corner
    output: boolean, if move at new position is blocked -> return True, else False
    """
    x, y = position
    flag = False

    if direction == 'up':
        if field[x - 1][y] == 'o':
            flag = True
    elif direction == 'right':
        if y + 1 > len(field) - 1:
            if field[x][0] == 'o':
                flag = True
        else:
            if field[x][y + 1] == 'o':
                flag = True
    elif direction == 'down':
        if x + 1 > len(field) - 1:
            if field[0][y] == 'o':
                flag = True
        else:
            if field[x + 1][y] == 'o':
                flag = True
    elif direction == 'left':
        if field[x][y - 1] == 'o':
            flag = True

    return flag

def add_obstacles(field, obs):
    """
    input: field - list of lists (2d list) represented field
           obs - integer, global value of obstacle % (converted to float obs/100) 
    output: filed - list of lists (2d list) represented field, with added obstacles (o) to it.
    """
    field_length = range(len(field))
    obs_percent = obs / 100
    for row in field_length:
        for col in field_length:
            if uniform(0, 1) <= obs_percent and field[row][col] != 'x':
                field[row][col] = 'o'

    return field


def user_input():
    return input('Выебрите одно из направлений: up right down left. exit для выхода. save для сохранения. load для загрузки. ')

def user_input_fields():
    return int(input('Укажите размер поля: '))

def save_game(f):
    """
    input: f (field) - list of lists (2d list) represented field
    save field to file
    """
    with open('save.dat', 'wb') as sf:
        pickle.dump(f, sf)
    print('Game saved!')

def load_game():
    """
    output: loaded field data (list of lists (2d list) represented field)
    """
    with open('save.dat', 'rb') as lf:
        loaded_data = pickle.load(lf)
    print('Game loaded!')
    return loaded_data

def main():
    game = True
    fields = user_input_fields()
    field = set_start_location(build_field(fields))
    add_obstacles(field, OBSTACLE_PERCENT)
    show_field(field)
    
    while game:
        user_direction = user_input()
        if user_direction == 'save':
            save_game(field)
        elif user_direction == 'load':
            field = load_game()

        position = find_position(field)
        field = direction_dispatcher(user_direction, field, position)

        if user_direction == 'exit':
            game = False
        if game:
            show_field(field)

main()


