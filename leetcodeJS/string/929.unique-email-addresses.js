/**
 * @param {string[]} emails
 * @return {number}
 */

const formEmail = (email) => {
  let arr = email.split("@");
  let front = arr[0].split("+")[0];
  front = front.split(".").join("");
  return front + "@" + arr[1];
};

var numUniqueEmails = function (emails) {
  let solution = [];
  for (i of emails) {
    let email = formEmail(i);
    if (!solution.includes(email)) solution.push(email);
  }
  return solution.length;
};
