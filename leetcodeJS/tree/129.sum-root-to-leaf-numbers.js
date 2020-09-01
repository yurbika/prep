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
 * @return {number}
 */

const helper = (root, head, memo) => {
  if (root.left) helper(root.left, head + `${root.val}`, memo);
  if (root.right) helper(root.right, head + `${root.val}`, memo);
  if (!root.left && !root.right) memo.push(Number(head + `${root.val}`));
  return;
};

var sumNumbers = function (root) {
  if (!root) return 0;
  let memo = [];
  helper(root, "", memo);
  return memo.reduce((acc, val) => acc + val);
};
