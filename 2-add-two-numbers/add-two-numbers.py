# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summ = 0
        dummy = ListNode(0)
        curent = dummy
        crry = 0
        while l1 or l2 or crry:
            if l1 is not None:
                val1 = l1.val
            else:
                val1 = 0
            if l2 is not None:
                val2 = l2.val
            else:
                val2 = 0
            summ = val1 + val2 + crry
            crry = summ //10
            digit = summ%10 #keep the rest

            #create the new node
            curent.next = ListNode(digit)
            curent = curent.next

            if l1: l1 = l1.next #walking
            if l2: l2 = l2.next #walking

        return dummy.next


        