function add(n) {
  let fn = (x) => add(n + x);
  fn.valueOf = () => n;
  return fn;
}
