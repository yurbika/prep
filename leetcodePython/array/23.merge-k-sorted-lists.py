# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         if not any(lists):
#             return
#         if len(lists) == 1:
#             return lists[0]

#         lists = [i for i in lists if i is not None]
#         lists.sort(key=lambda l: l.val)
#         l = ListNode(lists[0].val)
#         lists[0] = lists[0].next
#         head = l

#         while any(lists):
#             curMinValueIndex = None
#             for i in range(len(lists)):
#                 if curMinValueIndex is None and lists[i]:
#                     curMinValueIndex = i
#                 if lists[i] and lists[curMinValueIndex].val > lists[i].val:
#                     curMinValueIndex = i
#             if lists[curMinValueIndex]:
#                 l.next = ListNode(lists[curMinValueIndex].val)
#                 l = l.next
#                 lists[curMinValueIndex] = lists[curMinValueIndex].next

#         return head

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not any(lists):
            return
        if len(lists) == 1:
            return lists[0]

        solution = []

        for i in lists:
            while i:
                solution.append(i.val)
                i = i.next

        solution.sort()
        l = ListNode(solution[0])
        head = l

        for i in range(1, len(solution)):
            l.next = ListNode(solution[i])
            l = l.next

        return head
