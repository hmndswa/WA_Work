"""
Secure Notepad Application
It allows creating, viewing, and updating notes from the command line.
"""

import sqlite3
from typing import Optional


class SecureNotepad:
    """
    Handles creating, viewing, and updating notes with auto-generated IDs.
    """

    def __init__(self) -> None:
        """
        Connects to SQLite Database and ensures if the notes table exists.
        """
        self.connection = sqlite3.connect("notes.db")
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self) -> None:
        """
        Create notes table if it doesnt exist.
        """
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
        """
        Create a new note, store it in the database and return its ID
        """
        encoded = content.encode("utf-8")
        self.cursor.execute("INSERT INTO notes (content) VALUES (?)", (encoded,))
        self.connection.commit()
        return self.cursor.lastrowid

    def view_note(self, note_id: int) -> Optional[str]:
        """
        Get the content of a note from the database based on its ID.

        Args:
            note_id: ID of note to view

        Returns:
            Decoded note as a string if found if not NONE.
        """
        self.cursor.execute("SELECT content FROM notes WHERE id = ?", (note_id,))
        row = self.cursor.fetchone()

        if row is None:
            return None
        return row[0].decode("utf-8")

    def update_note(self, note_id: int, new_content: str) -> bool:
        """
        Update the content of a note by ID in database.

        Args:
            note_id: ID of the note to update
            new_content: New content to store

        Returns:
            True if note was updated and False if not.
        """
        encoded = new_content.encode("utf-8")
        self.cursor.execute(
            "UPDATE notes SET content = ? WHERE id = ?", (encoded, note_id)
        )
        self.connection.commit()
        return self.cursor.rowcount > 0

    def list_notes(self) -> None:
        """
        List all notes from the database, sorted by ID (ascending).
        """
        self.cursor.execute("SELECT id, content FROM notes ORDER BY id ASC")
        rows = self.cursor.fetchall()

        if not rows:
            print("No notes found.")
        else:
            for note_id, content in rows:
                print(f"{note_id}: {content.decode('utf-8')}")

    def delete_note(self, note_id: int) -> bool:
        """
        Delete a note by its ID.

        Args:
            note_id: ID of the note to delete

        Returns:
            True if a note was deleted, False otherwise.
        """
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def close(self) -> None:
        """Close the SQLite connection."""
        self.connection.close()


def main() -> None:
    """
    Handles user input for creating, viewing, updating,
    and listing notes until the user chooses to exit.
    """
    notepad = SecureNotepad()
    while True:
        print("\n--- Secure Notepad ---")
        print("1. Create Note")
        print("2. View Note")
        print("3. Update Note")
        print("4. List Notes")
        print("5. Delete Notes")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            content = input("Enter note content: ")
            note_id = notepad.create_note(content)
            print(f"Note created with ID: {note_id}")

        elif choice == "2":
            try:
                note_id = int(input("Enter note ID: "))
                note = notepad.view_note(note_id)
                if note is not None:
                    print(f"Note {note_id}: {note}")
                else:
                    print("Note not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "3":
            try:
                note_id = int(input("Enter note ID: "))
                new_content = input("Enter new content: ")
                success = notepad.update_note(note_id, new_content)
                if success:
                    print("Note updated.")
                else:
                    print("Note not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "4":
            notepad.list_notes()

        elif choice == "5":
            try:
                note_id = int(input("Enter note ID to delete: "))
                deleted = notepad.delete_note(note_id)
                if deleted:
                    print("Note deleted.")
                else:
                    print("Note not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "6":
            print("Exiting Secure Notepad.")
            notepad.close()
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
