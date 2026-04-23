# wrapping up of data and function line a single entity
# restrict access to methods and variables from outside
# prevent data accidental or unauthorized modification
# provide security by hiding data from outside world

class Person:
    def __init__(self, name, age):
        self.name=name
        self.__age= age

p1=Person("Emil", 25)
print(p1.name)
print(p1._Person__age)
