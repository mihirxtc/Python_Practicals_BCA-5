# newstudent.py

from student import student

s = student()
s.setid(100)
s.setname("James Bond")
s.setaddress("Eve Street, Newyork, USA")
s.setmarks(79)

print("Student ID = ", s.getid())
print("Student Name = ", s.getname())
print("Student Address = ", s.getaddress())
print("Student Marks = ", s.getmarks())