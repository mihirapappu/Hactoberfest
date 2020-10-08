class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def size(self):
        return(len(self.items))
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            print("stack is empty")
        return self.items[-1]
    def display(self):
        print(self.items)

if __name__ == "__main__":
    st=stack()
    while True:
        print("1.push")
        print("2.pop")
        print("3.peek")
        print("4.size")
        print("5.display")
        print("6.quit")
        choice=int(input("enter your choice"))
        if choice==1:
            x= int(input("enter the element to be inserted"))
            st.push(x)
        elif choice==2:
            x=st.pop()
        elif choice==3:
            print(st.peek())
        elif choice==4:
            print(st.size())
        elif choice==5:
            st.display()
        elif choice==6:
            break
        else:
            print("wrong choice")
        print()

