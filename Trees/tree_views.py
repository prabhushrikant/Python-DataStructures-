import BinaryTree as b_tree


def left_view(root, s, level):
    if root is None:
        return
    else:
        if level not in s:
            s.add(level)
            print str(root.data) + " ",

        left_view(root.left, s, level + 1)
        left_view(root.right, s, level + 1)


def right_view(root, s, level):
    if root is None:
        return
    else:
        if level not in s:
            s.add(level)
            print str(root.data) + " ",

        right_view(root.right, s, level + 1)
        right_view(root.left, s, level + 1)

def isLeaf(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True
    else:
        return False

def bottom_view(root, s, level):
    if root is None:
        return
    else:
        bottom_view(root.left, s, level - 1)
        #isLeaf is needed because we need to print the nodes as they appear from left to right
        #if we remove this condition bottom order will : 5,10,14,3,25 but that changes order of 3 and 14 as they appear in
        #tree, because in tree 3 appears before 14 from left, we want to print nodes from left to right
        #hence correct output is : 5,10,3,14,25

        if isLeaf(root.left) and isLeaf(root.right):
            if level not in s:
                s.add(level)
                print str(root.data) + " ",
        bottom_view(root.right, s, level + 1)

def vertical_view(root, s, level, levelMap):
    if root is None:
        return levelMap;
    else:
        vertical_view(root.left, s, level - 1, levelMap)
        if level in levelMap:
            nodeList = levelMap[level]
            nodeList.append(root)
        else:
            levelMap[level] = [root]
        # print str(root.data) + " ",
        vertical_view(root.right, s, level + 1, levelMap)
        return levelMap

if __name__ == "__main__":
    # tree = b_tree.BinaryTree(1)
    # root = tree.root
    # root.left = b_tree.Node(2)
    # root.right = b_tree.Node(3)
    # root.left.left = b_tree.Node(4)
    # root.left.right = b_tree.Node(5)
    # root.right.left = b_tree.Node(6)
    # root.right.right = b_tree.Node(7)
    # root.left.left.right = b_tree.Node(8)
    # root.left.right.right = b_tree.Node(9)
    # root.left.right.right.right = b_tree.Node(10)

    tree = b_tree.BinaryTree(20)
    root = tree.root
    root.left = b_tree.Node(8)
    root.right = b_tree.Node(22)
    root.left.left = b_tree.Node(5)
    root.left.right = b_tree.Node(3)
    root.right.left = b_tree.Node(4)
    root.right.right = b_tree.Node(25)
    # root.left.left.right = b_tree.Node(8)
    root.left.right.left = b_tree.Node(10)
    root.left.right.right = b_tree.Node(14)

    print "Left View of Tree : ",
    left_view(root, set(), 0)
    print
    print "Right View of Tree : ",
    right_view(root, set(), 0)
    print
    print "Bottom View of Tree : ",
    bottom_view(root, set(), 0)
    print
    print "Vertical View of Tree : ",
    levelMap = vertical_view(root, set(), 0, {})
    for level in sorted(levelMap):
        print "$",
        for node in levelMap[level]:
            print str(node.data) + " ",
    print