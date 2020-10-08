class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def length(self):#to return the length of the list
        currentnode=self.head
        len=0
        while currentnode is not None:
            len+=1
            currentnode=currentnode.next
        return len
    def inserthead(self,newnode):
        temporaray=self.head
        self.head=newnode
        self.head.next=temporaray
        del temporaray
    def insertat(self,newnode,position):#insert the node b/w two nodes
        if position is 0:#if u want to insert at pos 0
            self.inserthead(newnode)
            return

        currentnode=self.head
        currentpos=0
        while True:
            if currentpos==position:
                previousnode.next=newnode
                newnode.next=currentnode
                break

            previousnode=currentnode
            currentnode=currentnode.next
            currentpos+=1

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
link.insertat(thirdnode,1)
link.printlist()
print(link.length())
