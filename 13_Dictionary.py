student = {
    "name": "Harry",
    "city":"Delhi",
    "company":"Meta"
}

print(student["company"])
# print(student["nameee"])# error

print(student.get("nameeee"))# it can print Nan

print(student.get("name"))


# update

student["city"] = "ghaziabad"

# print(student)