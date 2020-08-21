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
 * @param {number} L
 * @param {number} R
 * @return {number}
 */
var rangeSumBST = function (root, L, R) {
  if (!root) return 0;
  cnt = 0;
  if (root.val >= L && root.val <= R) {
    cnt += root.val;
  }

  cnt += rangeSumBST(root.left, L, R);
  cnt += rangeSumBST(root.right, L, R);
  return cnt;
};
