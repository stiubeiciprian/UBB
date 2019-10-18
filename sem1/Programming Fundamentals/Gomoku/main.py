from repository.repository import Repository
from service.gameCont import GameController
from domain.board import GameBoard
from ui.console import Console
from validators.squareValidator import SquareValidator

repo = Repository()
board = GameBoard(repo)
squareValidator = SquareValidator()

gameCont = GameController(board, squareValidator)


ui = Console(gameCont)

ui.run()
