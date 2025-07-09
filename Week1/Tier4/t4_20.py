students = {}

num_of_students = int(input("Enter number of students: "))

for i in range(num_of_students):
    name = input(f"Enter name for student {i+1}: ")
    mark = float(input(f"Enter mark for {name}: "))
    students[name] = mark

#print("Collected student data: ")
#print(students)

def get_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'F'

total_marks = sum(students.values())
average_mark = total_marks / num_of_students

#print(average_mark)

top_scorer = max(students, key=students.get)
top_score = students[top_scorer]

print("\n Student Grades:")
for name, mark in students.items():
    grade = get_grade(mark)
    print(f"{name}: {mark} marks - Grade {grade}")

print("\n Grade Summary:")
print(f"Class average: {average_mark:.2f}")
print(f"Top scorer: {top_scorer} with {top_score} marks")    