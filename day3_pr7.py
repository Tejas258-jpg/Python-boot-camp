class Employee:
    def __init__(self,name,rollno,salary):
        self.name="you"
        self.role="CEO"
        self.__salary="12.5cr"  #private
    def get__salary(self):  #public
        return self.__salary
    def Empdisplay(self):
        print(self.name,self.role)  #public
class company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self):  #protected
            print("hiring for the manager role")
comobj=company('BGTS','Banjara hills')
empobj=Employee('you','CEO','12.5cr')
empobj.Empdisplay()
comobj.comdisplay()
print(comobj._hiring())  