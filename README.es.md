```md
      _____                                    __  __                  __         _____       
     /\  _` \                                 /\ \/\ \                /\ \       /\  __`\     
     \ \ \/\_\    ___   _____   __  __        \ \ \ \ \  _____     ___\ \ \     _\ \ \/\ \    
      \ \ \/_/_  / __`\/\ '__`\/\ \/\ \  ______\ \ \ \ \/\ '__`\  /',__\ \ \   /\_\ \ \ \ \   
       \ \ \L\ \/\ \L\ \ \ \L\ \ \ \_\ \/\______\ \ \_\ \ \ \L\ \/\__, `\ \_\  \/_/\ \ \_\ \  
        \ \____/\ \____/\ \ ,__/\/`____ \/______/\ \_____\ \ ,__/\/\____/\/\_\   /\_\ \_____\ 
         \/___/  \/___/  \ \ \/  `/___/> \        \/_____/\ \ \/  \/___/  \/_/   \/_/\/_____/ 
                          \ \_\     /\___/                 \ \_\                              
                           \/_/     \/__/                   \/_/                              
```
                      
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/sergiJimenez/copyUps/blob/master/README.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/sergiJimenez/copyUps/blob/master/README.es.md)

## Descripción

Copy-Ups! :O es un CLI desarrollado en Python cuya finalidad es clonar uno o múltiples repositorios. Una de las funciones que tiene al seleccionar cualquiera de las dos características que este CLI te brinda es el hecho de que si encuentra un repositorio con el mismo nombre, eliminará dicho repositorio con la finalidad de no tener copias del mismo.

## Requisitos

Para poder utilizarlo es necesario instalar Python en cualquier versión. Para comprobar si lo tenéis instalado simplemente tenéis que ejecutar el siguiente comando:

```powershell
python --version
```

Un aspecto **MUY IMPORTANTE** a tener en cuenta es el hecho de que poder eliminar directorios mediante un terminal requiere de utilizar un superusuario (sudo) así que deberemos ejecutar el programa como administradores en Windows o utilizar el comando `sudo su` en Linux/Unix.

## Instalación

Para instalar este repositorio solo necesitaremos clonarlo ya que todos los paquetes necesarios para utilizarlo se instalarán la primera vez que lo ejecutemos.

## Uso

Para utilizarlo tendremos que ubicarnos dentro de él con una terminal y ejecutar el comando:

```powershell
python .\main.py
# o
python3 main.py
```

Si es la primera vez que lo ejecutamos observaremos que se instalan los paquetes necesarios para poder ser utilizado. Una vez estos terminen podremos elegir cualquiera de las opciones del menu.

## Funcionalidades

- Clonar un repositorio: esta funcionalidad nos permite clonar el repositorio que nosotros le indiquemos. Lo primero que nos preguntará será la URL de dicho repositorio que tendremos que escribir, o pegar. Y, para finalizar nos pedirá la ruta donde queramos alojar dicho repositorio. Si el repositorio ya existe en la ruta que le hemos indicado previamente lo borrará y clonará el nuevo.
- Clonar multiples repositorios: esta funcionalidad es similar a la anterior pero requiere de una previa preparación. Para utilizar dicha funcionalidad tendremos que utilizar un editor de código, o un editor de texto, y abriremos el archivo “multiple_repositories.py”. En el array de string llamado `repo_urls` añadiremos todas las URL’s de los repositorios que queramos clonar y en la variable string `base_path` incluiremos la ruta donde queramos que estos sean copiados.
Es recomendable dejar la “`r`” que se encuentra delante de las doble comillas donde introduciremos la ruta donde alojemos alojar los repositorios ya que esta se encarga de formatear las rutas en Windows ya que estas utilizan una barra inversa.

**ES IMPORTANTE QUE TENGAMOS EN CUENTA QUE LOS REPOSITORIOS PRIVADOS NOS PREGUNTARÁ POR EL USUARIO Y CONTRASEÑA DE GITHUB.**
