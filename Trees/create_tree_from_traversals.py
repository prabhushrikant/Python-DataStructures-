import BinaryTree as b_tree

def partition_inorder(inorder, partitionValue):
    partitionIndex = 0
    for nodeVal in inorder:
        # partitioning at first node which matches partitionValue in input sequence
        if(nodeVal == partitionValue):
            break
        else:
            partitionIndex += 1

    if(partitionIndex >= 0):
        left = inorder[0:partitionIndex]
    else:
        left = None

    if partitionIndex+1 <= len(inorder)-1:
        right = inorder[partitionIndex+1:]
    else:
        right = None

    return left, right

def partition_bfs(left_inorder, right_inorder, bfs):
    left_bfs = []
    right_bfs = []

    if left_inorder and bfs:
        for e in bfs:
            for e1 in left_inorder:
                if e == e1:
                    left_bfs.append(e) # order they appear in bfs sequence is retained.

    if right_inorder and bfs:
        for e in bfs:
            for e1 in right_inorder:
                if e == e1:
                    right_bfs.append(e) # order they appear in bfs sequence is retained.

    return left_bfs, right_bfs

def create_tree_from_inorder_preorder(inorder, preorder):
    global idx   #remember whenever we use a global index in recursion, there is simpler iterative approach possible
    if idx >= len(preorder):
        return None
    else:
        root = b_tree.Node(preorder[idx])

        # print "root: " + str(root.data)
        #find root in inorder (partition inorder around root)
        left, right = partition_inorder(inorder,root.data)
        # print "left: ",
        # print left

        # print "right: ",
        # print right

        if left:
            idx += 1
            root.left = create_tree_from_inorder_preorder(left,preorder)
        else:
            root.left = None

        if right:
            idx += 1
            root.right = create_tree_from_inorder_preorder(right,preorder)
        else:
            root.right = None

        return root

def create_tree_from_inorder_postorder(inorder, postorder):
    global idx
    if idx < 0:
        return None
    else:
        root = b_tree.Node(preorder[idx])

        # print "root: " + str(root.data)
        #find root in inorder (partition inorder around root)
        left, right = partition_inorder(inorder,root.data)
        # print "left: ",
        # print left

        # print "right: ",
        # print right

        #Note the order is changed , we first process right tree, then left tree in case of processing postorder
        if right:
            idx -= 1
            root.right = create_tree_from_inorder_postorder(right,postorder)
        else:
            root.right = None

        if left:
            idx -= 1
            root.left = create_tree_from_inorder_postorder(left,postorder)
        else:
            root.left = None

        return root

def partition_postorder_BST(postorder, partitionValue):
    #because we know that tree is BST, let's partition all the nodes lesser than
    #partition value to be left of the tree, and higher as right of the tree.
    left = []
    right = []
    partitionIndex = 0
    for nodeVal in postorder:
        # in-case of postorder this will be the last node in postorder, all other nodes would come before it
        if(nodeVal == partitionValue):
            break
        else:
            if nodeVal <= partitionValue:
                left.append(nodeVal)
            else:
                right.append(nodeVal)
            partitionIndex += 1

    return left, right

def partition_postorder_full_tree(postorder, partitionValue, rootData):

    #because we know that tree is full tree,
    partitionIndex = 0
    found = False
    for nodeValue in postorder:
        if nodeValue == partitionValue:
            found = True
            break
        else:
            partitionIndex += 1

    # print "partitionIndex : " + str(partitionIndex)
    if found:
        left = postorder[0:partitionIndex+1]
        i = partitionIndex+1
        while i < len(postorder) and postorder[i] != rootData:
            i += 1

        right = postorder[partitionIndex+1:i]
    else:
        left = []
        right = []

    return left, right

#Note: it's not possible to create unique tree from preorder and postorder,
#Tree needs to have some other property such as Tree is either Full Binary Tree, or it's BST
def create_BST_from_preorder_postorder(postorder, preorder):
    global idx
    if idx >= len(preorder):
        return None
    else:
        root = b_tree.Node(preorder[idx])

        # print "root: " + str(root.data)
        #find root in inorder (partition inorder around root)
        left, right = partition_postorder_BST(postorder,root.data)
        # print "left: ",
        # print left
        #
        # print "right: ",
        # print right

        if left:
            idx += 1
            root.left = create_BST_from_preorder_postorder(left,preorder)
        else:
            root.left = None

        if right:
            idx += 1
            root.right = create_BST_from_preorder_postorder(right,preorder)
        else:
            root.right = None

        return root

