# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        head = ListNode(arr.pop())
        node = head
        for i in range(len(arr)-1, -1, -1):
            head.next = ListNode(arr[i])
            head = head.next

        return node
