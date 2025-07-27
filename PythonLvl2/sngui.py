from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QTextEdit,
    QLineEdit,
    QStackedLayout,
    QMessageBox,
    QHBoxLayout,
)
import sqlite3
import sys


class SecureNotepad:
    def __init__(self):
        self.connection = sqlite3.connect("notes.db")
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content BLOB NOT NULL
            )
        """
        )
        self.connection.commit()

    def create_note(self, content: str) -> int:
        encoded = content.encode("utf-8")
        self.cursor.execute("INSERT INTO notes (content) VALUES (?)", (encoded,))
        self.connection.commit()
        return self.cursor.lastrowid

    def view_note(self, note_id: int):
        self.cursor.execute("SELECT content FROM notes WHERE id = ?", (note_id,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        return row[0].decode("utf-8")

    def update_note(self, note_id: int, new_content: str) -> bool:
        encoded = new_content.encode("utf-8")
        self.cursor.execute(
            "UPDATE notes SET content = ? WHERE id = ?", (encoded, note_id)
        )
        self.connection.commit()
        return self.cursor.rowcount > 0

    def list_notes(self):
        self.cursor.execute("SELECT id, content FROM notes ORDER BY id ASC")
        rows = self.cursor.fetchall()
        return [(row[0], row[1].decode("utf-8")) for row in rows]

    def delete_note(self, note_id: int) -> bool:
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def reset_db(self):
        self.cursor.execute("DELETE FROM notes")
        self.connection.commit()

    def close(self):
        self.connection.close()


class NotepadGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.notepad = SecureNotepad()
        self.setWindowTitle("Secure Notepad")
        self.resize(400, 300)

        self.layout = QStackedLayout()
        self.init_main_menu()
        self.init_create_note()
        self.init_view_note()
        self.init_update_note()
        self.init_list_notes()
        self.init_delete_note()

        self.setLayout(self.layout)

    def init_main_menu(self):
        self.menu_widget = QWidget()
        vbox = QVBoxLayout()

        vbox.addWidget(QLabel("Secure Notepad Menu"))

        buttons = [
            ("Create Note", self.show_create_note),
            ("View Note", self.show_view_note),
            ("Update Note", self.show_update_note),
            ("List Notes", self.show_list_notes),
            ("Delete Note", self.show_delete_note),
            ("Reset DB", self.reset_db),
            ("Exit", self.close),
        ]

        for text, func in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(func)
            vbox.addWidget(btn)

        self.menu_widget.setLayout(vbox)
        self.layout.addWidget(self.menu_widget)

    def init_create_note(self):
        self.create_widget = QWidget()
        vbox = QVBoxLayout()
        self.create_input = QTextEdit()
        vbox.addWidget(QLabel("Enter note content:"))
        vbox.addWidget(self.create_input)

        btn_save = QPushButton("Save Note")
        btn_save.clicked.connect(self.save_note)
        vbox.addWidget(btn_save)

        btn_back = QPushButton("Back")
        btn_back.clicked.connect(lambda: self.layout.setCurrentWidget(self.menu_widget))
        vbox.addWidget(btn_back)

        self.create_widget.setLayout(vbox)
        self.layout.addWidget(self.create_widget)

    def init_view_note(self):
        self.view_widget = QWidget()
        vbox = QVBoxLayout()

        self.view_id_input = QLineEdit()
        self.view_output = QLabel()
        self.view_output.setWordWrap(True)

        vbox.addWidget(QLabel("Enter note ID to view:"))
        vbox.addWidget(self.view_id_input)

        btn_view = QPushButton("View Note")
        btn_view.clicked.connect(self.view_note)
        vbox.addWidget(btn_view)
        vbox.addWidget(self.view_output)

        btn_back = QPushButton("Back")
        btn_back.clicked.connect(lambda: self.layout.setCurrentWidget(self.menu_widget))
        vbox.addWidget(btn_back)

        self.view_widget.setLayout(vbox)
        self.layout.addWidget(self.view_widget)

    def init_update_note(self):
        self.update_widget = QWidget()
        vbox = QVBoxLayout()

        self.update_id_input = QLineEdit()
        self.update_content_input = QTextEdit()

        vbox.addWidget(QLabel("Enter note ID to update:"))
        vbox.addWidget(self.update_id_input)
        vbox.addWidget(QLabel("Enter new content:"))
        vbox.addWidget(self.update_content_input)

        btn_update = QPushButton("Update Note")
        btn_update.clicked.connect(self.update_note)
        vbox.addWidget(btn_update)

        btn_back = QPushButton("Back")
        btn_back.clicked.connect(lambda: self.layout.setCurrentWidget(self.menu_widget))
        vbox.addWidget(btn_back)

        self.update_widget.setLayout(vbox)
        self.layout.addWidget(self.update_widget)

    def init_list_notes(self):
        self.list_widget = QWidget()
        vbox = QVBoxLayout()

        self.list_output = QLabel()
        self.list_output.setWordWrap(True)

        btn_refresh = QPushButton("Refresh Notes")
        btn_refresh.clicked.connect(self.display_notes)
        vbox.addWidget(btn_refresh)
        vbox.addWidget(self.list_output)

        btn_back = QPushButton("Back")
        btn_back.clicked.connect(lambda: self.layout.setCurrentWidget(self.menu_widget))
        vbox.addWidget(btn_back)

        self.list_widget.setLayout(vbox)
        self.layout.addWidget(self.list_widget)

    def init_delete_note(self):
        self.delete_widget = QWidget()
        vbox = QVBoxLayout()

        self.delete_id_input = QLineEdit()

        vbox.addWidget(QLabel("Enter note ID to delete:"))
        vbox.addWidget(self.delete_id_input)

        btn_delete = QPushButton("Delete Note")
        btn_delete.clicked.connect(self.delete_note)
        vbox.addWidget(btn_delete)

        btn_back = QPushButton("Back")
        btn_back.clicked.connect(lambda: self.layout.setCurrentWidget(self.menu_widget))
        vbox.addWidget(btn_back)

        self.delete_widget.setLayout(vbox)
        self.layout.addWidget(self.delete_widget)

    def show_create_note(self):
        self.create_input.clear()
        self.layout.setCurrentWidget(self.create_widget)

    def show_view_note(self):
        self.view_id_input.clear()
        self.view_output.clear()
        self.layout.setCurrentWidget(self.view_widget)

    def show_update_note(self):
        self.update_id_input.clear()
        self.update_content_input.clear()
        self.layout.setCurrentWidget(self.update_widget)

    def show_list_notes(self):
        self.display_notes()
        self.layout.setCurrentWidget(self.list_widget)

    def show_delete_note(self):
        self.delete_id_input.clear()
        self.layout.setCurrentWidget(self.delete_widget)

    def save_note(self):
        content = self.create_input.toPlainText()
        if content:
            note_id = self.notepad.create_note(content)
            QMessageBox.information(self, "Success", f"Note saved with ID {note_id}")
            self.layout.setCurrentWidget(self.menu_widget)
        else:
            QMessageBox.warning(self, "Warning", "Note content cannot be empty.")

    def view_note(self):
        try:
            note_id = int(self.view_id_input.text())
            content = self.notepad.view_note(note_id)
            if content:
                self.view_output.setText(content)
            else:
                self.view_output.setText("Note not found.")
        except ValueError:
            self.view_output.setText("Invalid ID.")

    def update_note(self):
        try:
            note_id = int(self.update_id_input.text())
            content = self.update_content_input.toPlainText()
            if self.notepad.update_note(note_id, content):
                QMessageBox.information(self, "Updated", "Note updated successfully.")
                self.layout.setCurrentWidget(self.menu_widget)
            else:
                QMessageBox.warning(self, "Error", "Note not found.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid ID.")

    def display_notes(self):
        notes = self.notepad.list_notes()
        if not notes:
            self.list_output.setText("No notes found.")
        else:
            self.list_output.setText("\n".join([f"{nid}: {text}" for nid, text in notes]))

    def delete_note(self):
        try:
            note_id = int(self.delete_id_input.text())
            if self.notepad.delete_note(note_id):
                QMessageBox.information(self, "Deleted", "Note deleted successfully.")
                self.layout.setCurrentWidget(self.menu_widget)
            else:
                QMessageBox.warning(self, "Error", "Note not found.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid ID.")

    def reset_db(self):
        self.notepad.reset_db()
        QMessageBox.information(self, "Reset", "All notes have been deleted.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotepadGUI()
    window.show()
    sys.exit(app.exec_())
