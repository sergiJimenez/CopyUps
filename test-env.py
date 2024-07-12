import sys
print("Intérprete de Python:", sys.executable)

try:
    from git import Repo
    print("GitPython está instalado correctamente.")
except ModuleNotFoundError:
    print("GitPython no está instalado en este entorno.")
