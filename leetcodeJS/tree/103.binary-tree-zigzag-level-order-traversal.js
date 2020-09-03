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
 * @return {number[][]}
 */
const bfs = (node, temp) => {
  if (node.left && node.right) {
    temp.push(node.left);
    temp.push(node.right);
  } else if (node.left && !node.right) {
    temp.push(node.left);
  } else if (!node.left && node.right) {
    temp.push(node.right);
  }
  return;
};

var zigzagLevelOrder = function (root) {
  if (!root) return [];
  let stack = [];
  stack.push(root);
  let solution = [[root.val]];
  let level = 2;
  while (stack.length !== 0) {
    let temp = [];
    while (stack.length !== 0) {
      bfs(stack.shift(), temp);
    }
    let values = [];
    for (let i of temp) {
      values.push(i.val);
    }
    if (level % 2 === 0) values = values.reverse();
    if (values.length !== 0) solution.push(values);
    stack = [...temp];
    level++;
  }
  return solution;
};
