num_of_students = int(input("Enter the number of students: "))
def students_grades_tracker(num):
    students_grade_dictionary = {}

    for i in range(1, num_of_students + 1):
        # name = input("Enter student name: ")
        students_grade_dictionary[f"stud{i}"] = {}
        name = input("Enter student name: ")
        students_grade_dictionary[f"stud{i}"]["name"] = name
        grades_list = []
        while True:
            grade = int(input(f"Enter grade for student {name}: "))
            if grade not in range(0, 100 + 1):
                print(f"{grade} is invalid. Please enter a valid grade between 0 and 100: ")
            else:
                grades_list.append(grade)

                if len(grades_list) == 3:
                    break
        students_grade_dictionary[f"stud{i}"]["grades"] = grades_list
        students_grade_dictionary[f"stud{i}"]["average"] = round((sum(grades_list) / len(grades_list)), 2)
    # return (students_grade_dictionary)
    for x, obj in students_grade_dictionary.items():
        for y in obj:
            # a = obj.keys(x)
            # b = obj.values(x)
            if y != "grades":
                print(f"{obj[y]}")

students_grades_tracker(num_of_students)





            # for key, value in students_dict.items():
            #     print(f"Average grade for {key}: {value:.2f}")
# print(students_grade_dictionary)