def find_max(list):
  max = list[0]
  for number in list:
    if (number > max):
      max = number 

  return max

list = [3,7,12,8,4,9]
max = find_max(list)

print("Max:", max)
