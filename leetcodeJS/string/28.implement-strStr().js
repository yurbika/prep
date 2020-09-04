/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  if (needle.length === 0) return 0;
  let h = haystack.length;
  let n = needle.length;
  for (let i = 0; i < h - n + 1; i++) {
    if (haystack.substring(i, i + n) === needle) return i;
  }
  return -1;
};
