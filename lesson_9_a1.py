from random import uniform

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
    #TODO change return maybe, for printing unavailable
    """
    obstacle = check_obstacle(direction, field, position)

    if direction == 'up' and obstacle:
        field = move_up(field, position)
    elif direction == 'right' and obstacle:
        field = move_right(field, position)
    elif direction == 'down' and obstacle:
        field = move_down(field, position)
    elif direction == 'left' and obstacle:
        field = move_left(field, position)
    else:
        print('Move unavailable')

    return field

def find_position(field):
    """
    #TODO add description
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
    #TODO add description
    """
    x, y = position
    flag = True

    if direction == 'up':
        if field[x - 1][y] == 'o':
            flag = False
    elif direction == 'right':
        if y + 1 > len(field) - 1:
            if field[x][0] == 'o':
                flag = False
        else:
            if field[x][y + 1] == 'o':
                flag = False
    elif direction == 'down':
        if x + 1 > len(field) - 1:
            if field[0][y] == 'o':
                flag = False
        else:
            if field[x + 1][y] == 'o':
                flag = False
    elif direction == 'left':
        if field[x][y - 1] == 'o':
            flag = False

    return flag

def add_obstacles(field):
    """
    #TODO add description
    #TODO change magic number
    """
    field_length = range(len(field))

    for row in field_length:
        for col in field_length:
            if uniform(0, 1) <= 0.5 and field[row][col] != 'x':
                field[row][col] = 'o'

    return field

def user_input():
    return input('Выебрите одно из направлений: up right down left или exit для выхода ')

def user_input_fields():
    return int(input('Укажите размер поля: '))


def main():
    game = True
    fields = user_input_fields()
    field = set_start_location(build_field(fields))
    add_obstacles(field)
    show_field(field)
    
    while game:
        user_direction = user_input()
        position = find_position(field)
        field = direction_dispatcher(user_direction, field, position)

        if user_direction == 'exit':
            game = False
        if game:
            show_field(field)


main()


