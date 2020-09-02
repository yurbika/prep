/**
 * @param {string} s
 * @return {string[]}
 */
const helper = (s, cnt, start, memo) => {
  if (cnt === 3 && Number(s.slice(start, s.length)) <= 255) {
    if (s.slice(start, s.length).length > 1 && s[start] !== "0") memo.push(s);
    else if (s.slice(start, s.length).length === 1) memo.push(s);

    return;
  }

  for (let i = start; i < s.length - 1; i++) {
    if (s.slice(start, i + 1).length > 1 && s[start] === "0") return;
    if (Number(s.slice(start, i + 1)) > 255) return;
    if (cnt === 3) return;
    helper(
      s.slice(0, start) + s.slice(start, i + 1) + "." + s.slice(i + 1),
      cnt + 1,
      i + 2,
      memo
    );
  }
};
var restoreIpAddresses = function (s) {
  if (s.length < 4) return [];
  let memo = [];
  helper(s, 0, 0, memo);
  return memo;
};
