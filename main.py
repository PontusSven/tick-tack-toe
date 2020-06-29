game_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
acceptable_values = range(1,10)
acceptable_insert = ['X', 'O']

def start_up():
    print('Let the games begin!')
    print('Position indexes')
    print('1', '2', '3')
    print('4', '5', '6')
    print('7', '8', '9')


def display(game_list):
    print(game_list[0], game_list[1], game_list[2])
    print(game_list[3], game_list[4], game_list[5])
    print(game_list[6], game_list[7], game_list[8])

def position():
    position = input('Enter a position (1-9')

    while position not in acceptable_values:
        position = input('Input not valid, enter a position (1-9')
    else:
        return int(position)

def insert_value(position):
    insert = input('Enter a value to insert (X or O)')
    
    while insert not in acceptable_insert:
        insert = input('Input not valid, enter a value to insert (X or O)')

    else:
        game_list[position-1] = insert
        return game_list

def handler():
    count = 0
    start_up()

    while count < 9:

        user_position = position()
        game_list = insert_value(user_position)
        display(game_list)

        count += 1

    else:
        print('Ending game...')

handler()