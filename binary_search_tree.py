class TreeNode:
    def __init__ (self, value):
        self.right = roght
        self.left = left
        self.value = value

    def insert(self, value):                  #Funstion for inserting a value to the binary tree  
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        
        if value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):  # Go as left as possible, print and then call the node to the right and try and go left as soon as possible before printing
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):               # Print the value of each node before moving down the tree
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):               #Go as deep as possible into the tree and then print the last node value
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)

        if value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)

        else:
            return True
