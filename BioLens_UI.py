import sys
import os
import subprocess
import time
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QFont, QColor, QPalette
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

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🌿 BioLens Trail Cam Processor")
        self.setGeometry(100, 100, 500, 350)
        
        # Apply nature theme to window
        self._apply_nature_theme()
        
        # Icon will be set after window is shown for proper taskbar display

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)

        # Title label
        title_label = QLabel("🌿 BioLens Trail Cam Processor")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        layout.addWidget(title_label)
        
        # Description
        desc_label = QLabel("Wildlife camera data analysis and visualization")
        desc_font = QFont()
        desc_font.setPointSize(10)
        desc_label.setFont(desc_font)
        desc_label.setStyleSheet("color: #5a7a6a;")
        layout.addWidget(desc_label)

        self.label = QLabel("Select a CSV file to process:")
        label_font = QFont()
        label_font.setPointSize(11)
        label_font.setBold(True)
        self.label.setFont(label_font)
        layout.addWidget(self.label)

        self.select_button = self._create_styled_button("📁 Select File")
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        self.process_button = self._create_styled_button("⚙️ Process and Open Dashboard", is_primary=True)
        self.process_button.clicked.connect(self.process_file)
        self.process_button.setEnabled(False)
        layout.addWidget(self.process_button)

        self.status_label = QLabel("")
        status_font = QFont()
        status_font.setPointSize(10)
        status_font.setItalic(True)
        self.status_label.setFont(status_font)
        self.status_label.setStyleSheet("color: #4a7c59;")
        layout.addWidget(self.status_label)
        
        layout.addStretch()

        self.setLayout(layout)

        self.selected_file = None
    
    def _apply_nature_theme(self):
        """Apply nature-themed colors and styling to the window."""
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#f5f5f0"))
        palette.setColor(QPalette.WindowText, QColor("#2d3d2d"))
        palette.setColor(QPalette.Base, QColor("#ffffff"))
        palette.setColor(QPalette.Text, QColor("#2d3d2d"))
        palette.setColor(QPalette.Button, QColor("#e8f0e8"))
        palette.setColor(QPalette.ButtonText, QColor("#2d3d2d"))
        self.setPalette(palette)
    
    def _create_styled_button(self, text, is_primary=False):
        """Create a nature-themed button."""
        button = QPushButton(text)
        button.setMinimumHeight(45)
        button.setFont(QFont("Arial", 11))
        
        if is_primary:
            button.setStyleSheet("""
                QPushButton {
                    background-color: #4a7c59;
                    color: white;
                    border: none;
                    border-radius: 6px;
                    font-weight: bold;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #3a6a49;
                }
                QPushButton:pressed {
                    background-color: #2a5a39;
                }
                QPushButton:disabled {
                    background-color: #b0b0a0;
                    color: #707070;
                }
            """)
        else:
            button.setStyleSheet("""
                QPushButton {
                    background-color: #e8f0e8;
                    color: #2d3d2d;
                    border: 2px solid #4a7c59;
                    border-radius: 6px;
                    font-weight: bold;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #d8e8d8;
                    border: 2px solid #3a6a49;
                }
                QPushButton:pressed {
                    background-color: #c8e0c8;
                }
            """)
        return button

    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)")
        if file_path:
            self.selected_file = file_path
            self.label.setText(f"✓ Selected: {os.path.basename(file_path)}")
            self.status_label.setText("")
            self.process_button.setEnabled(True)

    def process_file(self):
        if not self.selected_file:
            return

        try:
            self.status_label.setText("🔄 Cleaning data...")
            QApplication.processEvents()  # Update UI

            cleaned_file = clean_csv(self.selected_file)

            self.status_label.setText("🌍 Starting dashboard...")
            QApplication.processEvents()

            # Run Dash in a separate process
            python_exe = sys.executable
            subprocess.Popen([python_exe, "Trailcam_Grapher.py", cleaned_file])

            # Wait a bit for server to start
            time.sleep(3)

            # Close the current window and open the dashboard in a native webview window
            self.close()
            webview.create_window('🌿 BioLens Trail Cam Dashboard', 'http://127.0.0.1:8050/')
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