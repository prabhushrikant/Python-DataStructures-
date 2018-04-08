# https://www.geeksforgeeks.org/print-nodes-distance-k-leaf-node/
import BinaryTree as b_tree

visited = set()

def printall(root, path, level, k):

    if root is None:
        return

    if root.left == None and root.right == None:
        if level-k >=0 and path[level-k] not in visited:
            print str(path[level-k].data) + " ",
            visited.add(path[level-k])
        elif level-k < 0:
            return

    else:
        path.append(root)
        printall(root.left, list(path), level+1, k)
        printall(root.right, list(path), level+1, k)
        # Note following lines will give wrong answer since , same list object get transferred
        # to successive recursive calls, instead what we need is to send new list of path for
        # every recursive call, i.e. pass by value. Since by default lists are mutable in python
        # they are passed by reference and can be modified in function, in order to achieve effect
        # of passed by value , we pass new instance of the list to every call.

        # printall(root.left, path, level+1, k)
        # printall(root.right, path, level+1, k)

if __name__ == "__main__":

    # example 1

    tree = b_tree.BinaryTree(1)
    root = tree.root
    root.left = b_tree.Node(2)
    root.right = b_tree.Node(3)
    root.left.left = b_tree.Node(4)
    root.left.right = b_tree.Node(5)
    root.right.left = b_tree.Node(6)
    root.right.right = b_tree.Node(7)
    root.right.left.right = b_tree.Node(8)

    print "Nodes are : "
    printall(root,[],0,2)