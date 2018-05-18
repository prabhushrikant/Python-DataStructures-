class Node:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, val=None):
        self.root = Node(val)

    def compare_presentations(self, pres1, pres2):
        if (len(pres1) == len(pres2)):
            index, sameCount, notSameCount = 0, 0, 0
            while(index < len(pres1)):
                if(pres1[index] == pres2[index]):
                    sameCount += 1
                else:
                    notSameCount += 1
                index += 1
            if (notSameCount == 0 and sameCount == len(pres1)):
                return True #same presentations
            else:
                return False #different presentations
        else:
            return False #different presentations
    #
    # def is_valid_presentation(presentationType):
    #     if(presentationType.lower() in ["inorder", "postorder", "preorder"]):
    #         return True
    #     else:
    #         return False
    #
    # def compare_presentations_types(pres1Type, pres2Type):
    #     if (len(pres1Type) == len(pres2Type)):
    #         if(pres1Type.lower() == pres2Type.lower()):
    #             return True
    #         elif is_valid_presentation(pres1Type) == False:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return True #same presentations

    def partition(self, inorder_presentation, partitionValue):
        """
        Function to partition the inorder string into left subtree inorder string and rightsubtree inorder string.
        :param inorder_presentation: inorder string of the tree on left of partition value.
        :param partitionValue: value from preorder string partition of value
        :return: 
        """
        left, right = None, None
        partitionIndex = 0
        for nodeVal in inorder_presentation:
            # partitioning at first node which matches partitionValue in input sequence
            if(nodeVal == partitionValue):
                break
            else:
                partitionIndex += 1

        if(partitionIndex >= 0):
            left = inorder_presentation[0:partitionIndex]
        else:
            left = None

        if(partitionIndex+1 <= len(inorder_presentation)-1):
            right = inorder_presentation[partitionIndex+1:]
        else:
            right = None

        return left, right

    def create_from_inorder_preorder(self, inorder_presentation = None, preorder_presentation = None, preorder_index = 0):
        """look at preorder presentation first, assign first element as root."""
        if inorder_presentation == None:
            return None
        partitionvalue = preorder_presentation[preorder_index]
        left_inorder_presentation, right_inorder_presentation = self.partition(inorder_presentation, partitionvalue)
        root = Node(preorder_presentation[preorder_index])
        if(preorder_index < len(preorder_presentation)):
            if left_inorder_presentation:
                preorder_index += 1
                root.left = self.create_from_inorder_preorder(left_inorder_presentation,preorder_presentation, preorder_index)
            else:
                root.left = None
            if right_inorder_presentation:
                preorder_index += 1
                root.right = self.create_from_inorder_preorder(right_inorder_presentation,preorder_presentation, preorder_index)
            else:
                root.right = None
        return root


    # def create_from_inorder_postorder(self, inorder_presentation=None, postorder_presentation=None):

    # def create_from_preorder_postorder(self, preorder_presentation=None, postorder_presentation=None):

    def InorderTraversal(self, currRoot, inorder, printout=False):
        if not currRoot:
            return None
        else:
            self.InorderTraversal(currRoot.left, inorder, printout)
            inorder.append(currRoot.data)
            if printout:
                print currRoot.data,
            self.InorderTraversal(currRoot.right, inorder, printout)
            return inorder

    def PreorderTraversal(self, currRoot, preorder, printout=False):
        if not currRoot:
            return None
        else:
            preorder.append(currRoot.data)
            if printout:
                print currRoot.data,
            self.PreorderTraversal(currRoot.left, preorder, printout)
            self.PreorderTraversal(currRoot.right, preorder, printout)
            return preorder

    def PostorderTraversal(self, currRoot, postorder, printout=False):
        if not currRoot:
            return None
        else:
            self.PostorderTraversal(currRoot.left, postorder, printout)
            self.PostorderTraversal(currRoot.right, postorder, printout)
            postorder.append(currRoot.data)
            if printout:
                print currRoot.data,
            return postorder

    def verify(self, presentation , presentationType):
        verified_presentation = []
        if presentationType.lower() == "inorder":
            inorder_verified = self.InorderTraversal(self.root, verified_presentation)
        elif presentationType.lower() == "preorder":
            preorder_verified = self.PreorderTraversal(self.root, verified_presentation)
        elif presentationType.lower() == "postorder":
            postorder_verified = self.PostorderTraversal(self.root, verified_presentation)

        if self.compare_presentations(presentation, verified_presentation):
            return True
        else:
            return False

    def create(self, presentation1 , presentation1Type , presentation2 , presentation2Type):
        if( presentation1 == None or presentation2 == None):
            print "At least 2 tree presentations are needed to construct the tree."
        # elif len(presentation1) != len(presentation2):
        #     print "Invalid presentations provided. Can't create the tree."
        # elif compare_presentations(presentation1, presentation2) == True:
        #     print "Invalid presentations provided. Can't create the tree."
        # elif compare_presentation_types(presentation1Type, presentation2Type) == True:
        #     print "Invalid presentations type provided, Can't create the tree."

        inorder_presentation,preorder_presentation,postorder_presentation = None,None,None

        if presentation1Type.lower() == "inorder":
            inorder_presentation = presentation1
        elif presentation1Type.lower() == "preorder":
            preorder_presentation = presentation1
        elif presentation1Type.lower() == "postorder":
            postorder_presentation = presentation1

        if presentation2Type.lower() == "inorder":
            inorder_presentation = presentation2
        elif presentation2Type.lower() == "preorder":
            preorder_presentation = presentation2
        elif presentation2Type.lower() == "postorder":
            postorder_presentation = presentation2

        if inorder_presentation and preorder_presentation:
            self.root = self.create_from_inorder_preorder(inorder_presentation, preorder_presentation, preorder_index=0)
        elif inorder_presentation and postorder_presentation:
            self.root = self.create_from_inorder_postorder(inorder_presentation, postorder_presentation)
        elif preorder_presentation and postorder_presentation:
            self.root = self.create_from_preorder_postorder(preorder_presentation, postorder_presentation)
        else:
            print "Invalid combination of presentation types. Can't create the tree"

        # verify the tree built is correct.
        if self.root:
            if self.verify(presentation1, presentation1Type) and self.verify(presentation2, presentation2Type):
                print "Tree Verification successful."
                return self
            else:
                print "Tree Verification failed."
                return None
        else:
            return None

if __name__ == '__main__':
    preorder = [2,1,3,4,5,6,7]
    inorder = [1,2,4,3,6,5,7]
    myTree = BinaryTree().create(inorder,"inorder",preorder,"preorder")
    print "Printing inorder traversal of built tree : "
    inorder = myTree.InorderTraversal(myTree.root, [])
    print inorder
    print "Finished creating tree at root node as: {}".format(myTree.root.data)
