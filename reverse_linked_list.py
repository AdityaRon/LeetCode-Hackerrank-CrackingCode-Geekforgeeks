class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.head = head
        previous = None
        forward = None
        while head:
            forward = head.next
            head.next = previous
            previous = head
            head =  forward
        return previous
