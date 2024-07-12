from install_dependencies import install_dependencies
from title import print_title
from menu import menu

def main():
    install_dependencies()
    print_title()
    menu()

if __name__ == "__main__":
    main()