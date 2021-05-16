
# Source: https://stackoverflow.com/questions/15081542/python-creating-objects

class Student(object):
    name = ""
    age = 0
    major = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

def make_student(name, age, major):
    student = Student(name, age, major)
    return student


s = Student('John', 88, None)

print(s.name, "is", s.age)


