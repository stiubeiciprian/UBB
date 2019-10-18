""""
Ski jumps

Ski jump:
    name
    time in air
    avg speed
    wind velocity

1. Read all the info about ski jumps form file and print name and distance.
2. Give back the gold silver and bronze winners and their jump distances.
3. Plot the jumps in a file in the following way:
        ********Gregor********Iane
        * = 1 meter

    Tests and specs

    Distance = time * ( avg speed + avg speed * random(-0.5, 0.5) + wind velocity)
"""
from repository.textFileRepository import TextFileRepository
from service.controller import Controller
from ui.console import Console

repo = TextFileRepository("jumps.txt")


controller = Controller(repo)

console = Console(controller)

console.run()