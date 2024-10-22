# We will import randint from random in order to 
# make the random choice factor in the game. 
import random
from random import sample

# Player boards. (val0: printing value, val1: true value)
player_one_board= {
 "a1":[" "," "], "a2":[" "," "], "a3":[" "," "], "a4":[" "," "], "a5":[" "," "],
 "b1":[" "," "], "b2":[" "," "], "b3":[" "," "], "b4":[" "," "], "b5":[" "," "],
 "c1":[" "," "], "c2":[" "," "], "c3":[" "," "], "c4":[" "," "], "c5":[" "," "],
 "d1":[" "," "], "d2":[" "," "], "d3":[" "," "], "d4":[" "," "], "d5":[" "," "],
 "e1":[" "," "], "e2":[" "," "], "e3":[" "," "], "e4":[" "," "], "e5":[" "," "]}

player_two_board= {
 "a1":[" "," "], "a2":[" "," "], "a3":[" "," "], "a4":[" "," "], "a5":[" "," "],
 "b1":[" "," "], "b2":[" "," "], "b3":[" "," "], "b4":[" "," "], "b5":[" "," "],
 "c1":[" "," "], "c2":[" "," "], "c3":[" "," "], "c4":[" "," "], "c5":[" "," "],
 "d1":[" "," "], "d2":[" "," "], "d3":[" "," "], "d4":[" "," "], "d5":[" "," "],
 "e1":[" "," "], "e2":[" "," "], "e3":[" "," "], "e4":[" "," "], "e5":[" "," "]}

# Player introduction (naming the players).
def name_player():
  player_name = "-1"
  while player_name == "-1":
    print("Name unknown?")
    user_choice = input("yes(y) or no(n)?")
    if user_choice in ["yes","y"]:
      player_name = ""
    else:
      print("Captain do not fool around, what is your name?")
      player_name = input("Answer here: ")
  print(" ")
  return player_name

# The player has to select the placement of his ships.
# Each player owns 5 ships.
def place_ships(player_name,player_board):
  used_positions = []
  for i in range(1,6):
    position = input("Captain "+ str(player_name) +" enter the position ship no "+ str(i)+": ")
    
    while position not in player_board.keys():
      print("Arg! That possition is not valid.")
      print("Try using a position in this format: <a-e><1-5> (ex. b4)\n")
      position = input("Captain "+ str(player_name) +" enter the position ship no "+ str(i)+": ")

    while position in used_positions:
      print("Avast ye mate! That possition has already been used. Try again savvy?\n")
      position = input("Captain "+ str(player_name) +" enter the position ship no "+ str(i)+": ")
 
    if (position not in used_positions) and (position in player_board.keys()):
      used_positions.append(position) 
  
  print("\n" *100)
  for i in used_positions:
    player_board[i][1] = "ship"
  
# Randomly generate ships for the pc and place them to the board.
def place_ships_pc(pc_board):
  random_ships = sample(pc_board.keys(),5)
  for i in random_ships:
    pc_board[i][1] = "ship"

def print_boards():
  values = ["a","b","c","d","e"]
  keys = [i for i in player_one_board]
  key_counter = 0

  print ("  1 2 3 4 5       1 2 3 4 5")
  for i in range(0,5):
    print(values[i],player_one_board[keys[key_counter]][0],player_one_board[keys[key_counter+1]][0],player_one_board[keys[key_counter+2]][0],player_one_board[keys[key_counter+3]][0],player_one_board[keys[key_counter+4]][0],"    "+values[i],player_two_board[keys[key_counter]][0],player_two_board[keys[key_counter+1]][0],player_two_board[keys[key_counter+2]][0],player_two_board[keys[key_counter+3]][0],player_two_board[keys[key_counter+4]][0])
    key_counter += 5

def print_header():
  print("Welcome to Battleship Game!")
  print("Avast ye! The objective is to sink the opponent's ships before the opponent sinks yours. Savvy?")
  gamemode = input("Input 1 for a 1-player game (player vs computer) or 2 for a 2-player game (player vs player):")
  while gamemode not in ["1","2"]:
    print("Invalid command mate! Try again or walk the plank.")
    gamemode = input("Input 1 for a 1-player game (player vs computer) or 2 for a 2-player game (player vs player):")
  return gamemode

# The players' gameplay.
def gameplay_player(player_name,player_board,player_score):
  print("\nMain cannon at the ready! Captain "+ str(player_name) +" feed them to the fishes!")
  missile_position = input("Enter the position to throw your missile: ")
 
  while missile_position not in player_board.keys():
    print("Arr! Invalid possition, try again captain!")
    print("Try using a position in this format: <a-e><1-5> (ex. b4)")
    missile_position = input("Enter the position to bombard the enemy:")
     
  while not(player_board[missile_position][0] == " "):
    print("That possition has already been registered. Avast ye!")
    print("Make 'em regret it captain!")
    missile_position = input("Enter the position to bombard the enemy:")

  if player_board[missile_position][0] == " ":
    print("Ahoy! Missile thrown at ",missile_position,"!")
  if player_board[missile_position][1] == "ship":
    player_board[missile_position][0] = "o"
    print("Target hit! There's blood in the water! What a fine meal for the sharks...")
    player_score += 1
  else:
    print("Target missed! You've been called out!")
    player_board[missile_position] = "x"
  return player_score

