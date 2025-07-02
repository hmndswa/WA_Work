num = int(input("Enter a number to view mulitplication table: "))

for i in range(1, 13):
    result = num * i
    print(f"{num} x {i} = {result}")
    