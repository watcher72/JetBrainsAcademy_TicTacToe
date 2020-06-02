def print_field(field):
    print('---------')
    for row in field:
        print(f"| {' '.join(row)} |")
    print('---------')


def check_status(field):
    if is_winner('X', field):
        print('X wins')
        return False
    elif is_winner('O', field):
        print('O wins')
        return False
    elif not has_empty_cell(field):
        print('Draw')
        return False
    return True


def is_winner(player, matrix):
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == player:
            return True
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == player:
            return True
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == player \
            or matrix[0][2] == matrix[1][1] == matrix[2][0] == player:
        return True
    return False


def has_empty_cell(matrix):
    for r in matrix:
        if '_' in r:
            return True
    return False


def is_cell_empty(x, y, field):
    return field[3 - y][x - 1] == '_'


def take_coordinates():
    while True:
        string = input('Enter the coordinates: ')
        if not string.replace(' ', '').isdigit():
            print('You should enter numbers!')
            continue
        x, y = [int(x) for x in string.split()]
        if x not in [1, 2, 3] or y not in [1, 2, 3]:
            print('Coordinates should be from 1 to 3!')
            continue
        if not is_cell_empty(x, y, field):
            print('This cell is occupied! Choose another one!')
            continue
        return x, y


# Start game
field = [['_' for j in range(3)] for i in range(3)]
print_field(field)

while True:
    x, y = take_coordinates()
    field[3 - y][x - 1] = 'X'
    print_field(field)
    if not check_status(field):
        break
    x, y = take_coordinates()
    field[3 - y][x - 1] = 'O'
    print_field(field)
    if not check_status(field):
        break
