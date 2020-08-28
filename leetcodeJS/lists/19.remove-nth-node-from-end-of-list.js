/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  node = head;
  arr = [];
  while (node) {
    arr.push(node.val);
    node = node.next;
  }
  arr[arr.length - n] = null;
  arr = arr.filter((a) => a !== null);
  if (arr.length === 0) return null;
  temp = new ListNode(arr.shift());
  head = temp;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== null) {
      temp.next = new ListNode(arr[i]);
      temp = temp.next;
    }
  }
  return head;
};
