import sys
import subprocess
import time

def gitpython_installed():
    try:
        import git
        print("Executing...")
        time.sleep(2)
        print("...")
        time.sleep(1.5)
        print("..")
        time.sleep(1)
        print(".")
        time.sleep(2)
    except ModuleNotFoundError:
        print("GitPython is not installed. Installing GitPython...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gitpython'])
            print("GitPython has been successfully installed.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing GitPython: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    gitpython_installed()
