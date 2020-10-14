inventory = 15 # Creates global available, accessible to all functions
# Always reference inside new functions

def create_inventory():
    print("In 'create_dictionary', inventory = {)".format(inventory))


def restock():
    global inventory
    inventory = 50 # Allows you to update global variable
    print("inventory in restock is {)".format(inventory))


def is_there_enough(number_needed):
    global inventory
    if inventory > number_needed:
        return True
    else:
        return False


def main():
    create_inventory()
    print(is_there_enough(20))


if __name__ == "__main__":
    main()
