class Student:
     def __init__(self,name,rollno,address,email,branch):
         self.name=name
         self.rollno=rollno
         self.address=address
         self.email=email
         self.branch=branch
     def display(self):
         print("name is:",self.name)
         print("roll no is:",self.rollno)
         print("address is:",self.address)
         print("email is:",self.email)
         print("branch is:",self.branch)
s1=Student('tejasri',82,'hyderabad','chindamtejasri@gmail.com','CSE')
s1.display()
