class Prodcut:
    def __init__(self,x,y):
        self._x=x
        self._y=y #underscore refers to the users that it is private but still u can access the value
    def display(self):
        print(self._x,self._y)
    @property
    def value(self):
        return(self._x)
    @value.setter  ## using setter  u can change the value of the instance variables
    def value(self,val):
        self._x=val
    @value.deleter
    def value(self):
        return self._x
p1=Prodcut(20,40)
p1.value
p1.display()
p1.value=50 ## changing the values of instance variables by using assign function
p1.display()
del p1.value
    