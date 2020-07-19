from config import constants
from src.game.app import MacGyverGame

app = MacGyverGame(constants.WIN_TITLE, constants.WIN_BACKGROUND_COLOR,
                   constants.MAZE_CELLS_NUMBER, constants.MAZE_CELLS_SIZE,
                   constants.WIN_ICON)

if __name__ == "__main__":
    app.start()
