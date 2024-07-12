import sys
import subprocess

def install_dependencies():
    try:
        try:
            import git
        except ModuleNotFoundError:
            print("GitPython is not installed. Installing GitPython...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gitpython'])
            print("GitPython has been successfully installed.")
        
        try:
            import keyboard
        except ModuleNotFoundError:
            print("keyboard is not installed. Installing keyboard...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'keyboard'])
            print("keyboard has been successfully installed.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")