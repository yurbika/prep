/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number}
 */

const swap = (a, b, val) => {
  let cnt = 0;
  for (let i = 0; i < a.length; i++) {
    if (a[i] != val && b[i] != val) return Number.MAX_VALUE;
    else if (a[i] != val && b[i] == val) {
      cnt++;
    }
  }
  return cnt;
};

var minDominoRotations = function (A, B) {
  let minRotations = Math.min(swap(A, B, A[0]), swap(A, B, B[0]));
  minRotations = Math.min(swap(B, A, A[0]), minRotations);
  minRotations = Math.min(swap(B, A, B[0]), minRotations);

  if (minRotations == Number.MAX_VALUE) return -1;
  return minRotations;
};
