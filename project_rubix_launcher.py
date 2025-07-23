import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QLineEdit, QInputDialog, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ProjectRubixLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.username = None
        self.setWindowTitle("Project Rubix Launcher")
        self.setFixedSize(400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        logo = QLabel("Project Rubix")
        logo.setFont(QFont("Arial", 26, QFont.Bold))
        logo.setStyleSheet("color: #9109c4; background: white;")
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)
        self.login_btn = QPushButton("Zaloguj się")
        self.login_btn.clicked.connect(self.login)
        layout.addWidget(self.login_btn)
        start_btn = QPushButton("Uruchom Fortnite")
        start_btn.clicked.connect(self.start_game)
        layout.addWidget(start_btn)
        exit_btn = QPushButton("Wyjdź")
        exit_btn.clicked.connect(self.close)
        layout.addWidget(exit_btn)
        self.setLayout(layout)

    def login(self):
        username, ok = QInputDialog.getText(self, "Login", "Podaj nazwę użytkownika:")
        if ok and username:
            self.username = username
            QMessageBox.information(self, "Logowanie", f"Zalogowano jako: {self.username}")

    def start_game(self):
        path, ok = QInputDialog.getText(self, "Start", "Podaj ścieżkę do Fortnite.exe:")
        if ok and path:
            try:
                subprocess.Popen([path])
                QMessageBox.information(self, "Launcher", "Fortnite uruchomiony!")
            except Exception as e:
                QMessageBox.warning(self, "Launcher", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ProjectRubixLauncher()
    win.show()
    sys.exit(app.exec_())