#Create full binary tree from preorder and postorder traversals.
#what is a full binary tree: - Free when each node has either 0 or 2 children.
def create_full_tree_from_preorder_postorder(postorder, preorder):
    global idx
    if idx >= len(preorder):
        return None
    else:
        root = b_tree.Node(preorder[idx])
        print "root: " + str(root.data)

        left = []
        right = []
        if len(preorder[idx:]) >= 2:
            #this means there exists, next node to current root in preorder
            #since tree is full, this next node is left child of root.

            left, right = partition_postorder_full_tree(postorder, preorder[idx+1], root.data)

        print "left: ",
        print left

        print "right: ",
        print right

        if left:
            idx += 1
            root.left = create_full_tree_from_preorder_postorder(left,preorder)
        else:
            root.left = None

        if right:
            idx += 1
            root.right = create_full_tree_from_preorder_postorder(right,preorder)
        else:
            root.right = None

        return root


#it's possible to create a tree from inorder and bfs ,
#search for root
def create_tree_from_inorder_BFS(inorder, bfs):

    root = b_tree.Node(bfs[0])

    left, right = partition_inorder(inorder, root.data)

    #partition bfs is needed because using original bfs will contain
    #level order nodes from
    bfs_left, bfs_right = partition_bfs(left, right, bfs)

    if left:
        root.left = create_tree_from_inorder_BFS(left, bfs_left)
    else:
        root.left = None

    if right:
        root.right = create_tree_from_inorder_BFS(right, bfs_right)
    else:
        root.right = None

    return root

def inorder_traversal(root):
    if not root:
        return
    else:
        inorder_traversal(root.left)
        print root.data,
        inorder_traversal(root.right)

def preorder_traversal(root):
    if not root:
        return
    else:
        print root.data,
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if not root:
        return
    else:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print root.data,


#driver scripts
print "Building tree from inorder - preorder"
idx = 0
inorder = [10,30,40,50,60,70,80]
preorder = [50,30,10,40,70,60,80]
root = create_tree_from_inorder_preorder(inorder, preorder)
inorder_traversal(root)
print
preorder_traversal(root)
print

print "Building tree from inorder - postorder"
inorder = [10,30,40,50,60,70,80]
postorder = [10,40,30,60,80,70,50]
idx=len(postorder)-1
root = create_tree_from_inorder_postorder(inorder, postorder)

inorder_traversal(root)
print
preorder_traversal(root)
print
# print root.data

print "Building BST from preorder - postorder"
preorder = [50,30,10,40,70,60,80]
postorder = [10,40,30,60,80,70,50]
idx=0
root = create_BST_from_preorder_postorder(postorder,preorder)

inorder_traversal(root)
print
preorder_traversal(root)
print

print "Building BST from preorder - postorder"
preorder = [50,30,40,70,60]
postorder = [40,30,60,70,50]
idx=0
root = create_BST_from_preorder_postorder(postorder,preorder)

inorder_traversal(root)
print
preorder_traversal(root)
print

print "Building full tree from preorder - postorder"
preorder = [50,30,40,60,70]
postorder = [40,60,30,70,50]
idx=0
root = create_full_tree_from_preorder_postorder(postorder,preorder)

inorder_traversal(root)
print
preorder_traversal(root)
print

print "Building full tree from preorder - postorder"
preorder = [50,30,70,40,60]
postorder = [30,40,60,70,50]
idx=0
root = create_full_tree_from_preorder_postorder(postorder,preorder)

inorder_traversal(root)
print
preorder_traversal(root)
print

print "Building tree from inorder - BFS"
inorder = [4,8,10,12,14,20,22]
bfs = [20,8,22,4,12,10,14]
idx=0
root = create_tree_from_inorder_BFS(inorder,bfs)

inorder_traversal(root)
print
preorder_traversal(root)
print