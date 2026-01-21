import sys
import os
import subprocess
import webbrowser
import time
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, QMessageBox

from CSVDateCleaner import clean_csv

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BioLens Trail Cam Processor")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Select a CSV file to process:")
        layout.addWidget(self.label)

        self.select_button = QPushButton("Select File")
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        self.process_button = QPushButton("Process and Open Dashboard")
        self.process_button.clicked.connect(self.process_file)
        self.process_button.setEnabled(False)
        layout.addWidget(self.process_button)

        self.status_label = QLabel("")
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        self.selected_file = None

    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)")
        if file_path:
            self.selected_file = file_path
            self.label.setText(f"Selected: {os.path.basename(file_path)}")
            self.process_button.setEnabled(True)

    def process_file(self):
        if not self.selected_file:
            return

        try:
            self.status_label.setText("Cleaning data...")
            QApplication.processEvents()  # Update UI

            cleaned_file = clean_csv(self.selected_file)

            self.status_label.setText("Starting dashboard...")
            QApplication.processEvents()

            # Run Dash in a separate process
            python_exe = sys.executable
            subprocess.Popen([python_exe, "Trailcam_Grapher.py", cleaned_file])

            # Wait a bit for server to start
            time.sleep(3)

            # Open browser
            webbrowser.open("http://127.0.0.1:8050/")

            self.status_label.setText("Dashboard opened in browser.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())