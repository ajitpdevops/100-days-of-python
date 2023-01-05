student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62,
}

# Initialize an empty dictionary
student_grades = {}

# Derive the dictinary
# 91 -100 : outstanding
# 81-90: Exceeds Expectations
# 71-80: Acceptable 
# 70 and below : Fail

def get_grade(score):
    if score >= 91:
        return "Outstanding"
    elif score >= 81:
        return "Exceeds Expectations"
    elif score >= 71:
        return "Acceptable"
    elif score < 71:
        return "Fail"

# Add grades for each student 

for key in student_scores:
    grade = get_grade(student_scores[key])
    student_grades[key] = grade

print(student_scores)
print(student_grades)

