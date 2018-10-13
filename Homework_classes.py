
class Person:

    def __init__(self, name, last_name, age, gender, student):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student

    def Greeting(self):
        return ("Welcome dear ", self.name)

    def Goodbye(self):
        return ('Bye everyone!')

    def Favourite_num(self):

Person_1 = Person('Narek', 'yeranosyan', '31', 'man', False)
second_person = Person('Shahane', 'Arushanyan', '23', 'woman', False)

print(Person_1.Greeting())
print(Person_1.Greeting())






