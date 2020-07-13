// This problem takes its name by arguably the most important event in the life of the ancient historian Josephus: according to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege.

// Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and proceeded to kill one man every three, until one last man was left (and that it was supposed to kill himself to end the act).

// Well, Josephus and another man were the last two and, as we now know every detail of the story, you may have correctly guessed that they didn't exactly follow through the original idea.

// You are now to create a function that returns a Josephus permutation, taking as parameters the initial array/list of items to be permuted as if they were in a circle and counted out every k places until none remained.

// Tips and notes: it helps to start counting from 1 up to n, instead of the usual range 0..n-1; k will always be >=1.

// For example, with n=7 and k=3 josephus(7,3) should act this way.

// [1,2,3,4,5,6,7] - initial sequence
// [1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
// [1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
// [1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
// [1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
// [1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
// [4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
// [] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]

//solution of best user
function josephus(items, k) {
  let result = [],
    index = 0;
  while (items.length > 0) {
    index = (index + k - 1) % items.length;
    result = result.concat(items.splice(index, 1));
  }
  return result;
}

//my solution
//behandelt nicht alle fälle zum beispiel [true,false,true,false]
function josephus(items, k) {
  let arr = [];
  let arr2 = [];
  let i = 0;
  let counter = 1;
  while (arr.length < items.length) {
    if (counter === k && !arr2.includes(i)) {
      arr2.push(i);
      counter = 1;
      arr.push(items[i]);
      if (i === items.length - 1) i = 0;
      else i++;
      continue;
    }
    if (!arr2.includes(i)) counter++;
    i++;
    if (i === items.length) i = 0;
  }
  return arr;
}

//other version we only get numbers

// josephus_survivor(7,3) => means 7 people in a circle;
// one every 3 is eliminated until one remains
// [1,2,3,4,5,6,7] - initial sequence
// [1,2,4,5,6,7] => 3 is counted out
// [1,2,4,5,7] => 6 is counted out
// [1,4,5,7] => 2 is counted out
// [1,4,5] => 7 is counted out
// [1,4] => 5 is counted out
// [4] => 1 counted out, 4 is the last element - the survivor!

//solution with recursion
function josephusSurvivor(n, k) {
  return n < 1 ? 1 : ((josephusSurvivor(n - 1, k) + --k) % n) + 1;
}

//n = 11 k = 19

// 11 19 12     return 10
// 10 19 11     4 + 18 % 12 = 10
// 9 19 10      8 + 18 % 11 = 4
// 8 19 9       0 + 18 % 10 = 8
// 7 19 8       0 + 18 % 9 = 0
// 6 19 7       6 + 18 % 8 = 0
// 5 19 6       1 + 18 % 7 = 6
// 4 19 5       1 + 18 % 6 = 1
// 3 19 4       3 + 18 % 5 = 1
// 2 19 3       1 + 18 % 4 = 3
// 1 19 2       1 + 18 % 2 = 1
// 0 19 1       return 1
