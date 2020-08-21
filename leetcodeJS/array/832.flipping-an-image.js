/**
 * @param {number[][]} A
 * @return {number[][]}
 */
var flipAndInvertImage = function (A) {
  for (i of A) {
    for (let j = 0; j < i.length; j++) {
      if (i[j] == 1) i[j] = 0;
      else {
        i[j] = 1;
      }
    }
    i.reverse();
  }
  return A;
};
