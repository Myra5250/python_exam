def grade_students(mark):
    if 90 <= mark <= 100:
        return 'A', 'Excellent'
    elif 80 <= mark < 90:
        return 'B', 'Excellent'
    elif 70 <= mark < 80:
        return 'C', 'Good'
    elif 60 <= mark < 70:
        return 'D', 'Satisfactory'
    elif 0 <= mark < 60:
        return 'F', 'Needs Improvement'
    else:
        return 'Invalid'
grade, compliment = grade_students(78)
print(f"Grade: {grade}, Message: {compliment}")