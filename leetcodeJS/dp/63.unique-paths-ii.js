/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function (obstacleGrid) {
  if (obstacleGrid[0][0] === 1 || obstacleGrid.length === 0) return 0;
  for (let i = 0; i < obstacleGrid.length; i++) {
    for (let j = 0; j < obstacleGrid[i].length; j++) {
      if (i > 0 && j === 0 && obstacleGrid[i - 1][j] === 0)
        obstacleGrid[i][j] = 0;
      else if (i === 0 && j > 0 && obstacleGrid[i][j - 1] === 0)
        obstacleGrid[i][j] = 0;
      else if (obstacleGrid[i][j] == 0) obstacleGrid[i][j] = 1;
      else obstacleGrid[i][j] = 0;
    }
  }

  for (let i = 1; i < obstacleGrid.length; i++) {
    for (let j = 1; j < obstacleGrid[i].length; j++) {
      if (obstacleGrid[i][j - 1] === 0 && obstacleGrid[i - 1][j] === 0)
        obstacleGrid[i][j] = 0;
      if (obstacleGrid[i][j] == 0) continue;
      else obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j];
    }
  }
  return obstacleGrid[obstacleGrid.length - 1][obstacleGrid[0].length - 1];
};
