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
        if(self.head):
            current = self.head
            while(current):
                print(current.data)
                current = current.next
        else:
            print("List is empty")
    def delete_last_node(self):
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = None
        
        
list1 = LinkedList()
list1.append_node(1)
list1.append_node(3)
list1.append_node(4)
list1.append_node(5)
list1.PrintList()





