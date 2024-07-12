from single_repository import single_repository
from multiple_repository import multiple_repository

def menu():
    import keyboard
    
    while True:
        print("Press the corresponding number key to select an option:")
        print("1. Clone a single repository")
        print("2. Clone multiple repositories, previously included in the script")
        print("0. Exit")

        key = keyboard.read_key(suppress=True)

        if key == '1':
            single_repository()
            break
        elif key == '2':
            multiple_repository()
            break
        elif key == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please press 1, 2, or 0")
            print("\n")