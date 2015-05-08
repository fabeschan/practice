
def reverse_recursive(node):
    # 1->2->3->4

    if node and node.next:
        last = node.next # this will be the last element after reversal
        head = reverse(node.next) #reverse the rest of the list
        last.next = node
        node.next = None
        return head
    else:
        return node

def reverse_iterative(node):
    # 1->2->3->4->NULL

    if node and node.next:
        nextnode = node.next
        nextnextnode = nextnode.next
    else:
        return node

    while nextnextnode:
        nextnode.next = node
        node = nextnode
        nextnode = nextnextnode
        nextnextnode = nextnode.next
    node.next = None
    nextnode.next = node
    return nextnode
