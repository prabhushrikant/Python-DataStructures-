import BinaryTree

def InOrderTraversal(root):
    if root:
        InOrderTraversal(root.left)
        print root.data
        InOrderTraversal(root.right)