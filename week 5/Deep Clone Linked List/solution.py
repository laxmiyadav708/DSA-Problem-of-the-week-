class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        node_map = {}
        new_head = Node(head.val)
        node_map[head] = new_head

        old_temp = head.next
        new_temp = new_head

        while old_temp:
            new_node = Node(old_temp.val)
            new_temp.next = new_node
            node_map[old_temp] = new_node

            new_temp = new_temp.next
            old_temp = old_temp.next

        old_temp = head
        new_temp = new_head

        while old_temp:
            if old_temp.random:
                new_temp.random = node_map[old_temp.random]
            old_temp = old_temp.next
            new_temp = new_temp.next

        return new_head
