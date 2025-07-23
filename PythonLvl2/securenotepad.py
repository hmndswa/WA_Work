"""
Secure Notepad Application
It allows creating, viewing, and updating notes from the command line.
"""

from typing import Optional


class Note:
    """
    Stores note ID and the content encoded as bytes.
    Represents a single note.
    """

    def __init__(self, note_id: int, content: str) -> None:
        """
        Initialize a new Note with an ID and content.
        """
        self.id: int = note_id
        self._encoded_content: bytes = content.encode("utf-8")

    def get_content(self) -> str:
        """
        Decode and return the note content as a string.
        """
        return self._encoded_content.decode("utf-8")

    def update_content(self, new_content: str) -> None:
        """
        Update the note content and re-encode it.
        """
        self._encoded_content = new_content.encode("utf-8")


class SecureNotepad:
    """
    Handles creating, viewing, and updating notes with auto-generated IDs.
    """

    def __init__(self) -> None:
        """Initialize an empty notepad with an ID counter."""
        self.notes: dict[int, Note] = {}
        self.next_id: int = 1

    def create_note(self, content: str) -> int:
        """
        Create a new note and store it.
        """
        note = Note(self.next_id, content)
        self.notes[self.next_id] = note
        self.next_id += 1
        return note.id

    def view_note(self, note_id: int) -> Optional[str]:
        """
        Get the content of a note by ID.
        """
        note = self.notes.get(note_id)
        if note is None:
            return None
        return note.get_content()

    def update_note(self, note_id: int, new_content: str) -> bool:
        """
        Update the content of a note by ID.
        """
        note = self.notes.get(note_id)
        if note is None:
            return False
        note.update_content(new_content)
        return True


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
        print("5. Exit")

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
            if not notepad.notes:
                print("No notes found.")
            else:
                for note_id, note in notepad.notes.items():
                    print(f"{note_id}: {note.get_content()}")

        elif choice == "5":
            print("Exiting Secure Notepad.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
