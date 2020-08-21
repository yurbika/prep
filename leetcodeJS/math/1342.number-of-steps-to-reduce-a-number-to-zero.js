/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function (num) {
  cnt = 0;
  while (num > 0) {
    if (num % 2 == 0) num /= 2;
    else {
      num--;
    }
    cnt++;
  }
  return cnt;
};
