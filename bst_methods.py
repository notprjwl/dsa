class node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class binary_search_tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)  #private insert function    #._ is understood as private functions. python does not has private function but using "._" is understood as pvt functions     
    def _insert(self, value, curr_node):
        if value < curr_node.value:
            if curr_node.left == None:
                curr_node.left = node(value)
            else:
                self._insert(value, curr_node.left)

        elif value > curr_node.value:
            if curr_node.right == None:
                curr_node.right = node(value)
            else:
                self._insert(value, curr_node.right)
        
        else:
            print ("the value already in the tree")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, curr_node):
        if curr_node != None:
            self._print_tree(curr_node.left)
            print(str(curr_node.value))
            self._print_tree(curr_node.right)
 
    
def fill_tree(tree, elem = 100, max_int = 1000):
    from random import randint
    for _ in range(elem):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree



tree = binary_search_tree()

tree = fill_tree(tree)

            
tree.print_tree()