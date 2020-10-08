#from stack import Stack
class stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[0]
    def is_empty(self):
            return self.items==[]
    def get_items(self):
        return self.items
    def div_by_2(num):
        s=Stack()
        while num>0:
            rem=num%2
            s.push(rem)
            num=num//2
        bin_num=""
       while not s.is_empty():
           bin_num+=str(s.pop())
       return bin_num
print(div_by_2(242))    
