class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elem = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elem.append(cur_node.data)
        print(elem)

    def get(self, index):
        if index < 0 or index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None

        cur_idx = 0
        cur_node = self.head.next
        while cur_node is not None:
            if cur_idx == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_idx += 1

# Example usage:
mylist = linkedlist()

mylist.append(2)
mylist.append(4)
mylist.append(8)
mylist.append(10)

mylist.display()

print("the element in the 2nd index is: %d" % mylist.get(1))
