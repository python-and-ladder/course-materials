students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Sort by grade
sorted_by_grade = sorted(students, key=lambda student: student['grade'])
print([s['name'] for s in sorted_by_grade])  # ['Charlie', 'Alice', 'Bob']

# Sort by name length
sorted_by_name_length = sorted(students, key=lambda student: len(student['name']))
print([s['name'] for s in sorted_by_name_length])  # ['Bob', 'Alice', 'Charlie']
