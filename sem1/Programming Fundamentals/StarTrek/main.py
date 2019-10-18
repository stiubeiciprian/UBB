"""

- 8x8 grid
- randomly placed stars
- randomly placed 3 Blingon ships
- randomly placed USS Endeavour

"""
from service.gameController import GameController
from ui.console import Console

gameController = GameController()

console = Console(gameController)

console.run()