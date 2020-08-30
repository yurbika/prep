/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function (l1, l2) {
  if (!l1 && !l2) return null;
  let arr = [];
  while (l1) {
    arr.push(l1.val);
    l1 = l1.next;
  }

  while (l2) {
    arr.push(l2.val);
    l2 = l2.next;
  }

  arr.sort((a, b) => a - b);
  node = new ListNode(arr.shift());
  head = node;
  for (let i of arr) {
    node.next = new ListNode(i);
    node = node.next;
  }

  return head;
};
