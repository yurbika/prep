/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  if (needle.length === 0) return 0;
  let left = 0;
  let right = 0;
  let p = 0;
  while (right < haystack.length) {
    if (haystack[right] === needle[p]) {
      while (haystack[right] === needle[p] && p < needle.length) {
        right++;
        p++;
      }
      if (p === needle.length) return left;
      else {
        left++;
        right = left;
        p = 0;
      }
    } else {
      left++;
      right++;
    }
  }
  return -1;
};