# The pc's gameplay.
def gameplay_pc(pc_board,pc_score):
  random_missile_position = random.choice(list(pc_board.keys()))
  
  while not (pc_board[random_missile_position][0] == " "):
    random_missile_position = random.choice(list(pc_board.keys()))
  
  print("Enemy's missile thrown at", random_missile_position)
  if pc_board[random_missile_position][1] == "ship":
    print ("Target hit! Crying won't do you any good.")
    pc_board[random_missile_position][0] = "o"
    pc_score += 1
  else:
    print ("Target missed! It was one slash away, ear to ear.")
    pc_board[random_missile_position][0] = "x"
  return pc_score

def win_condition_pvc(player_name,player_score,pc_score):
  if player_score == 5:
    print("\nCongratulations!",player_name,"you win!\nAs for your opponent, a slow death will be their reward.")
    exit()
  if pc_score == 5:
    print("\nThe computer wins. Be careful, your tears will salt the ocean!")

def win_condition_pvp(player_one_name,player_two_name,player_one_score,player_two_score):
  if player_one_score == 5:
    print("\nCongratulations!",player_one_name,"you win!\nYour opponent is now fishbate.")
    exit()
  if player_two_score == 5:
    print("\nCongratulations!",player_two_name,"you win!\nYour opponent is resting with the sharks tonight.")
    exit()

# The game.
if __name__ == "__main__":
  gamemode = print_header()
  if gamemode == "1": # pc vs player
    player_score = pc_score = 0
    print("\nThe war's begun! The flames are calling...")
    player_name = name_player()
    place_ships(player_name,player_two_board)
    place_ships_pc(player_one_board)
    game_starter = sample([1,2],1) 
    if game_starter == 1:
      print("Yar ha har! ",player_name," you go first lad!\n")
      while (player_score < 5) and (pc_score < 5):
        player_score = gameplay_player(player_name,player_one_board,player_score)
        print("\n Computer","  vs  ",player_name)
        print_boards()
        win_condition_pvc(player_name,player_score,pc_score)
        pc_score = gameplay_pc(player_two_board,pc_score)
        print("\n Computer","  vs  ",player_name)
        print_boards()
        win_condition_pvc(player_name,player_score,pc_score)
    else:
      print("Computer goes first. Prepare the cannons!\n")
      while (player_score < 5) and (pc_score < 5):
        pc_score = gameplay_pc(player_two_board,pc_score)
        print("\n Computer","  vs  ",player_name)
        print_boards()
        win_condition_pvc(player_name,player_score,pc_score)
        player_score = gameplay_player(player_name,player_one_board,player_score)
        print("\n Computer","  vs  ",player_name)
        print_boards()
        win_condition_pvc(player_name,player_score,pc_score)

  if gamemode == "2": # player vs player
    player_one_score = player_two_score = 0
    print("\nAhoy lads!")
    print("Captain 1, what is your name?")
    player_one_name = name_player()
    print("Captain 2, what is your name?")
    player_two_name = name_player()
    place_ships(player_one_name,player_two_board)
    place_ships(player_two_name,player_one_board)
    game_starter = sample([1,2],1)
    if game_starter == 1:
      print("Yar ha har! ",player_one_name," you go first lad!")
      while (player_one_score < 5) and (player_two_score < 5):
        player_one_score = gameplay_player(player_one_name,player_one_board,player_one_score)
        print("\n ",player_one_name,"  vs  ",player_two_name)
        print_boards()
        win_condition_pvp(player_one_name,player_two_name,player_one_score,player_two_score)
        player_two_score = gameplay_player(player_two_name,player_two_board,player_two_score)
        print("\n ",player_one_name,"  vs  ",player_two_name)
        print_boards()
        win_condition_pvp(player_one_name,player_two_name,player_one_score,player_two_score)
    else:
      print(player_two_name," goes first. Prepare the cannons!")
      while (player_one_score < 5) and (player_two_score < 5):
        player_two_score = gameplay_player(player_two_name,player_two_board,player_two_score)
        print("\n ",player_one_name,"  vs  ",player_two_name)
        print_boards()
        win_condition_pvp(player_one_name,player_two_name,player_one_score,player_two_score)
        player_one_score = gameplay_player(player_one_name,player_one_board,player_one_score)
        print("\n ",player_one_name,"  vs  ",player_two_name)
        print_boards()
        win_condition_pvp(player_one_name,player_two_name,player_one_score,player_two_score)

















 
