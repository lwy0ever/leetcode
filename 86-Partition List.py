# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # ans and bigHead are the two pointers used to create two list
        # cur and bigC are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        ans = ListNode(0)
        cur = ans
        bigHead = ListNode(0)
        bigC = bigHead
        c = head
        while c:
            # If the original list node is lesser than the given x,
            # assign it to the ans list.
            if c.val < x:
                cur.next = c
                cur = cur.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the bigHead list.
                bigC.next = c
                bigC = bigC.next
            # move ahead in the original list
            c = c.next
        # Last node of bigHead list would also be ending node of the reformed list
        bigC.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        cur.next = bigHead.next
        return ans.next