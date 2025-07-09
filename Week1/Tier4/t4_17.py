names_input = input("Enter names separated by commas: ")

names_list = []
for name in names_input.split(","):
    clean_name = name.strip().lower()
    names_list.append(clean_name)

unique_names = set(names_list)

sorted_names = sorted(unique_names)

print("Sorted unique names:", sorted_names)