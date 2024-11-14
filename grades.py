grades = []
passed_students = []

while True:
        grade = input("Please enter your grade (type done if you're finish): ")

        if grade.lower() == 'done':
           break
        if not grade.isdigit():
            print("Error: Please enter a numeric grade.")
        else:
            grade = int(grade)
            if grade <=39:
                print("Incorrect")
                continue
            elif grade >=101:
                print("Incorrect")
                continue
            grades.append(grade)
            if grade >=75:
                passed_students.append(grade)
if grades:
        average = sum(grades) / len(grades)
        passing_percentage = (len(passed_students) / len(grades)) * 100
        print(f"The average grade is: {average: .2f}")
        print(f"The passing percentage is: {passing_percentage:.2f}%")
        print(f"Number of students who passed:{len(passed_students)}")
        print(f"Grades: {passed_students}")

else:
    print("No grade were entered.")
