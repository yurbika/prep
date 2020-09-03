/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  if (intervals.length === 0) return intervals;
  if (intervals.length === 1) return intervals;
  intervals = intervals.sort((a, b) => a[0] - b[0]);
  let solution = [intervals[0]];
  let j = 0;
  for (let i = 1; i < intervals.length; i++) {
    j = solution.length - 1;
    if (
      (intervals[i][0] < solution[j][1] ||
        intervals[i][0] === solution[j][1]) &&
      intervals[i][1] > solution[j][1]
    ) {
      solution[j][1] = intervals[i][1];
    } else if (intervals[i][0] > solution[j][1]) {
      solution.push(intervals[i]);
    }
  }
  return solution;
};
