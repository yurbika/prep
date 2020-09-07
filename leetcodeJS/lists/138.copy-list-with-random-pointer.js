/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function (head) {
  if (!head) return head;

  let ptr = head;
  while (ptr) {
    newNode = new Node(ptr.val);
    newNode.next = ptr.next;
    ptr.next = newNode;
    ptr = newNode.next;
  }
  ptr = head;
  while (ptr) {
    ptr.next.random = ptr.random ? ptr.random.next : null;
    ptr = ptr.next.next;
  }
  let ptr_old_list = head;
  let ptr_new_list = head.next;
  let head_old = head.next;
  while (ptr_old_list) {
    ptr_old_list.next = ptr_old_list.next.next;
    ptr_new_list.next = ptr_new_list.next ? ptr_new_list.next.next : null;
    ptr_old_list = ptr_old_list.next;
    ptr_new_list = ptr_new_list.next;
  }
  return head_old;
};
