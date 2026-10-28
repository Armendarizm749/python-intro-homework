student = {
    "name": "Mariana",
    "grade": "A",
    "subjects": ["Python", "Statistics", "Data Visualization"]
}

for key, value in student.items():
    print(key, value)


student["graduated"] = False
print("Updated student:", student)