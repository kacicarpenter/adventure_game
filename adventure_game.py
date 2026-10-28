def banner(message):
    print("---------- " + message + " ----------")

# Introduces the earthquake.
# Parameters: None
# Return: None
def stay_home():
    banner("Home")
    print("You decided to stay home and relax.")
    print("ALERT: An earthquake is coming!")

# Introduces the tsunami.
# Parameters: None
# Return: None
def go_beach():
    banner("Beach")
    print("You decided to spend the day at the beach.")
    print("ALERT: A tsunami is coming!")

# Calculates the player's remaining health.
# Parameter: damage (integer)
# Return: integer representing remaining health
def health_update(damage):
    health = 100 - damage
    print("Your health is:", health)
    return health

# Handles the emergency kit.
# Parameter: choice (string)
# Return: integer representing health lost
def emergency_kit(choice):
    if choice == "yes":
        print("You picked up the emergency kit!")
        return 0
    else:
        print("You left the emergency kit.")
        return 30

# Starts the game and handles player decisions.
# Parameters: None
# Return: None
def main():
    banner("Welcome to Disaster Escape!")

    history = ["Home"]

    print("You are home on your day off.")
    print("Where would you like to go?")
    print("1. Stay home")
    print("2. Go to the beach")

    choice = input("Enter 1 or 2: ")
    if choice == "1":
        stay_home()
        print("Where will you hide?")
        print("1. Under the doorway")
        print("2. Under a table")

        decision = input("Enter 1 or 2: ")
        if decision == "1":
            history.append("Doorway")
            banner("Game Result")
            print("The earthquake has hit!")
            health = health_update(80)

        elif decision == "2":
            history.append("Table")
            print("There is an emergency kit on the table.")
            kit = input("Pick it up? yes/no: ").lower()

            damage = emergency_kit(kit)

            banner("Game Result")
            print("The earthquake has hit!")
            health = health_update(damage)

        else:
            print("Invalid choice.")
            return

    elif choice == "2":
        go_beach()
        history.append("Beach")

        print("Where will you go?")
        print("1. Boardwalk")
        print("2. Roof of a nearby building")

        decision = input("Enter 1 or 2: ")

        if decision == "1":
            history.append("Boardwalk")
            banner("Game Result")
            print("The tsunami has hit!")
            health = health_update(80)
        elif decision == "2":
            history.append("Roof")
            banner("Game Result")
            print("The tsunami has hit!")
            health = health_update(0)
        else:
            print("Invalid choice.")
            return
    else:
        print("Invalid choice.")
        return

    if health < 60:
        print("You were injured. You lost!")
    elif health == 70:
        print("You survived with some injury. You win!")
    else:
        print("You are safe! You win!")
    print("Your path:", history)

main()