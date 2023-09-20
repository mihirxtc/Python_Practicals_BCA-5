# 13. Create a program name "employee.py" and implement the function DA, HRA, PF and ITAX. Create another program that uses the function of employee moduleand calculates gross and net salaries of an employee.

import employee
print("SALARY PROGRAM")

name = str(input("Enter name of employee: "))
basic = float(input("Enter Basic Salary: "))
netpay = employee.netPay(basic)
print(f"Net Salary: {netpay}")
grospay = employee.grossPay(basic, netpay)
print(f"gross Salary: {grospay}")