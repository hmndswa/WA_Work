list1 = [2, 3, 5, 9, 7]
list2 = [1, 12, 7, 10, 4, 5]

set1 = set(list1)
set2 = set(list2)

common_elements = set1 & set2

elements_list = list(common_elements)

print("Common Elements: ", elements_list)
