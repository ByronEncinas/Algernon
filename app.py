import sys, os

from rich.console import Console
from PyQt6.QtWidgets import QApplication, QMainWindow

curPath = os.getcwd().split('\\')

console = Console()

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setFixedWidth(600)
        self.setFixedHeight(300)
        self.setWindowTitle("Algernon Gui")

def App():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    # testing PyQt6
    window = MainWindow().Run()