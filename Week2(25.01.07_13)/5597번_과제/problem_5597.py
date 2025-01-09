students = set()

for _ in range(28):
    student = int(input())
    students.add(student)

all_students = set(range(1,31))

missing_students = sorted(all_students - students)

for student in missing_students:
    print(student)