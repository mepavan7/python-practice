
students = []
for _ in range(int(input("Enter the name:"))):
    name = input()
    score = float(input())
    students.append([name, score])
all_score = [student[1] for student in students]
unique_grade = sorted(list(set(all_score)))
second_lowest_grade = unique_grade[1]
result_name = []
for name , grade in students:
    if grade == second_lowest_grade:
        result_name.append(name)
result_name.sort()
for name in result_name:
    print(f"output:{name}")    
