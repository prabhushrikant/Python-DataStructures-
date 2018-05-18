# perform inorder traversal without recursion and stack

import BinaryTree as b_tree

def morris_traversal_inorder(root):
    curr = root
    while curr:
        if curr.left:
            temp = curr.left
            while temp.right and temp.right != curr:
                temp = temp.right

            if temp.right == curr:
                print str(curr.data) ,
                temp.right = None # destroying the back link
                curr = curr.right
            else:
                temp.right = curr #creating a back link
                curr = curr.left
        else:
            print str(curr.data) ,
            curr = curr.right

def morris_traversal_preorder(root):
    pass


#driver program.
tree = b_tree.BinaryTree(20)
root = tree.root
root.left = b_tree.Node(10)
root.right = b_tree.Node(30)
root.left.left = b_tree.Node(5)
root.left.right = b_tree.Node(15)
root.left.right.left = b_tree.Node(11)

print "regular: ",
tree.InorderTraversal(root,[],True)

print
print "morris:  ",
morris_traversal_inorder(root)


print
tree = b_tree.BinaryTree(1)
root = tree.root
root.left = b_tree.Node(2)
root.right = b_tree.Node(3)
root.left.left = b_tree.Node(4)
root.left.right = b_tree.Node(5)

print "regular: ",
tree.InorderTraversal(root,[],True)

print
print "morris:  ",
morris_traversal_inorder(root)
