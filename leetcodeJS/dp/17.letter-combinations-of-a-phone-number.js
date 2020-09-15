/**
 * @param {string} digits
 * @return {string[]}
 */

const wave = (digit, arr, phone) => {
  let temp = [];
  let chars = [...phone[digit]];

  for (let i of chars) {
    for (let j of arr) {
      temp.push(i + j);
    }
  }
  return temp;
};

const helper = (digits, phone) => {
  if (digits.length === 2) {
    return wave(digits[0], [...phone[digits[1]]], phone);
  }

  let char = digits.slice(0, 1);
  return wave(char, helper(digits.slice(1, digits.length), phone), phone);
};

var letterCombinations = function (digits) {
  if (digits.length === 0) return [];

  let phone = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
  };
  if (digits.length === 1) return [...phone[digits[0]]];
  return helper(digits, phone);
};
