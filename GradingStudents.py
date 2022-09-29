def gradingStudents(grades):
    finalGrades = []
    for grade in grades:
        if grade < 38 or grade%5<3:
            finalGrades.append(grade)
        else:
            finalGrades.append(grade + (5 - grade%5))
    return finalGrades
