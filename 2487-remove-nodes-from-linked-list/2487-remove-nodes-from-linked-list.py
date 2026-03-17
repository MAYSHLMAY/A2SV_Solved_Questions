# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        temp = head

        while (temp != None):

            while (stack and stack[-1].val < temp.val):
                stack.pop()
            stack.append(temp)

            temp = temp.next
        
        head = None
        
        while (stack):
            if (head == None):
                head = stack.pop()
            else:
                popped = stack.pop()
                popped.next = head
                head = popped
        
        return head


        