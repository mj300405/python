from random import random

class Node:
    
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

class BST:

    def __init__(self):
        self.root=None

    def appendNode(self, value):
        if self.root==None:
            self.root=Node(value)
            return
        else:
            current=self.root
            while(True):
                if value<current.value:
                    if current.left==None:
                        current.left=Node(value)
                        return
                    current=current.left
                else:
                    if current.right==None:
                        current.right=Node(value)
                        return
                    current=current.right
                
    def searchNode(self, value):
        current=self.root
        while current!=None:
            if value==current.value: return current
            elif value<current.value: current=current.left
            else: current=current.right
        return None
        

    def deleteNode(self, value):
        def minNode(node):
            current = node
            while current.left != None:
                current = current.left
                return current

        def delete(node, value):
            if node == None:
                return None

            if value < node.value:
                node.left = delete(node.left, value)
            elif value > node.value:
                node.right = delete(node.right, value)
            else:
                if node.left == None:
                    return node.right
                elif node.right == None:
                    return node.left
                else:
                    minRight = minNode(node.right)
                    node.value = minRight.value
                    node.right = delete(node.right, minRight.value)
            return node

        self.root = delete(self.root, value)

    def __str__(self):
        pass

x=BST()
for i in range(100):
    x.appendNode(int(random()*100))


print(x.searchNode(4))
