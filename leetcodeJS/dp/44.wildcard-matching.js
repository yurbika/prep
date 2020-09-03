/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function (s, p) {
  if (p === "*") return true;
  let temp = [];
  let i = 0;
  while (i < p.length) {
    if (p[i] === "*") {
      temp.push(p[i]);
      while (p[i] === "*") i++;
    } else {
      temp.push(p[i]);
      i++;
    }
  }
  p = temp.join("");
  let dp = new Array(s.length + 1);
  for (let i = 0; i < s.length + 1; i++) {
    dp[i] = new Array(p.length + 1).fill(false);
  }

  dp[0][0] = true;
  if (p[0] === "*") dp[0][1] = true;
  for (let i = 1; i < dp.length; i++) {
    for (let j = 1; j < dp[0].length; j++) {
      if (p[j - 1] == "?" || s[i - 1] === p[j - 1]) dp[i][j] = dp[i - 1][j - 1];
      else if (p[j - 1] == "*") dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
    }
  }
  return dp[s.length][p.length];
};
