class Student(object):

    __doc__ = "student"
    count = 0
    books = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass


Student.books.extend(["python", "JS"])
print(Student.books[0])
HB = Student("1", "2")
print("student name=:%s" % HB.name)
