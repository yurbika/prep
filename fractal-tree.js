import React from "react";

function rnd(min, max) {
  return Math.random() * (max - min) + min;
}

var mult = rnd(0.01, 0.1);
var totalLevel = 6;

//creates position of every group which stacks on eachother
const posOfG = ({ gen, ang }) => {
  //rotation in deg
  const rotation = ang + (((Math.sin(mult) * Math.PI) / 128) * 180) / Math.PI;
  const style = {
    id: "gen" + gen,
    //bad practices but i am lazy
    key: rnd(0, 1110004239042390482034820480293429034),
    transform:
      gen === 0
        ? `
        ${"scale(" + 2.5 + ")"} rotate(${rotation},0,0)`
        : //translate values are depending on the path values
          `translate(0.35,-28.8) ${"scale(0.87)"} rotate(${rotation},0,0)`,
  };

  return style;
};

const Branch = ({ len, ang, gen }) => {
  const style = posOfG({ len, ang, gen });
  //each branch has a left and right child
  const left =
    gen < totalLevel &&
    React.createElement(
      Branch,
      Object.assign(
        { len: len * rnd(0.8, 0.99) },
        { ang: rnd(0, 37) },
        { gen: gen + 1 },
        { key: rnd(0, 1110004239042390482034820480293429034) }
      ),
      //each group has a path to scale
      React.createElement("path", {
        d: "M0,0 v-30 l3,-3 l3,3 v30 z",
        style: {
          strokeWidth: 0.1,
          fill: "#939ca7",
        },
        key: rnd(0, 1110004239042390482034820480293429034),
      })
    );

  const right =
    gen < totalLevel &&
    React.createElement(
      Branch,
      Object.assign(
        { len: len * rnd(0.8, 0.99) },
        { ang: rnd(0, -37) },
        { gen: gen + 1 },
        { key: rnd(0, 1110004239042390482034820480293429034) }
      ),
      //each group has a path to scale
      React.createElement("path", {
        d: "M0,0 v-30 l3,-3 l3,3 v30 z",
        style: {
          strokeWidth: 0.1,
          fill: "#939ca7",
        },
        key: rnd(0, 1110004239042390482034820480293429034),
      })
    );

  return React.createElement(
    "g",
    style,
    //each group has a path to scale
    React.createElement("path", {
      d: "M0,0 v-30 l3,-3 l3,3 v30 z",
      style: {
        strokeWidth: 0.1,
        fill: "#939ca7",
      },
      key: rnd(0, 1110004239042390482034820480293429034),
    }),
    left,
    right
  );
};

class Tree extends React.Component {
  render() {
    return (
      <svg
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="-400,-500,800,650"
      >
        <Branch len={80} ang={0} gen={0} />
      </svg>
    );
  }
}

export default Tree;
