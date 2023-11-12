import os
import random
import readchar


class Labyrinth:
    def __init__(self, map):
        self.map = map
        self.matrix = self.convert_map()
        self.start = (1, 1)
        self.end = (19, 21)

    def convert_map(self):
        return [list(fila) for fila in self.map.split("\n")]

    def cls_pr(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        # self.show_matrix()

    def show_matrix(self):
        self.cls_pr()
        for fila in self.matrix:
            print(" ".join(fila))

    def main_loop(self):
        x, y = self.start
        while (x, y) != self.end:
            self.matrix[y][x] = "$"
            self.show_matrix()
            tecla = readchar.readkey()
            if tecla == "w":
                if y > 0 and self.matrix[y - 1][x] != "#":
                    self.matrix[y][x] = "."
                    y -= 1
            elif tecla == "s":
                if y < len(self.matrix) - 1 and self.matrix[y + 1][x] != "#":
                    self.matrix[y][x] = "."
                    y += 1
            elif tecla == "a":
                if x > 0 and self.matrix[y][x - 1] != "#":
                    self.matrix[y][x] = "."
                    x -= 1
            elif tecla == "d":
                if x < len(self.matrix[0]) - 1 and self.matrix[y][x + 1] != "#":
                    self.matrix[y][x] = "."
                    x += 1

        self.matrix[y][x] = "$"
        self.show_matrix()
        print(
            "¡Felicitaciones completo el laberinto!")


labyrinth_1 = (
    "#####Labyrinth-1#####\n..###################\n#.......#...#.......#\n#####.#.###.#.#.#.###\n"
    "#.....#...#...#.#...#\n"
    "###.#.###.#########.#\n#...#.#.......#.#...#\n###.#######.###.#.#.#\n#.....#...........#.#\n"
    "#####.#######.#####.#\n#.#...#.....#.#.....#\n#.#####.#.###.###.###\n#.......#.....#.#...#\n"
    "###.###.#######.###.#\n#.#.#.#.#.....#...#.#\n#.#.#.#.###.#.#.###.#\n#...#.......#...#...#\n"
    "###.#.###.###.#####.#\n#...#.#.#.#.#.#.....#\n###.###.#.#.###.#####\n#.......#...#.......#\n"
    "###################.#")

labyrinth_2 = (
    '######Labyrinth-2####\n..###################\n#.#.......#...#.#...#\n#.#####.###.###.#.###\n'
    '#.....#.......#.#...#\n'
    '#.#.###.#######.###.#\n#.#.........#...#...#\n###.###.#####.###.###\n#...#...#.#.........#\n'
    '###.#####.#.#.###.###\n#...#.......#.#.....#\n#.#.###.###.#####.#.#\n#.#.....#.....#.#.#.#\n'
    '#.###.###.###.#.#####\n#.#...#...#.......#.#\n#.#####.###########.#\n#.#...#.............#\n'
    '#.###.#.#.#.#.#####.#\n#.#.....#.#.#...#.#.#\n#.###.###.###.###.#.#\n#...#...#...#.....#.#\n'
    '###################.#')

labyrinths = [labyrinth_1, labyrinth_2]


def choose_labyrinth():
    return random.choice(labyrinths)


selected_labyrinth = choose_labyrinth()
labyrinth = Labyrinth(selected_labyrinth)
labyrinth.main_loop()
