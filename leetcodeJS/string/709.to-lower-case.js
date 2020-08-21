/**
 * @param {string} str
 * @return {string}
 */
var toLowerCase = function (str) {
  let arr = [...str];
  for (let i = 0; i < arr.length; i++) {
    if (str.charCodeAt(i) < 97 && 65 <= str.charCodeAt(i)) {
      arr[i] = String.fromCharCode(str.charCodeAt(i) - 65 + 97);
    }
  }
  return arr.join("");
};
