from entities.game import Game
from path_config import save_file_path


class GameView:
    def __init__(self, root) -> None:
        self._root = root
        self._game = None

        if self._SAVE_FILE_is_empty:
            self._game = Game("broke")
        else:
            self._game = Game.read_save_from_binary(save_file_path)


    def _SAVE_FILE_is_empty(self):
        if save_file_path.stat().st_size == 0:
            return True
        
        return False

   