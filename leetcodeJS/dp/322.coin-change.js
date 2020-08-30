/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */

var coinChange = function (coins, amount) {
  let dp = new Array(amount + 1);
  for (let i = 0; i < dp.length; i++) {
    dp[i] = Number.MAX_VALUE;
  }
  dp[0] = 0;
  for (let i of coins) {
    for (let j = i; j < amount + 1; j++) {
      dp[j] = Math.min(dp[j], dp[j - i] + 1);
    }
  }
  return dp[amount] != Number.MAX_VALUE ? dp[amount] : -1;
};
