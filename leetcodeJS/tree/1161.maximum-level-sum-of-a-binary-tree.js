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

const getChildren = (root) => {
  if (root.left && root.right) return [root.left, root.right];
  if (root.left && !root.right) return [root.left];
  return [root.right];
};

var maxLevelSum = function (root) {
  if (!root) return;
  let solution = [root.val];
  let stack = [root];
  while (stack.length) {
    let temp = [];
    while (stack.length) {
      let cur = stack.shift();
      solution[solution.length - 1] += cur.val;
      temp = [...temp, ...getChildren(cur)];
    }
    stack = [];
    for (i of temp) {
      if (i) stack.push(i);
    }
    if (stack.length) solution.push(0);
  }
  return solution.indexOf(Math.max(...solution)) + 1;
};
