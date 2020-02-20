# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.cnt = 0
        cur = head
        while cur:
            self.cnt += 1
            cur = cur.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        r = random.randrange(self.cnt)
        cur = self.head
        for i in range(r):
            cur = cur.next
        return cur.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()