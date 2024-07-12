from install_dependencies import install_dependencies
from title import print_title
from menu import menu

def show_menu():
    install_dependencies()
    print_title()
    menu()

if __name__ == "__main__":
    show_menu()