class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    # A utility function to do inorder traversal of BST
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def insert(self, node, key):

        if self.root == None:
            self.root = Node(key)
            return

        if node == None:
            return Node(key)

        if node.key >= key:
            node.left = self.insert(node.left, key)
        elif node.key < key:
            node.right = self.insert(node.right, key)

        return node

    def _get_min_node(self, node):
        if node.left == None:
            return node
        return self._get_min_node(node.left)

    def delete(self, node, key):

        if node is None:
            return None

        if node.key > key:
            node.left = self.delete(node.left, key)
        elif node.key < key:
            node.right = self.delete(node.right, key)
        else:
            succ = self._get_min_node(node.right)
            node.key = succ.key
            self.right = self.delete(node.right, succ.key)

            if self.root.key == key:
                self.root = succ

        return node


        # Driver program to test above functions
""" Let us create following BST 
			50 
		/	 \ 
		30	 70 
		/ \ / \ 
	20 40 60 80 """


tree = BST()

tree.insert(tree.root, 50)
tree.insert(tree.root, 30)
tree.insert(tree.root, 20)
tree.insert(tree.root, 40)
tree.insert(tree.root, 70)
tree.insert(tree.root, 60)
tree.insert(tree.root, 80)

print("Inorder traversal of the given tree")
tree.inorder(tree.root)

print("\nDelete 20")
tree.delete(tree.root, 20)
print("Inorder traversal of the modified tree")
tree.inorder(tree.root)

print("\nDelete 20")
tree.delete(tree.root, 30)
print("Inorder traversal of the modified tree")
tree.inorder(tree.root)

print("\nDelete 20")
tree.delete(tree.root, 40)
print("Inorder traversal of the modified tree")
tree.inorder(tree.root)

print("\nDelete 20")
tree.delete(tree.root, 50)
print("Inorder traversal of the modified tree")
tree.inorder(tree.root)
