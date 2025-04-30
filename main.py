import sys
import logging
import argparse
from pdf_generator import generate_html, generate_pdf
from gui.main_window import MainWindow
from PySide6.QtWidgets import QApplication

def run_cli():
    parser = argparse.ArgumentParser(description="Resume Generator CLI")
    parser.add_argument("--yaml", type=str, required=True, help="Path to YAML resume file")
    parser.add_argument("--template", type=str, default="basic.html", help="Template to use")
    parser.add_argument("--output", type=str, default="output.pdf", help="Output PDF file name")
    args = parser.parse_args()

    logging.info("CLI mode started with arguments: %s", args)

    html_result = generate_html(resume=args.yaml, template=args.template)
    if html_result['status'] == 'Error':
        print(f"❌ {html_result['message']}")
        return
    
    pdf_result = generate_pdf(html_out=html_result['message'], target_job=args.output) # pdf name is usually target_job, but in this case it's not so that will change in the future
    if pdf_result.get("status") == "Error":
        print(f"❌ {pdf_result['message']}")
    else:
        print(f"✅ {pdf_result['message']}")

def run_gui():
    logging.info("Launching GUI mode")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    logging.info("Resume generator started")
    sys.exit(app.exec())

def main():
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

    if len(sys.argv) > 1:
        run_cli()
    else:
        run_gui()


if __name__ == "__main__":
    main()