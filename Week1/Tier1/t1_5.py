def convert(t_seconds):
    seconds = t_seconds % (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60

    return f"{hours:02d}:{mins:02d}:{seconds:02d}"


user_input = int(input("Enter seconds: "))
print(convert(user_input))


