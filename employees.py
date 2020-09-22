import csv

class Employee:
  def __init__(self, first_name, last_name, hourly_rate, hours_worked, amount_due):
    self.first_name = first_name
    self.last_name = last_name
    self.hourly_rate = float(hourly_rate)
    self.hours_worked = float(hours_worked)
    self.amount_due = float(amount_due)

  def values(self):
    return [self.first_name, self.last_name, self.hourly_rate, self.hours_worked, self.amount_due]

employees = []
count = 1

with open("employees.csv", "r") as employee_csv:
	reader = csv.reader(employee_csv, skipinitialspace=True)

	next(reader)
	for row in reader:
		count += 1
		current_employee = Employee(*row)
		employees.append(current_employee)

for employee in employees:
	print(f"{employee.first_name} makes {employee.hourly_rate} per hour. Sucker (apart from you Paula, well done!)")

# Add a new employee to the file

with open("employees.csv", "a") as employee_csv:
  writer = csv.writer(employee_csv, quoting=csv.QUOTE_ALL)
  new_employee = Employee("Jenny", "Jones", 12.5, 40, 0)
  writer.writerow(new_employee.values())

# Loop through the employees, calculate the amount_due column 
# (hourly_rate * hours_worked), and amend each row to add this 
# data in the amount_due column.

with open("employees.csv", "w") as employee_csv:
  writer = csv.writer(employee_csv, quoting=csv.QUOTE_ALL)
  writer.writerow(["first_name", "last_name", "hourly_rate", "hours_worked", "amount_due"])

  for employee in employees:
    employee.amount_due = employee.hourly_rate * employee.hours_worked
    writer.writerow(employee.values())

for employee in employees:
	print(f"{employee.first_name} is due £{employee.amount_due}")