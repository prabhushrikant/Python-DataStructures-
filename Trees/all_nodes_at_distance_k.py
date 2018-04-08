#find all nodes in a tree at distance k from given node with value n
#you can assume that there is only one node in tree with value n

import BinaryTree as b_tree

def nodes_at_dist_k_down(root, k):
    if root is None or k < 0:
        return

    if k == 0:
        print str(root.data) + " ",
        return

    nodes_at_dist_k_down(root.left, k-1)
    nodes_at_dist_k_down(root.right, k-1)


def nodes_at_dist_k(root, t, k):
    if root is None:
        return -1
    else:
        if root.data == t:
            nodes_at_dist_k_down(root, k)
            return 0
        else:
            # exploring left subtree of the root
            #returns the distance of target node from root if exists otherwise -1
            dl = nodes_at_dist_k(root.left, t, k)
            if dl != -1:
                if dl < k:
                    if dl + 1 == k:
                        print str(root.data) + " ",
                    else:
                        nodes_at_dist_k_down(root.right, k-dl-2)

                return 1 + dl

            # exploring right subtree of the root
            #returns the distance of target node from root if exists otherwise -1
            dr = nodes_at_dist_k(root.right,t,k)
            if dr != -1:
                if dr < k:
                    if dr + 1 == k:
                        print str(root.data) + " ",
                    else:
                        nodes_at_dist_k_down(root.left, k-dr-2)

                return 1 + dr

            #if n is not present in left or right subtree return -1
            return -1

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

    print "All nodes at distance k in example 1: "
    t = 8 #target node with data
    k = 2 #find all nodes from t which are at distance k
    nodes_at_dist_k(root, t, k)
    print

    # example 2

    tree = b_tree.BinaryTree(2)
    root = tree.root
    root.left = b_tree.Node(3)
    root.right = b_tree.Node(4)
    root.left.left = b_tree.Node(6)
    root.left.right = b_tree.Node(7)
    root.left.right.left = b_tree.Node(9)
    root.left.right.right = b_tree.Node(10)
    root.right.right = b_tree.Node(8)
    root.right.right.right = b_tree.Node(12)
    root.left.right.right.left = b_tree.Node(17)

    print "All nodes at distance k in example 2: "
    t = 7 #target node with data
    k = 8 #find all nodes from t which are at distance k
    nodes_at_dist_k(root, t, k)
    print

