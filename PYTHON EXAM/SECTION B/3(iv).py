def grade_students(mark):
    try:
        mark = int(mark)
        if 90 <= mark <= 100:
           return 'A'
        elif 80 <= mark < 90:
           return 'B'
        elif 70 <= mark < 80:
           return 'C'
        elif 60 <= mark < 70:
           return 'D'
        elif 0 <= mark < 60:
           return 'F'
        else:
           return 'invalid'
    except ValueError:
        return 'Invalid Input'
    
grade = grade_students("invalid input")
print("Grade:", grade)  
    
