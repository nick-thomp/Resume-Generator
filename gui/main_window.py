import sys
from PySide6.QtWidgets import QListWidget, QMainWindow, QHBoxLayout, QTextEdit, QVBoxLayout, QPushButton, QWidget, QScrollArea, QLabel, QMessageBox
from PySide6.QtWebEngineWidgets import QWebEngineView
import os
import yaml
from pdf_generator import generate_pdf, generate_html
from functools import partial
from .preview_window import PreviewWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Resume Builder")
        self.setGeometry(200, 200, 600, 400)

        self.resume_list = None
        self.parsed_resume = None
        self.resumes_dir = os.path.join(os.getcwd(), 'resumes')
        self.init_ui()
    
    def get_resumes(self):
        resume_list = 'resumes'
        self.resume_list = [f for f in os.listdir(resume_list) if f.endswith('.yaml')]
        self.resume_btn_list.clear()
        for resume in self.resume_list:
            self.resume_btn_list.addItem(resume)

    def init_ui(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        double_btn_layout = QHBoxLayout()

        # Resume button list
        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.get_resumes)
        self.resume_btn_list = QListWidget()
        self.resume_btn_list.itemClicked.connect(self.update_resume_preview)
        left_layout.addWidget(self.refresh_btn)
        left_layout.addWidget(self.resume_btn_list)

        # Step preview and ( run btn | preview btn )
        self.resume_preview = QTextEdit()
        self.resume_preview.setReadOnly(True)
        self.generate_pdf_btn = QPushButton("Generate PDF")
        self.generate_pdf_btn.clicked.connect(self.generate_pdf)
        self.preview_html_btn = QPushButton("Preview PDF")
        self.preview_html_btn.clicked.connect(self.open_preview)

        double_btn_layout.addWidget(self.generate_pdf_btn)
        double_btn_layout.addWidget(self.preview_html_btn)

        right_layout.addWidget(self.resume_preview)
        right_layout.addLayout(double_btn_layout)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        # Set the layout
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.get_resumes()

    def update_resume_preview(self, item):
        if not os.path.exists(f"{self.resumes_dir}/{item.text()}"):
            return self.get_resumes()
        with open(f"{self.resumes_dir}/{item.text()}", "r") as f:
            self.parsed_resume = yaml.safe_load(f)
        resume_data = yaml.dump(self.parsed_resume, default_flow_style=False)

        self.resume_preview.setText(resume_data)

    def generate_pdf(self):
        # Trigger the generate pdf function with parsed yaml file
        # first generate html then send it to the pdf function
        html_result = generate_html(resume = self.parsed_resume)
        if html_result['status'] == 'Error':
            self.show_message(result['message'], result['status'])
            return None
        result = generate_pdf(html_out=html_result['message'], target_job=self.parsed_resume['target_job_title'])
        self.show_message(result['message'], result['status'])

    def open_preview(self):
        # generate html and pass it to the preview window
        result = generate_html(resume=self.parsed_resume)
        if result['status'] == "Error":
            self.show_message(result['message'], result['status'])
        self.preview_window = PreviewWindow(result['message'])
        self.preview_window.show()

    def show_message(self, message, title):
        msg_box = QMessageBox()
        if title == 'Error':
            msg_box.setIcon(QMessageBox.Critical)
        else:
            msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()