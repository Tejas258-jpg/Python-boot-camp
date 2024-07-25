class Employee:
    #static data
    company='Accenture'
    project='Digital image processing'
    def __init__(self,name,id,phoneno,salary):
        self.name=name
        self.id=id
        self.phoneno=phoneno
        self.salary=salary
    def display(self):
        print("name is:",self.name)
        print("id is:",self.id)
        print("phoneno is:",self.phoneno)
        print("salary is:",self.salary)
        print("company is:",Employee.company)
        print("project is:",Employee.project)
e1=Employee('tejasri','82','7569850159','17000')
e1.display()
