/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {string[]}
 */

const helper = (s, dict, memo) => {
  if (memo[s]) return memo[s];
  if (s.length === 0) return [];

  let res = [];
  for (let i of dict) {
    if (!s.startsWith(i)) continue;
    if (i.length === s.length) res.push(i);
    else {
      let result = helper(s.slice(i.length, s.length), dict, memo);
      for (let j of result) {
        j = i + " " + j;
        res.push(j);
      }
    }
  }
  memo[s] = res;
  return res;
};

var wordBreak = function (s, wordDict) {
  let memo = {};
  return helper(s, wordDict, memo);
};
