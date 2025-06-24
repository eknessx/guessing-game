class User:
    def __init__(self,name="",age="",programming_language=""):
        self.name = name
        self.age = age
        self.programming_language = programming_language
    def show(self):
        self.name = input("enter your name :")
        self.age = int(input("enter your age :"))
        self.programming_language = input("enter your programming language :")
        print(self)
    def __str__(self):
        return f"his name is :{self.name} is {self.age} years old and knows :{self.programming_language}"
    
user1 = User()
user1.show()
