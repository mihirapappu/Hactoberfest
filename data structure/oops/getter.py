class Employee:
    def __init__(self,name,password,salary):
        self._name=name
        self._password=password
        self._salary=salary
    @property         ### by only using property we can only read the name
    def name(self):
        return(self._name)
    @property
    def password(self):
        raise AttributeError("password not readable")
    @password.setter
    def password(self,new_pass):
        self._password=new_pass
    @property
    def salary(self):             
        return(self._salary)
    @salary.setter
    def salary(self,new_sal):
        self._salary=new_sal
p=Employee("rohan","23445r",456000)
print(p.name)
p.password="655rytfy"
