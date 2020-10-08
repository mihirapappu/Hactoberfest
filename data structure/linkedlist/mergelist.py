from single_linklist import Node,linklist
def mergedlist(firstlist,secondlist,mergelist):
    #1->3->4||2->7->9
    currentfirst=firstlist.head
    currentsecond=secondlist.head
    while True:
        if currentfirst is None:
            mergelist.insert(currentsecond)
            break
        if currentfirst is None:
            mergelist.insert(currentfirst)
            break
        if currentfirst.data<currentsecond.data:
            currentfirstnext=currentfirst.next
            currentfirst.next=None
            mergelist.insert(currentfirst)
            currentfirst=currentfirstnext
        else:
            currentsecondnext=currentsecond.next
            currentsecond.next =None
            mergelist.insert(currentsecond)
            currentsecond=currentsecondnext

#first list
nodeone=Node(1)
nodetwo=Node(2)
nodethree=Node(6)
firstlist=linklist()
firstlist.insert(nodeone)
firstlist.insert(nodetwo)
firstlist.insert(nodethree)

#secondlist
nodefour=Node(3)
nodefive=Node(4)
nodesix=Node(7)
nodeseven=Node(9)
secondlist=linklist()
secondlist.insert(nodefour)
secondlist.insert(nodefive)
secondlist.insert(nodesix)
secondlist.insert(nodeseven)

print("print first list")
firstlist.printlist()
print("print second list")
secondlist.printlist()
mergelist=linklist()

mergedlist(firstlist,secondlist,mergelist)
del firstlist
del secondlist
print("print merge list")

mergelist.printlist()
