function wave(name) {
  var wavestring = [];
  for (var i = 0; i < name.length; i++) {
    var temp = name.split("");
    temp[i] = temp[i].toUpperCase();
    if (temp[i] == " ") continue;

    wavestring.push(temp.join(""));
  }
  return wavestring;
}
