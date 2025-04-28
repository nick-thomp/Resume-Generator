from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

class PreviewWindow(QMainWindow):
    def __init__(self, html_content):
        super().__init__()
        self.setWindowTitle("Resume Preview")
        self.setMinimumSize(800, 600)

        widget = QWidget()
        layout = QVBoxLayout(widget)

        self.webview = QWebEngineView()
        self.webview.setHtml(html_content)

        layout.addWidget(self.webview)
        self.setCentralWidget(widget)
