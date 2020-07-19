function rgb(r, g, b) {
  // complete this function
  r < 0 ? (r = 0) : null;
  g < 0 ? (g = 0) : null;
  b < 0 ? (b = 0) : null;
  r > 255 ? (r = 255) : null;
  g > 255 ? (g = 255) : null;
  b > 255 ? (b = 255) : null;
  let hex = "";
  let rHex = r.toString(16).toUpperCase();
  let gHex = g.toString(16).toUpperCase();
  let bHex = b.toString(16).toUpperCase();
  console.log(rHex, gHex, bHex);
  r <= 15 ? (rHex = "0" + rHex) : null;
  g <= 15 ? (gHex = "0" + gHex) : null;
  b <= 15 ? (bHex = "0" + bHex) : null;
  return (hex += rHex + "" + gHex + "" + bHex);
}
