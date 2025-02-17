"""Pikachu in the Wild! This program simulates a pokemon game, where the user directs pikachu
to move accross a 150x150 grid. The user can direct pikachu to move up, down, left, or right.
Pikachu will move in the direction specified by the user until it reaches the edge of the grid.
Users can name their pikachu and can also set the number of turns it takes to see a wild pokemon.
The user can also choose which pokemon type they want to battle.

Author: Jimmy Chen
Version: 1
"""

def simulation_loop(turns, name, battle_freq):
    curr_turn = 0
    curr_coords = (75, 75)
    print("Starting simluation turn {} {} at {}".format(curr_turn, name, curr_coords))
    curr_turn += 1

    record = []
    
    while curr_turn <= turns:
        curr_direction = input("Which direction do you want to move (U)p, (D)own, (L)eft, (R)ight? => ").strip()
        print(curr_direction)
        if curr_turn % battle_freq == 0:
            print("Turn {}, {} at {}".format(curr_turn, name, curr_coords))
            opp_type = input("What type of Pokemon do you want to meet (W)ater, (G)round? => ").strip()
            print(opp_type)
            if opp_type.upper() == "W":
                curr_coords = move_pokemon(curr_coords, curr_direction, 1)
                print("{} wins and moves to {}".format(name, curr_coords))
                record.append('Win')
            elif opp_type.upper() == "G":
                if curr_direction.upper() == "U":
                    curr_coords = move_pokemon(curr_coords, "D", 10)
                elif curr_direction.upper() == "D":
                    curr_coords = move_pokemon(curr_coords, "U", 10)
                elif curr_direction.upper() == "L":
                    curr_coords = move_pokemon(curr_coords, "R", 10)
                elif curr_direction.upper() == "R":
                    curr_coords = move_pokemon(curr_coords, "L", 10)
                print("{} runs away to {}".format(name, curr_coords))
                record.append('Lose')
            else:
                record.append('No Pokemon')
        else:
            curr_coords = move_pokemon(curr_coords, curr_direction, 5)
        curr_turn += 1
    
    print("{} ends up at {}, Record: {}".format(name, curr_coords, record))
    
    
'''This function takes the current coordinates of pikachu and the direction to move, as well as the steps to move.
It returns the new coordinates of pikachu after moving in the specified direction. The return value is a tuple,
and must be within the bounds of the grid. Any invalid direction will be ignored'''
def move_pokemon(coords, direction, steps):
    x, y = coords
    if direction.upper() == "U":
        y += steps
    elif direction.upper() == "D":
        y -= steps
    elif direction.upper() == "L":
        x -= steps
    elif direction.upper() == "R":
        x += steps
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