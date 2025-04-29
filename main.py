from PySide6.QtWidgets import QApplication
import sys
from gui.main_window import MainWindow
import logging

if __name__ == "__main__":

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    logging.info("Resume generator started")
    sys.exit(app.exec())