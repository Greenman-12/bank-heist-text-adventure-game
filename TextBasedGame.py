# Geoff Jensen
from idlelib.runscript import indent_message


def game_introduction():
    print()
    print('Bank Heist Text Adventure Game')
    print('You are a security officer at a bank\n'
          'A bank robber has made their way into the Vault and it is up to you to stop them!\n'
          'First, you will need to find items that will help you take down the bank robber.\n'
          'There are a total of 6 items that must be found in the different rooms of the bank that will prepare you to confront the Bank Robber in the Vault!\n'
          'Good Luck!')
    print()
    print('-----------------------------------------------------------------')
    print()
    instructions()
    print()
    print('-----------------------------------------------------------------')

def instructions():
    print(
         "You may take the following actions:\n"
         "type 'N' to move North\n"
         "type 'E' to move East\n"
         "type 'S' to move South\n"
         "type 'W' to move West\n"
         "type 'I' to pick up item\n"
         "type 'V' to view inventory\n"
         "type 'Exit' to QUIT THE GAME"
     )

    
def player_status(player_location, rooms, player_inventory):
    print(f'You are in the {player_location}')
    item = rooms[player_location]['i']
    if item not in player_inventory and item != []:
        print(f'You see: {item}')
    else:
        print('There are no items in this room')

def player_selection():
    return input('Type your action selection:').strip().lower()


def main():
    player_location = 'Lobby'  # sets player starting location
    player_inventory = []  # creates an empty player inventory list
    player_selection_options = ['n', 's', 'e', 'w']  # setting valid input's for direction choice
    rooms = {
    'Lobby': {'i': [],'n': 'Storage Room', 'w': 'Employee Break Room', 's':'Loan Office', 'e': 'Security Office'},
    'Maintenance Room': {'i': ['A Rope'], 'w':'Storage Room'},
    'Storage Room': {'i': ['The Vault Code'], 'e': 'Maintenance Room', 's': 'Lobby'},
    'Employee Break Room': {'i': ['An Energy Drink'],'e': 'Lobby'},
    'Loan Office': {'i': ['A Flashlight'],'n': 'Lobby', 'e': 'Manager\'s Office'},
    'Manager\'s Office': {'i': ['The Vault Key'],'w': 'Loan Office'},
    'Security Office': {'i': ['A Taser'],'w': 'Lobby', 'n': 'Vault'},
    'Vault': {'i': [],'s': 'Security Office'}, #Bank Robber location
    }

    game_introduction()
    
    
    while player_location != 'Vault': #loop until player_location is Vault
        player_status(player_location, rooms, player_inventory)
        selection = player_selection()
        if selection == 'v':
            print()
            print(f'Here is your inventory: {player_inventory}')
            print()
        elif selection == 'exit': # exit game if player enters exit command
            print()
            print('Exiting Game...')
            break
        elif selection == 'i':
            item = rooms[player_location]['i']
            if item not in player_inventory and item != []:
                player_inventory.append(item)
                print()
                print(f'You have added {item} to your inventory!')
                print()
            else:
                print()
                print('There are no items in this room that you can pick up.')
                print()
        elif selection not in player_selection_options: # check for valid player entry
            print()
            print('that is an invalid entry')
            print()
            instructions()
        elif selection in rooms[player_location]: # check for valid movement based on player location
            player_location = rooms[player_location][selection]
            print()
        else:
            print()
            print(f'You can''t go any further in that direction, pick a different direction')
            print()


    if player_location == 'Vault': # set win and lose conditions
        while int(len(player_inventory)) < 6:
            print()
            print('You entered the Vault without first collecting the required items.\n'
                  'The bank robber was able to make it past you and escape!\n'
                  'GAME OVER...')
            print()
            print('type \'exit\' to QUIT or \'restart\' to try again: ')
            game_end_choice = input().strip().lower()
            if game_end_choice == 'exit':
                print('Goodbye!')
                break
            elif game_end_choice == 'restart':
                main()
                break
            else:
                print('Invalid Entry')
        else:
            print()
            print('you entered the Vault\n'
                  'Since you were prepared by collecting all 6 items,\n'
                  'You capture the bank robber!\n')
            print('              YOU WIN!!!')
        # print('You made it to the Vault! You Win!!!')


main()
