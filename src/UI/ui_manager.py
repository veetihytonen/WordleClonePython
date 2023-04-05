from ui.game_view import GameView

class UIManager:
    def __init__(self, root) -> None:
        self._root = root
        self._current_view = None

    def start(self):
        self._draw_game_view()


    def _draw_game_view(self):
        self._current_view = GameView(self._root)
        
    