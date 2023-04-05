from tkinter import Tk
from ui.ui_manager import UIManager


def main():
    window = Tk()
    window.title('Highly Illegal Bootleg Wordle')

    ui_view = UIManager(window)
    ui_view.start()

    window.mainloop()


if __name__ == '__main__':
    main()