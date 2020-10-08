class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def inserthead(self,newnode):
        temporaray=self.head
        self.head=newnode
        self.head.next=temporaray
        del temporaray

    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            #head->john->rohan->none
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode
    def printlist(self):
        if self.head is None:
            print("list is empty")
            return
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next


firstnode=Node("john")
link=linklist()
link.insert(firstnode)
secondnode=Node("rohan")
link.insert(secondnode)
thirdnode=Node("komal")
link.inserthead(thirdnode)
link.printlist()
