class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = node()

    #creates a new node
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
    
    #returns the length of the nodes
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total

    #displays the linked list in the list format
    def display(self):
        elem = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elem.append(cur_node.data)
        print(elem)
    
    #returns the element to the given index
    def get(self, index):
        if index < 0 or index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None

        cur_idx = 0
        cur_node = self.head.next
        while cur_node:
            if cur_idx == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_idx += 1

    #deletes the node at a given index 
    def erase(self, index):
        if index >= self.length() or index < 0:
            print("index out of range")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            lastnode = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                lastnode.next = cur_node.next
                return
            cur_idx+=1



mylist = linkedlist()

mylist.append(2)
mylist.append(4)
mylist.append(8)
mylist.append(10)

mylist.length()
mylist.erase(1)
mylist.display()

print("the element in the 2nd index is: %d" % mylist.get(2))
