multiplicationTable = function (size) {
  var table = [];
  for (var j = 0; j < size; j++) {
    var i = 1 + j;
    var k = 0;
    var l = 1;
    var table2 = [];
    while (k < size) {
      if (table[k + i] == null && k == 0) table2.push(i);
      else {
        table2.push(table2[0] + table2[0] * l);
        l++;
      }
      i++;
      k++;
    }
    table.push(table2);
  }

  return table;
};
