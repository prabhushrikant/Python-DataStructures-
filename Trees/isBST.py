# https://github.com/mission-peace/interview/blob/master/src/com/interview/tree/IsBST.java

# https://youtu.be/MILxfAbIhrE

import BinaryTree as b_tree
import sys

def isBST(root, minn, maxx):
    if not root:
        return True

    if root.data <= minn or root.data > maxx:
        return False;

    return isBST(root.left, minn, root.data) and isBST(root.right, root.data, maxx)

#driver program
  #   20
  #   /  \
  #   10  30
  #  /  \
  # 5    25

tree = b_tree.BinaryTree(20)
root = tree.root
root.left = b_tree.Node(10)
root.right = b_tree.Node(30)
root.left.left = b_tree.Node(5)
root.left.right = b_tree.Node(25)

print isBST(root, sys.maxint*-1, sys.maxint)