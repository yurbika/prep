/**
 * @param {string} keyboard
 * @param {string} word
 * @return {number}
 */
var calculateTime = function (keyboard, word) {
  let p = 0;
  let time = 0;
  for (i of word) {
    time += Math.abs(keyboard.indexOf(i) - p);
    p = keyboard.indexOf(i);
  }
  return time;
};
