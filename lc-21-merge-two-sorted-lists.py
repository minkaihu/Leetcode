# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

 
class LinkedList:
 
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None
    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.val)
            printval = printval.next          
class Solution:
    def mergeTwoLists(self, list1, list2):
        LL = LinkedList()
       
 

        newlistListNode = ListNode()
        
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2

        if list1.val <= list2.val:
            newlistListNode.next = list1
            list1, newlistListNode = list1.next, list1


        else:
            newlistListNode.next = list2
            list2, newlistListNode = list2.next, list2
            
        LL.head = newlistListNode


        while list1 or list2:
            if list1 == None and (list2 != None):
                print("check1")
                newlistListNode.next = list2
                list2, newlistListNode = list2.next, newlistListNode.next
            elif list2 == None and list1 != None:

                newlistListNode.next = list1
                list1, newlistListNode = list1.next, newlistListNode.next
            elif list1.val <= list2.val:

                newlistListNode.next = list1
                list1, newlistListNode = list1.next, newlistListNode.next

            elif list2.val <= list1.val:

                newlistListNode.next = list2
                list2, newlistListNode = list2.next, newlistListNode.next
        return LL.head
        