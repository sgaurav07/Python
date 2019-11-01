class Person:
    pname = ""
    page = 0
    def __init__(self, person_name, person_age):
        self.pname = person_name
        self.page = person_age
    def printName(self):
        print(self.pname)
    def printAge(self):
        print(self.page)

class std(Person):
    def __init__(self,name,age):
        super().__init__(self,name,age)




p1 = Person("Jane",22)
p1.printName()
p1.printAge()
std1 = std("SG",26)

std1.printAge()
std1.printName()