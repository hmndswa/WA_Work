def open_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        lines = content.splitlines()
        words = content.split()
        characters = len(content)

        print(f"Final Result for '{filename}':")
        print("Number of lines:", len(lines))
        print("Number of words:", len(words))
        print("Number of characters:", characters)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

open_file("Week1/Bonus_Challenges/sample.txt")
