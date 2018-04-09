# Programmer
class Person(object):
    def __init__(self, name, education):
        self.name = name
        self.education = education

    def work(self):
        print("%s goes to work" % self.name)


test_person = Person('Generic name', 'bachelors degree')
test_person.work()


class Employee(Person):
    def __init__(self, name, education, age):
        super(Employee, self).__init__(name, education)
        self.age = age
        self.living = True

    def dying(self):
        print("%s died lmao" % self.name)
        self.living = False


class Programmer(Employee):
    def __init__(self, name, education, age, salary):
        super(Programmer, self).__init__(name, education, age)
        self.salary = salary

    def gain_salary(self):
        print("%s  dollars gained" % self.salary)


test_employee = Employee('Generic name', 'bachelors degree', 'currently alive',)
test_employee.dying()
test_programmer = Programmer("jew", "Masters degree", "34 years old", 400000000000000000)
test_programmer.gain_salary()
