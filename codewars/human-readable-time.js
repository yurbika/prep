function humanReadable(seconds) {
  // TODO
  if (seconds === 86400) return "24:00:00";
  let hours = Math.floor(seconds / 3600);
  let second = seconds % 3600;
  let minutes = Math.floor(second / 60);
  let seconde = second % 60;

  let time = "";
  if (hours < 9) time = "0" + hours + ":";
  else time += hours + ":";
  if (minutes < 9) time += "0" + minutes + ":";
  else time += minutes + ":";
  if (seconde < 9) time += "0" + seconde;
  else time += seconde;
  return time;
}
