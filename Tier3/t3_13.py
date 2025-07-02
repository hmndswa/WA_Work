while True:
    try:
        user_input = input("Enter a number or 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Exiting program. Goodbye!")
            break

        num = int(user_input)
        initial = 1

        for i in range(1, num + 1):
            initial *= i

        print(f"Factorial is: {initial}")

    except ValueError:
        print("Invalid input! Please enter numbers only or 'q' to quit.")