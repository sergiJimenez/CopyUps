from scripts.install_dependencies import install_dependencies
from scripts.title import print_title
from scripts.menu import menu

def main():
    install_dependencies()
    print_title()
    menu()

if __name__ == "__main__":
    main()