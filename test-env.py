import sys
import subprocess

print("Intérprete de Python:", sys.executable)

try:
    from git import Repo
    print("GitPython está instalado correctamente.")
except ModuleNotFoundError:
    print("GitPython no está instalado en este entorno.")
    print("Instalando GitPython...")

    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gitpython'])
        print("GitPython se ha instalado correctamente.")
        from git import Repo  # Intentar importar nuevamente después de la instalación
    except subprocess.CalledProcessError:
        print("Hubo un problema al instalar GitPython. Por favor, instálalo manualmente.")
    except ImportError:
        print("No se pudo importar GitPython después de la instalación. Verifica la instalación manualmente.")
