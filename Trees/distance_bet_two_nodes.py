import BinaryTree as b_tree

# method 1 > using same logic as find all nodes at distance k problem but not successful.
# Returns level of target(t) if it is present in
# tree rooted at (root), otherwise returns -1
def get_distance_below(root, t, level):
    if root is None:
        return -1
    if root == t:
        return level

    left = get_distance_below(root.left, t, level+1)
    if left == -1:
        return get_distance_below(root.right, t, level+1)
    return left

def get_distance(root, a, b):
    if root is None:
        return -1
    else:
        if root == a or root == b:
            if root == a:
                d = get_distance_below(a, b, 0)
                return d if d != -1 else 0
            elif root == b:
                d = get_distance_below(b, a, 0)
                return d if d != -1 else 0
        else:
            dl = get_distance(root.left, a, b)
            if dl > 0:
                return dl
            elif dl == 0:
                return 1 + dl, False

            dr = get_distance(root.right, a, b)
            if dr > 0:
                return dl
            elif dl == 0:
                return 1 + get_distance(root.left, a, b)

            return -1

#method 2 (using LCA)
def covers(root, t):
    if root is None:
        return False
    else:
        if root == t:
            return True
        else:
            return covers(root.left, t) or covers(root.right, t)

def get_LCA(root, a , b):

    if root is None:
        return None
    elif root == a:
        return a
    elif root == b:
        return b
    else:
        a_on_left = covers(root.left, a)
        b_on_left = covers(root.left, b)

        if a_on_left != b_on_left:
            return root
        else:
            if a_on_left:  #means b_on_left is also True.
                return get_LCA(root.left, a, b)
            else:
                return get_LCA(root.right, a, b)

def get_distance_from(root, t, level):
    if root is None:
            return -1
    if root == t:
        return level

    left = get_distance_from(root.left, t, level+1)
    if left == -1:
        return get_distance_from(root.right, t, level+1)
    return left

def get_distance_using_LCA(root, a, b):

    if root is None:
        return 0

    if a is None or b is None:
        return 0

    LCA = get_LCA(root, a, b)

    d1 = get_distance_from(LCA, a, 0) #it's not possible to have -1 here since root is LCA of a

    d2 = get_distance_from(LCA, b, 0) #it's not possible to have -1 here since root is LCA of b

    return d1 + d2;

if __name__ == "__main__":

    # example 1

    tree = b_tree.BinaryTree(20)
    root = tree.root
    root.left = b_tree.Node(8)
    root.right = b_tree.Node(22)
    root.left.left = b_tree.Node(4)
    root.left.right = b_tree.Node(12)
    root.left.right.left = b_tree.Node(10)
    root.left.right.right = b_tree.Node(14)

    print "distance between target nodes in example 1: "
    t1 = root.left.right #target node 1
    t2 = root.right #target node 2
    print get_distance_using_LCA(root, t1, t2)
    print

    print "distance between target nodes in example 1: "
    t1 = root.left #target node 1
    t2 = root.left.left #target node 2
    print get_distance_using_LCA(root, t1, t2)
    print