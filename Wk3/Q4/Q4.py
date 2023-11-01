#Q4
class Employee:
  employee_dir = "/intranet"

  def __init__(self, employee_id, first_name, last_name, position, phone):
    self.employee_id = employee_id
    self.first_name = first_name
    self.last_name = last_name
    self.position = position
    self.phone = phone

  def home_dir(self):
    return Employee.employee_dir + "/" + self.employee_id


class Casual(Employee):
  employee_dir = "/intranet/casual"

  def __init__(self, employee_id, first_name, last_name, position, phone, type):
    super().__init__(employee_id, first_name, last_name, position, phone)

  def home_dir(self):
    return Casual.employee_dir + "/" + self.employee_id

  def print_detail(self):
    print("Employee id: " + self.employee_id)
    print("Name: " + self.first_name + " " + self.last_name)
    print("Position: " + self.position)
    print("Phone number: " + self.phone)
    print("Home directory: " + self.home_dir())


casualObj1 = Casual("1234567", "John", "Smith", "Manager", "0420400000", "Casual")
casualObj1.print_detail()
