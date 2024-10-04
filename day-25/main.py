import random

names = ["Robert", "Alex", "Bob", "Charlie", "Angela", "Bob", "Charlie"]

student_scores = {student: random.randint(1, 100) for student in names}

passed_students = {student: score for (student, score) in student_scores.items() if score > 50}

print(passed_students)
