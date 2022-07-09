class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def detail(self):
        print("My name is " + self.firstname, self.lastname)


intro = Person("Ashish", "Lal")
intro.detail()


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("My name and year is " + self.firstname, self.lastname, self.graduationyear)


p1 = Student("Saumya", "Pallavi", 2010)
p1.welcome()
