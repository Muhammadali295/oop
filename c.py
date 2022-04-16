class student:
    def __init__(self,name="ali",Class=13,subject="oop"):
        self.name=name
        self.Class=Class
        self.subject=subject
        print(name, subject)

    def __int__(self,name,Class,subject):
        self.name=name
        self.Class=Class
        self.subject=subject
        print(name, subject, Class)

c=student("ali",13,'oop')


