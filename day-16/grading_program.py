def get_score(student_score: int) -> str:
    if 91 <= student_score <= 100:
        return "Outstanding"
    elif 81 <= student_score <= 90:
        return "Exceeds Expectations"
    elif 71 <= student_score <= 80:
        return "Acceptable"
    elif student_score <= 70:
        return "Fail"

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student_name, student_score in student_scores.items():
    student_grades[student_name] = get_score(student_score)

print(student_grades)

