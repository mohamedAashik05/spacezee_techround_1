class node:
    def __init__(self, val, next=None, random = None):
        self.val = val
        self.next = next
        self.random = random

def copyrandomlist(head):
    if not head:
        return None
    mapping = {}
    curr = head

    while curr:
        mapping[curr] = node(curr.val)
        curr = curr.next
    curr = head
    while curr:
        if curr.next:
            mapping[curr].next = mapping[curr.next]
        if curr.random:
            mapping[curr].random = mapping[curr.random]
            curr = curr.next
    return mapping[head]
