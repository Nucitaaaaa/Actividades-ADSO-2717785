
name = str(input("Enter your name: "))
salary = int(input("Enter your basic salary: "))
hours = float(input("Enter your hours worked: "))

salaryAmount = 1030000
subsidy = 70000

if salary > (salaryAmount * 2):
    salaryNew = salary + subsidy
    print(f"{name}, your salary will be of {salaryNew}, the subsidy transportation will be of {subsidy}, your basic salary was of {salary} ")
else:
    print(f"{name}, your salary will be of {salary}")

