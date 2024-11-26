# import ast
# class_list = input("Please provide a list of students names, ages, and grades, like so: [name1, age1, grade1], [name2, age2, grade2].: ")

# try:
#     parsed_list = ast.literal_eval(f"[{class_list}]")
    
#     class_dict = {}
#     for index, element in enumerate(class_list):
#         class_dict[index] = element
#     print(class_dict)

# except (SyntaxError, ValueError) as e:
#     print(f"Invalid input: {e}")


# # list
# Name = ["Triston", "Terry", "Jordan"]
# Age = [20, 40, 60]
# Grade = ["A", "B", "C"]

# Group = {
#     "name": Name,
#     "age": Age,
#     "grade": Grade,
# }

# length=len(Group)


# for i in range(length):
#     student_info = ""
#     for key, value in Group.items():
#         student_info += f"{key.title()}: {value[i]}, "
#     print(student_info.strip(", "))

from collections import defaultdict as dd

# List

Name = ["Triston", "Jordan", "Terry"]
Age = [20, 40, 60]
Grade = ["A", "B", "C"]

Students = dd(dict)

for i in range(len(Name)):
    Students[i]["Name"] = Name[i]
    Students[i]["Age"] = Age[i]
    Students[i]["Grade"] = Grade[i]

for student_id, info in Students.items():
    Student_info = ", ".join(f"{key}: {value}" for key, value in info.items())
    print(Student_info)







# Name = ["Triston", "Terry", "Jordan"]
# Age = [20, 40, 60]
# Grade = ["A", "B", "C"]

# Students = dd(dict)

# for i in range(len(Name)):
#     Students[i]["Name"] = Name[i]
#     Students[i]["Age"] = Age[i]
#     Students[i]["Grade"] = Grade[i]

# for student_id, info in Students.items():
#     Student_ID = ", ".join(f"{key}: {value}" for key, value in info.items())
#     print(Student_ID)









# Name = ["Triston", "Jordan", "Terry"]
# Age = [20, 40, 60]
# Grade = ["A", "B", "C"]

# Students = dd(dict)

# for i in range(len(Name)):
#     Students[i]["Name"] = Name[i]
#     Students[i]["Age"] = Age[i]
#     Students[i]["Grade"] = Grade[i]

# for student_id, info in Students.items():
#     student_info= ", ".join(f"{key}: {value}" for key, value in info.items())
#     print(student_info)






# Name = ["Triston", "Jordan", "Terry"]
# Age = [20, 40, 60]
# Grade = ["A", "B", "C"]

# Students = dd(dict)

# for i in range(len(Name)):
#     Students[i]["Name"] = Name[i]
#     Students[i]["Age"] = Age[i]
#     Students[i]["Grade"] = Grade[i]

# for students_id, info in Students.items():
#    student_info = ", ".join(f"{key}: {value}" for key, value in info.items())
#    print(student_info)









# # list
# Name = ["Triston", "Terry", "Jordan"]
# Age = [20, 40, 60]
# Grade = ["A", "B", "C"]

# students = dd(dict)

# for i in range(len(Name)):
#     students[i]["Name"] = Name[i]
#     students[i]["Age"] = Age[i]
#     students[i]["Grade"] = Grade[i]

# for students_id, info in students.items():
#     student_info = ", ".join(f"{key}: {value}" for key, value in info.items() )
#     print(student_info)


# Group = {
#     "Name": Name,
#     "Age" : Age,
#     "Grade" : Grade,
# }

# Length = len(Group)

# for i in range(Length):
#     student_info = ""
#     for key, value in Group.items():
#         student_info += f"{key.title()} : {value[i]}, "
#     print(student_info.strip(", "))

