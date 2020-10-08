class Product:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @property          #by using @property function u can call the function as a instance variables
    def display(self):
        return(self.x)
p1=Product(20,30)
print(p1.display)
print(p1.display+2)