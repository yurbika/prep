/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function (J, S) {
  if (J == "" || S == "") return 0;
  cnt = 0;
  for (let i = 0; i < S.length; i++) {
    if (J.includes(S[i])) cnt++;
  }
  return cnt;
};
