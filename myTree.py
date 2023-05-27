#
class Node:
    
    #
    def __init__(self,data):
        self.data  = data
        self.left  = None
        self.right = None
    
    #
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    #
    def search(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.left is None:
                return False
            else:
                return self.left.search(data)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(data)

    #
    def inorder_traversal(self):
        result = []
        if self.left:
            result += self.left.inorder_traversal()
        result.append(self.data)
        if self.right:
            result += self.right.inorder_traversal()
        return result

    def print_tree(self):
        self._print_tree_helper(self, 0)

    def _print_tree_helper(self, node, level):
        if node is not None:
            self._print_tree_helper(node.right, level + 1)
            print("    " * level + str(node.data))
            self._print_tree_helper(node.left, level + 1)


#
def main():
    #
    root = Node(5)

    #
    root.insert(3)
    root.insert(7)
    root.insert(2)
    root.insert(4)
    root.insert(6)
    root.insert(8)

    #
    print(root.search(4))
    print(root.search(9))

    #
    print(root.inorder_traversal())

    #
    root.print_tree()

#
if __name__ == "__main__":
    main()
            
