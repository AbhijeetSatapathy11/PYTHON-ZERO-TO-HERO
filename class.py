class Person:
    name = ""
    age = 0
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)
class Student(Person):
    studentId = ""
    def __init__(self, studentName, studentAge, studentId):
        Person.__init__(self, studentName, studentAge)
        self.studentId = studentId
    def getId(self):
        return self.studentId
class Teacher(Student):
    salary = 0
    def __init__(self, teacherName, teacherAge, teacherId, salary):
        Student.__init__(self, teacherName, teacherAge,
                         teacherId)
        self.salary = salary
    def getSalary(self):
        return self.salary
print('This is Super Class Person')
person1 = Person("Abhijit Satpathy", 20)
print('Age of the Person :-')
person1.showAge()
print('Name of the Person :-')
person1.showName()
print('This is Child Class Student derived from Parent Class Person ')
student1 = Student("Ranjit", 20, "AB123")  # Line: 39
print('Student ID:-', student1.getId())
student1.getId()
print('Name of the Student:-')
student1.showName()
print('Age of the Student:-')
student1.showAge()
print('This is Child Class Teacher derived from Parent Class Student')
teacher1 = Teacher("Smita", 50, "Cse008", 600000)
print('Teacher ID:-', teacher1.getId())
print('Name of the Teacher')
teacher1.showName()
print('Age of the Teacher:-')
teacher1.showAge()
print('Salary of the Teacher:-', teacher1.getSalary())