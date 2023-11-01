#Q2
class Person:
#{
  state = "NSW"
  def __init__(self, first_name, last_name, age, phone, email):
  #{
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.phone = phone
    self.email = email
  #}
  def __str__(self):
    return "{} {}: {} years old\nContact: {}, {}".format(self.first_name, self.last_name, self.age, self.phone, self.email)
  def __repr__(self):
    return "Person('{}', '{}', {}, '{}', '{}')".format(self.first_name, self.last_name, self.age, self.phone, self.email)
  @staticmethod
  def get_uni_website():
    return "www.uow.edu.au"
  @classmethod
  def get_state(cls):
    return  "State: " + cls.state
#}
# write your code to create objects:
personObj1 =  Person('John', 'Lee', '19', '0400000000', 'jl123@gmail.com')
personObj2 =  Person('Mary', 'Zheng', '25', '0242239999', 'maryz@gmail.com')
personObj3 =  Person('Cindy', 'Wilson', '53', '0430982200', 'cw456@hotmail.com')

# write your code to display the string of each person object
print("{} {}: {} years old\nContact: {}, {}".format(personObj1.first_name, personObj1.last_name, personObj1.age, personObj1.phone, personObj1.email))
print("{} {}: {} years old\nContact: {}, {}".format(personObj2.first_name, personObj2.last_name, personObj2.age, personObj2.phone, personObj2.email))
print("{} {}: {} years old\nContact: {}, {}".format(personObj3.first_name, personObj3.last_name, personObj3.age, personObj3.phone, personObj3.email))
# write your code to display the code of building each person object
print(repr(personObj1))
print(repr(personObj2))
print(repr(personObj3))

# write your code to display the university's website using the static method

print(Person.get_uni_website())

# write your code to display the state using the class method
print(Person.get_state())
