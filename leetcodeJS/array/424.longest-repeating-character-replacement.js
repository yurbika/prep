var characterReplacement = function (s, k) {
  const charCount = new Array(26).fill(0);

  let left = 0;
  let maxLength = 0;
  let maxCount = 0;

  for (let i = 0; i < s.length; i++) {
    const cur = s.charCodeAt(i) - 65;
    charCount[cur]++;
    maxCount = Math.max(maxCount, charCount[cur]);

    while (i - left + 1 - maxCount > k) {
      const leftChar = s.charCodeAt(left) - 65;
      charCount[leftChar]--;
      left++;
    }

    maxLength = (maxLength, i - left + 1);
  }

  return maxLength;
};
