# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 13:16:16 2023

@author: behira
"""
import random

def rotationRight(root):
    pivot = root.left
    reatchedNode = pivot.right
    root.left = reatchedNode
    pivot.right = root
    return pivot

def rotationLeft(root):
    pivot = root.right
    reatchedNode = pivot.left
    root.right = reatchedNode
    pivot.left = root
    return pivot

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None
        
    def search(self, target):
        
        curr = self.data
        if curr == target:
            print(f"Found it {curr}")
            return self
        elif self.left and curr> target:            
            return self.left.search(target)
        elif self.right and curr<target:
            return self.right.search(target)
        else:
            print('Not here')
            
    # chapter 2
    def addNode(self, data):
        if self.data == data:
            return
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.addNode(data)
                self.left = self.left.FixImbalanceIfExists()
                return
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
                return
            else:
                self.right.addNode(data) 
                self.right = self.right.FixImbalanceIfExists()
                
    def findmin(self):
        if self.left:
            return self.left.findmin()
        return self.data            
                
    def deleteNode(self, target):
        if self.data == target:
            # deletion happens here
            if self.right and self.left:
                # ## RTFM ## : Right tree find minimum 
                minval = self.right.findmin()
                self.data = minval
                self.right = self.right.deleteNode(minval)
                            
                return self
            else:
                return self.left or self.right
           
        if  target < self.data:
            self.left = self.left.deleteNode(target)
            
        if target > self.data:
            self.right = self.right.deleteNode(target)
           
        
        return self.FixImbalanceIfExists()       
    
    def is_balance(self):
        leftHeigh = self.left.height() if self.left else 0
        RightHeigh = self.right.height()  if self.right else 0
        return abs(leftHeigh-RightHeigh)<2
    
    def getLeftRightHeightDifference(self):
        leftHeigh = self.left.height() if self.left else 0
        RightHeigh = self.right.height()  if self.right else 0
        return leftHeigh-RightHeigh
    
    def FixImbalanceIfExists(self):
        if self.getLeftRightHeightDifference()>1:
            # left imbalanced
            if self.left.getLeftRightHeightDifference()>0:
                # left left imbalanced
                return rotationRight(self)
            else:
                # left right imbalance
                self.left = rotationLeft(self.left)
                return rotationRight(self)
        elif self.getLeftRightHeightDifference()<-1:
            # rigth imbalanced
            if self.right.getLeftRightHeightDifference()>0:
                # right left imbalanced 
               self.right = rotationRight(self.right)
               return rotationLeft(self)
            else:
                # right right imbalanced
                rotationLeft(self)
        
        return self 
    
    def rebalance(self):
      
        if self.left:
            self.left.rebalance()
            self.left = self.left.FixImbalanceIfExists()
            
        if self.right:
            self.right.rebalance()
            self.right = self.right.FixImbalanceIfExists()

    # ____________________      
    
    def traversePreOrder(self):
        print(self.data)
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()
            
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.data)
        if self.right:
           self.right.traverseInOrder()
        
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.data)
        
    def height(self, height= 0):
        leftheight = self.left.height(height+1) if self.left else height+1
        rightheight = self.right.height(height+1) if self.right else height+1
    
        return max(leftheight, rightheight)
    
    def getNodeAtDepth(self, depth,  nodes = []):
       
        if depth == 0:
            nodes.append(self)
            return nodes
        if self.left:
            self.left.getNodeAtDepth(depth-1, nodes) 
        else:
            nodes.extend([None]*2**(depth-1))
        if self.right:
            self.right.getNodeAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes

class Tree:
    def __init__(self, root, name = ''):
        self.root = Node(root)
        self.name = name
    def is_balance(self):
        return self.root.is_balance()
        
    def NodeToChar(self, n, spacing):
        if n is None:
            return ' ' +  (' '*spacing)
        d = str(n.data)
        if not n.is_balance():
            d = d+'*'
        spacing = spacing-len(str(d))+1
        return d+(' '*spacing)
    def search(self, target):
        return self.root.search(target)
    
    def traverseInOrder(self):
        return self.root.traverseInOrder()
    
    def traversePreOrder(self):
        return self.root.traversePreOrder()
    
    def traversePostOrder(self):
        return self.root.traversePostOrder()
    
    def getNodeAtDepth(self, depth, node =[]):
        return self.root.getNodeAtDepth(depth, node)
        
    def height(self):
        return self.root.height()
    
    def printNode(self, label = ' '):
        print(self.name + ':: ' + label)
        d = 0
        h = self.height()
        spacing = 6
        w = int((h+1)**2 + spacing -1)
        # check to see if it is balance
            
        offset = int((w-1)/2)   
        for d in range(0,h):
            if d>0:
                print(' '*(offset+1) + (' '*(spacing+2)).join(['/' +' '*(spacing-2) +  '\\']*(2**(d-1))))
            row  =self.getNodeAtDepth(d, node=[])
 
            print(' '*(offset) + ''.join([self.NodeToChar(n, spacing) for n in row]))
 
            spacing = offset+1
            offset = int(offset/2 -1)
            
    def addNode(self,data):
        self.root.addNode(data)
        self.root = self.root.FixImbalanceIfExists()
    
    def deleteNode(self, target):
        self.root = self.root.deleteNode(target)
 
    
    def rebalance(self):
        self.root.rebalance()
        self.root = self.root.FixImbalanceIfExists()
        
    def __str__(self):
        out  = self.name
        return out

if __name__ == "__main__":
    # node =  Node(10)
    # t = Tree(root = 50, name = 'Behzad\'s tree')
    # leaves = [12, 25, 75, 67, 100, 128, 80, 92]
    # for l in leaves:
    #       t.addNode(l)

    # print(t.name)
    # print(t.root.right.left.data)
    # print(t)
    # t.search(1000) 
    # print('preorder')
    # t.traversePreOrder()
    # print('inorder')
    # t.traverseInOrder() 
    # print('postorder')
    # t.traversePostOrder()    
    
    # print(f'the height is {t.height()}')
    
    # print(t.getNodeAtDepth(3))
    # t.printNode()
    # t.deleteNode(50)
    # t.printNode()
    # print(t.root.is_balance())
    # print(t.root.left.is_balance())
    
    
    # st = Tree(23, "small")
    # st.addNode(60)
    # st.addNode(100)
    # print(st.height())
    # st.printNode()
    # ------------------
    
    
    # ------------- UNBALANCED NODE -------------
    unbalancedleft = Tree(30, "UNBALANCED LEFT LEFT")
    unbalancedleft.root.left = Node(20)
    unbalancedleft.root.left.right = Node(21)
    unbalancedleft.root.left.left = Node(10)
    unbalancedleft.root.left.left.left = Node(9)
    unbalancedleft.root.left.left.right = Node(11)
    
    unbalancedleft.printNode()
    
    unbalancedleft.addNode(60)
    unbalancedleft.addNode(62)
    unbalancedleft.addNode(63)
    unbalancedleft.addNode(12)
    unbalancedleft.addNode(7)
    unbalancedleft.addNode(1)
    unbalancedleft.addNode(2)
    unbalancedleft.printNode()
    
    unbalancedleft.deleteNode(7)
    # unbalancedleft.deleteNode(30)
    unbalancedleft.printNode()
    # unbalancedleft.rebalance()
    # unbalancedleft.root = rotationRight(unbalancedleft.root)
    # unbalancedleft.printNode()
    
    # ------------- UNBALANCED NODE -------------
    # unbalancedright = Tree(10, "UNBALANCED RIGHT RIGHT")
    # unbalancedright.root.right = Node(20)
    # unbalancedright.root.right.right = Node(30)
    # unbalancedright.root.right.left= Node(19)
    # unbalancedright.root.right.right.left = Node(29)
    # unbalancedright.root.right.right.right = Node(31)
    
    # unbalancedright.printNode()
    # unbalancedright.root = rotationLeft(unbalancedright.root)
    # unbalancedright.printNode()
    
    