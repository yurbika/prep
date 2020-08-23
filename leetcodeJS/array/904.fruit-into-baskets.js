/**
 * @param {number[]} tree
 * @return {number}
 */
var totalFruit = function (tree) {
  if (tree.length == 0) return 0;
  if (tree.length < 3) return tree.length;
  let length = 0;
  let p = 0;
  let p2 = 1;
  let cnt = 1;
  let basket = [tree[p]];

  while (p2 < tree.length) {
    if (basket.includes(tree[p2])) basket.push(tree[p2]);
    else if (!basket.includes(tree[p2]) && cnt != 2) {
      cnt++;
      basket.push(tree[p2]);
    }
    if (!basket.includes(tree[p2]) && cnt == 2) {
      if (basket.length > length) length = basket.length;
      p = p2 - 1;
      while (tree[p] == tree[p - 1]) p--;
      p2 = p + 1;
      basket = [tree[p]];
      cnt = 1;
    } else {
      if (basket.length > length) length = basket.length;
      p2++;
    }
  }
  return length;
};
