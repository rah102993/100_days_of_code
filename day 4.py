print('''
       \       /
  \     /  
   \.-./ 
  (o\^/o)  _   _   _     __
   ./ \.\ ( )-( )-( ) .-'  '-.
    {-} \(//  ||   \\/ (   )) '-.
         //-__||__.-\\.       .-'
        (/    ()     \)'-._.-'
        ||    ||      \\
        ('    ('       ')''')
def start_game():
    print("Welcome to the Ant's Adventure: The Quest for Sugar!")
    print("Your mission is to find sugar and transport it safely to the storage room")
    print("But beware, your choices will determine your success!")

    direction = input("Do you want the ant to turn right or left? (right/left): ").lower()

    if direction == "right":
        print("Congratulations! You've found the Sugar.")
        move_sugar()
    elif direction == "left":
        print("Oh no! You've taken the wrong path, and it's Game Over!!!")
    else:
        print("Invalid choice! Please type 'right' or 'left'.")
        start_game()

def move_sugar():
    print("\nNow that you have found the sugar, you need to move it to the storage room.")
    direction = input("Do you want to move up or down? (up/down): ").lower()

    if direction == "up":
        print("Uh-oh! The door is closed, and you can't get in.")
        print("You need to go back and try again.")
        move_sugar()
    elif direction == "down":
        print("Good Choice! You found the door with a key.")
        unlock_door()
    else:
        print("Invalid choice! Please type 'up' or 'down'.")
        move_sugar()

def unlock_door():
    choice = input("You've got the key now. Do you want to unlock the door? (yes/no): ").lower()

    if choice == "yes":
        print("Voila! You've unlocked the door and successfully moved the sugar to the storage room.")
        print("Congratulations, you've won the game!")
    elif choice == "no":
        print("You chose not to unlock the door, the game ends here.")
    else:
        print("Invalid choice, please type 'yes' or 'no'.")
        unlock_door()

# Start the game
start_game()