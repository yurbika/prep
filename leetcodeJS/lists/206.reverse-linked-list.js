function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  if (!head) return null;
  let arr = [];
  while (head) {
    arr.push(head.val);
    head = head.next;
  }

  head = new ListNode(arr.pop());
  let temp = head;
  for (let i = arr.length - 1; i >= 0; i--) {
    head.next = new ListNode(arr[i]);
    head = head.next;
  }
  return temp;
};
