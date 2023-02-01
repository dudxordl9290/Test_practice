
class Student():
    
    planet = 'Earth'  #CLASS OBJECT ATTRIBUTE (클래스 객체 속성)

    def __init__(self,name,gpa):  #ATTRIBUTE (그냥 속성 = name,gpa)

        self.name = name
        self.gpa = gpa

stu1 = Student(name="Jose",gpa=4.0)
stu2 = Student(name="Mimi",gpa=3.5)

print(stu1.planet)