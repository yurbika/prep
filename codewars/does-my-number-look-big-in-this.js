function narcissistic(value) {
  split = value
    .toString()
    .split("")
    .map((i) => Number(i));
  i = 0;
  while (true) {
    sum = 0;
    split.map((v) => (sum += Math.pow(v, i)));
    i++;
    if (sum === value) return true;
    if (sum > value) return false;
  }
}
