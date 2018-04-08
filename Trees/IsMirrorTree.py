import BinaryTree as b_tree

def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        return root1.data == root2.data and \
               isMirror(root1.left, root2.right) and \
               isMirror(root1.right, root2.left)

    return False

if __name__ == "__main__":

    # example 1

    tree = b_tree.BinaryTree(2)
    root = tree.root
    root.left = b_tree.Node(2)
    root.right = b_tree.Node(2)
    root.left.left = b_tree.Node(3)
    root.left.right = b_tree.Node(4)
    root.right.left = b_tree.Node(4)
    root.right.right = b_tree.Node(3)

    print "Tree is a mirror : " + str(isMirror(root,root))

    # example 2

    tree = b_tree.BinaryTree(1)
    root = tree.root
    root.left = b_tree.Node(2)
    root.right = b_tree.Node(2)
    # root.left.left = b_tree.Node(3)
    root.left.right = b_tree.Node(3)
    # root.right.left = b_tree.Node(4)
    root.right.right = b_tree.Node(3)

    print "Tree is a mirror : " + str(isMirror(root,root))