"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 官方算法3
        if not head:
            return head
        
        # Creating a new weaved list of original and copied nodes.
        cur = head
        while cur:
            # Cloned node
            nNode = Node(cur.val,cur.next,None)
            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            cur.next = nNode
            cur = nNode.next
        
        cur = head
        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        cur = head
        cur_new = head.next
        new_head = head.next
        while cur:
            cur.next = cur.next.next
            cur_new.next = cur_new.next.next if cur_new.next else None
            cur = cur.next
            cur_new = cur_new.next
        return new_head
