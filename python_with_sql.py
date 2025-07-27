import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit

class UserApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("משתמשים ממסד נתונים")
        self.resize(400, 300)

        self.layout = QVBoxLayout()
        self.text_area = QTextEdit()
        self.load_button = QPushButton("טען משתמשים")

        self.layout.addWidget(self.text_area)
        self.layout.addWidget(self.load_button)
        self.setLayout(self.layout)

        self.load_button.clicked.connect(self.load_users)

        # יצירת מסד נתונים זמני
        self.init_db()

    def init_db(self):
        self.conn = sqlite3.connect(":memory:")  # מסד נתונים בזיכרון
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        self.cursor.execute("INSERT INTO users (name) VALUES ('יוסי')")
        self.cursor.execute("INSERT INTO users (name) VALUES ('דנה')")
        self.conn.commit()

    def load_users(self):
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        self.text_area.clear()
        for user in users:
            self.text_area.append(f"ID: {user[0]} | שם: {user[1]}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserApp()
    window.show()
    sys.exit(app.exec_())
