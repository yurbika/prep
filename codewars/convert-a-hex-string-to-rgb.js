function hexStringToRGB(hexString) {
  hexString = hexString.slice(1);
  let arr = [];

  while (hexString.length > 0) {
    arr.push(hexString.slice(0, 2));
    hexString = hexString.slice(2);
  }
  arr = arr.map((i) => "0x" + i).map((i) => parseInt(i));

  let obj = {};

  obj.r = arr[0];
  obj.g = arr[1];
  obj.b = arr[2];

  return obj;
}
