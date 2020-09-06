/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function (root) {
  if (!root) return [];
  let memo = [];
  let stack = [];
  while (stack.length !== 0 || root) {
    while (root) {
      stack.push(root);
      root = root.left;
    }
    root = stack.pop();
    memo.push(root.val);
    root = root.right;
  }

  return memo;
};
