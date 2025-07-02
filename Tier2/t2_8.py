word = str(input("Enter a word to count the number of vowels: "))
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

count = 0
for x in word:
    if x in vowels:
        count += 1


print(f"Number of vowels: {count}")