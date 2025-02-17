"""Pikachu in the Wild! This program simulates a pokemon game, where the user directs pikachu
to move accross a 150x150 grid. The user can direct pikachu to move up, down, left, or right.
Pikachu will move in the direction specified by the user until it reaches the edge of the grid.
Users can name their pikachu and can also set the number of turns it takes to see a wild pokemon.
The user can also choose which pokemon type they want to battle.

Author: Jimmy Chen
Version: 1
"""


'''This function simulates the pokemon game. It takes the number of turns, the name of the pikachu, and the battle frequency
as inputs. The function will prompt the user to input the direction to move the pikachu, and the type of pokemon to battle.
The function will then move the pikachu in the specified direction, and will battle the pokemon if the turn is a multiple of the
battle frequency. The function will keep track of the record of battles, and will print the final coordinates of pikachu, as well as
the battle record.'''
def simulation_loop(turns, name, battle_freq):
    # initialize the turn number, and the starting coordinates of pikachu
    curr_turn = 0
    curr_coords = (75, 75)
    print("Starting simulation, turn {} {} at {}".format(curr_turn, name, curr_coords))
    curr_turn += 1

    record = []
    
    # loop through the number of turns specified
    while curr_turn <= turns:
        # get the direction to move pikachu
        curr_direction = input("What direction does {} walk? => ".format(name)).strip()
        print(curr_direction)

        # move pikachu in the specified direction
        curr_coords = move_pokemon(curr_coords, curr_direction, 5)

        # check if pikachu encounters a pokemon
        if curr_turn % battle_freq == 0:
            print("Turn {}, {} at {}".format(curr_turn, name, curr_coords))
            opp_type = input("What type of pokemon do you meet (W)ater, (G)round? => ").strip()
            print(opp_type)

            # battle the pokemon
            if opp_type.upper() == "W":
                curr_coords = move_pokemon(curr_coords, curr_direction, 1)
                print("{} wins and moves to {}".format(name, curr_coords))
                record.append('Win')
            elif opp_type.upper() == "G":
                # if pikachu loses the battle, it will run away in the opposite direction
                if curr_direction.upper() == "S":
                    curr_coords = move_pokemon(curr_coords, "N", 10)
                elif curr_direction.upper() == "N":
                    curr_coords = move_pokemon(curr_coords, "S", 10)
                elif curr_direction.upper() == "E":
                    curr_coords = move_pokemon(curr_coords, "W", 10)
                elif curr_direction.upper() == "W":
                    curr_coords = move_pokemon(curr_coords, "E", 10)
                print("{} runs away to {}".format(name, curr_coords))
                record.append('Lose')
            else:
                record.append('No Pokemon')
        curr_turn += 1
    
    print("{} ends up at {}, Record: {}".format(name, curr_coords, record))
    
    
'''This function takes the current coordinates of pikachu and the direction to move, as well as the steps to move.
It returns the new coordinates of pikachu after moving in the specified direction. The return value is a tuple,
and must be within the bounds of the grid. Any invalid direction will be ignored'''
def move_pokemon(coords, direction, steps):
    x, y = coords

    # move pikachu in the specified direction
    if direction.upper() == "N":
        x -= steps
    elif direction.upper() == "S":
        x += steps
    elif direction.upper() == "W":
        y -= steps
    elif direction.upper() == "E":
        y += steps

    # check if the new coordinates are within the bounds of the grid
    if x < 0:
        x = 0
    elif x > 150:
        x = 150
    if y < 0:
        y = 0
    elif y > 150:
        y = 150
    return (x, y)

if __name__ == "__main__":
    # Get inputs on the number of turns, name of pikachu, and battle frequency from the user
    turns = input("How many turns? => ").strip()
    print(turns)
    turns = int(turns)

    name = input("What is the name of your pikachu? => ").strip()
    print(name)

    battle_freq = input("How often do we see a Pokemon (turns)? => ").strip()
    print(battle_freq + "\n")
    battle_freq = int(battle_freq)

    simulation_loop(turns, name, battle_freq)