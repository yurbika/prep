/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  let indegree = new Array(numCourses).fill(0);
  let stack = [];
  let count = 0;

  for (const i of prerequisites) {
    indegree[i[0]] += 1;
  }

  for (let i = 0; i < indegree.length; i++) {
    if (indegree[i] === 0) stack.push(i);
  }

  while (stack.length !== 0) {
    const c = stack.pop();
    count += 1;

    for (const i of prerequisites) {
      if (i[1] === c) {
        indegree[i[0]] -= 1;
        if (indegree[i[0]] === 0) {
          stack.push(i[0]);
        }
      }
    }
  }
  return count === numCourses;
};
