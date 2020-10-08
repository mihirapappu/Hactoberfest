class Person:
    def greet(self):
        print("Iam a person")
class teacher(Person):
    def greet(self):
        super().greet()
        print("I am a teacher")
class student(Person):
    def greet(self):
        super().greet()
        print("I am a student")
class teaching_ass(student,teacher):
    def greet(self):
        super().greet()
        print("I am a  teaching assistant")
x=teaching_ass()
x.greet()
help(teaching_ass)