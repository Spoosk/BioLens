import sys
import os
import subprocess
import time
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer
import webview

# Try to set Windows taskbar icon
try:
    import ctypes
    myappid = 'BioLens.TrailCam.Processor'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except:
    pass

from CSVDateCleaner import clean_csv

# Nature theme stylesheet
NATURE_STYLESHEET = """
    QWidget {
        background-color: #f5f5f0;
        color: #2d3d2d;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 11pt;
    }
    QPushButton {
        background-color: #4a7c59;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #5a9c6f;
    }
    QPushButton:pressed {
        background-color: #2d5a3d;
    }
    QPushButton:disabled {
        background-color: #a0a0a0;
        color: #cccccc;
    }
    QLabel {
        color: #2d3d2d;
    }
    QFileDialog {
        background-color: #f5f5f0;
    }
"""

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BioLens Trail Cam Processor")
        self.setGeometry(100, 100, 500, 250)
        self.setStyleSheet(NATURE_STYLESHEET)
        
        # Icon will be set after window is shown for proper taskbar display

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

            # Close the current window and open the dashboard in a native webview window
            self.close()
            webview.create_window('BioLens Trail Cam Dashboard', 'http://127.0.0.1:8050/')
            webview.start()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    # Set icon after window is shown to ensure taskbar gets it
    def set_taskbar_icon():
        icon = QIcon("icon.ico")
        app.setWindowIcon(icon)
        window.setWindowIcon(icon)
        # Force repaint
        window.repaint()
    
    # Use timer to set icon after event loop starts
    QTimer.singleShot(100, set_taskbar_icon)
    
    sys.exit(app.exec())