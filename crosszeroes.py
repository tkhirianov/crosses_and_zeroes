import pygame
from model import *

FPS = 60
CELL_SIZE = 50


class GameFieldView:
    """
    Виджет игрового поля, который отображает его на экране, а также выясняет место клика.
    """
    def __init__(self, field):
        # загрузить картинки значков клеток...
        # отобразить первичное состояние поля
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self, x, y):
        return True  # TODO: self._height учесть

    def get_coords(self, x, y):
        return 0, 0  # TODO: реально вычислить клетку клика


class ChoosePlayersManager:
    """
    Менеджер игры, запускающий все игровые процессы.
    """
    pass


class GameRoundManager:
    """
    Менеджер игры, запускающий все игровые процессы.
    """

    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player_index = 0
        self._field = GameField()

    def handle_click(self, i, j):
        player = self._players[self._current_player_index]
        # игрок делает клик на поле
        print("click_handled",  i, j)


class GameWindow:
    """
    Содержит виджет поля,
    а также менеджера игрового раунда.
    """
    def __init__(self):
        # инициализация pygame
        pygame.init()

        self._width = 800
        self._height = 600
        self._title = "Crosses & Zeroes"
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)

        player1 = HumanPlayer(Cell.CROSS)
        player2 = AIPlayer(Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos
                    if self._field_widget.check_coords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)
            pygame.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.main_loop()
    print('Game over!')


if __name__ == "__main__":
    main()