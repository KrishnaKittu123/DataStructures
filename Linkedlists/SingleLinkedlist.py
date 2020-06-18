class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
node1 = Node(1)

class LinkedList:
    def __init__(self):
        self.head = None
    def append_node(self,data):
        new_node = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    def PrintList(self):
        current = self.head
        while(current.next):
            print(current.data)
            current = current.next
        
list1 = LinkedList()
list1.head = node1
list1.append_node(3)
list1.append_node(4)

list1.PrintList()

