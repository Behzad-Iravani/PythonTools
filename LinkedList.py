# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:15:58 2023
Data and Stricture in python:
    This class creates the linked list object 
    
@author: behira
"""

class Node:
    def __init__(self, value, Next= None):
        self.value = value 
        self.next = Next
    def push(self, data):
        if self.next == None:   
            self.next = Node(data)
        else:
            self.next.push(data)
           
    def printList(self): 
        if self.next:
            print(str(self.value))
            print('|')
            self.next.printList()
        else:
            print(self.value)
            print('$Tail')
    def size(self):
        dummy = self
        c = 0
        while dummy.next:
             dummy=dummy.next
             c +=1
        return c

# Wrapper class
class LinkedList:
    def __init__(self, head):
        self.head = Node(head)
        
    def push(self, data):
        if self.head.next == None:
            self.head.next = Node(data) 
        else:
            self.head.next.push(data)
            
    def printList(self):
        print('$Head')
        self.head.printList()
    
    def size(self):
        return self.head.size()
        
    
if __name__ == "__main__":
    
    # Create an instance of Linked List
    L = LinkedList(2)
    #  adding some data to linked list 
    L.push(5)
    L.push(0)
    L.push(1000)
    L.push(55)
    # print the linked list
    L.printList()
    # pritn the size of the list 
    print(L.size())
        



