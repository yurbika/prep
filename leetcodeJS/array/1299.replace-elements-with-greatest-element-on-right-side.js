const replaceElements = (arr) => {
  let max = -1;

  for (let i = arr.length - 1; i > -1; i -= 1) {
    max = Math.max(arr[i], (arr[i] = max));
  }

  return arr;
};
