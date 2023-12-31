""""Proyecto Integrador parte 1
El proyecto de este curso consistirá en un videojuego de texto de recorrer laberintos. Este consistirá de laberintos representados por caracteres ASCII dónde # representará una pared, . un pasillo y P el personaje.

Podrás moverte por el mapa usando las teclas ↑ ↓ ← → de tu teclado.

Una vez terminado el proyecto deberá verse así:


Nota: La razón de tener todos el mismo proyecto es para poder realizar un seguimiento estandarizado del avance y permitir la cooperación entre compañeros en caso de dificultades

Una vez presentado el proyecto, pasemos a la primera parte de este:

Crea un repositorio de Github para el proyecto, en este repositorio realiza lo siguiente:

Crear un archivo README.md con la descripción del proyecto escrita por ti, esta será tu documentación del proyecto.
Crear el archivo main del proyecto.
Pedir el nombre del jugador por teclado.
Imprimir un mensaje de bienvenida con el nombre."""

# impotaciones de los paquetes de python
from readchar import readkey, key
import os
import readchar

# primer paso del proyecto
# pedir el nombre del jugador
player_name = input("Add your name: ")
print(f"Welcome to my Integrator Project, your name is {player_name}, white yes or no to continue...\n")

EXIT_KEY = readchar.key.UP

def cls_pr(n):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(n)


EXIT_KEY = readchar.key.UP
n = 0
while True:
    key = readchar.readkey()
    if key == 'n':
        n += 1
        if n > 50:
            break
        cls_pr(n)
