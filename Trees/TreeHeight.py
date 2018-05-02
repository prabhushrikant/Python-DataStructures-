from collections import deque
import BinaryTree as b_tree

def getHeight_DFS(root, level):
    if root is None:
        return level-1
    else:
        return max(getHeight_DFS(root.left, level+1), getHeight_DFS(root.right, level+1))

def getHeight_BFS(root):

    q = deque([])
    if root is None:
        return 0

    q.append(root)
    level = 1
    q.append('|')
    while len(q) > 0:
        p = q.popleft()
        if p is not '|':
            # print str(p.data) + " ",
            if p.left is not None:
                q.append(p.left)
            if p.right is not None:
                q.append(p.right)
        elif len(q) > 0:
            level += 1
            q.append('|') #adding a delimiter to mark level complete, in the queue at end of each level
            # print


    return level

if __name__ == "__main__":

    # example 1

    tree = b_tree.BinaryTree(10)
    root = tree.root
    root.left = b_tree.Node(12)
    root.right = b_tree.Node(15)
    root.left.left = b_tree.Node(25)
    root.left.right = b_tree.Node(30)
    root.right.left = b_tree.Node(36)


    print "tree height using DFS : " + str(getHeight_DFS(root, 0) + 1)
    print "tree height using BFS : " + str(getHeight_BFS(root))

    print "BFS on tree to print nodes for each level on separate line"
    getHeight_BFS(root)