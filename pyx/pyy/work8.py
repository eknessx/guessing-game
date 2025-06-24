class Hello:
    def __init__(self,name="",age="",hello=""):
        self.name=name
        self.hello=hello
        self.age=age

    def show(self):
        self.name = input("enter your name :    ")
        self.age = int(input("enter your age :" ))
        self.hello = input("say hi! :   ")
        print(self)
    def __str__(self):
        return f"your name is : {self.name} is {self.age} and {self.hello}"



enter=Hello()
enter.show()
