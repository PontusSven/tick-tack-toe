game_list = [0,1,2]
game_on = True
status_list = ['Y', 'N']



def display(game_list):
    print('Here is the current list: ')
    print(game_list)

def position_choice():
    choice = 'wrong'

    while choice not in game_list:
        choice = input('Pick a postion (0,1,2)')

        if choice not in game_list:
            print('Invalid input')

    return int(choice)

def replacement_choice(game_list, position):

    user_placement = input('Type a string to place at position: ')

    game_list[position] = user_placement

    return game_list

    
def gameon_choice():
    choice = 'wrong'

    while choice not in status_list:
        choice = input('Keep playing? (Y or N) ')

        if choice not in status_list:
            print('Invalid input, please choose Y or N')

    if choice == 'Y':
        return True
    else:
        print('Ending game...')
        display(game_list)
        return False

def handler():
    game_on = True
    game_list = [0,1,2]

    while game_on:
        display(game_list)

        position = position_choice()

        game_list = replacement_choice(game_list, position)

        display(game_list)

        game_on = gameon_choice()
    
    

handler()