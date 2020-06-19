import React from "react";
import gsap from "gsap";
import { Elastic } from "gsap/gsap-core";

const rnd = (min, max) => {
  return Math.random() * (max - min) + min;
};

const mult = rnd(0.01, 0.1);
const totalLevel = 5;
let sway = 0;

//creates position of every group which stacks on eachother
const posOfG = ({ len, ang, gen }) => {
  //rotation in deg
  if (gen === 0) sway++;
  const rotation =
    ang + (((Math.sin(sway * mult) * Math.PI) / 128) * 180) / Math.PI;
  const style = {
    id: "gen" + gen,
    //bad practices but i am lazy
    key: rnd(0, 1110004239042390482034820480293429034),
    transform:
      gen === 0
        ? `
        ${"scale(" + 3.5 + ")"} rotate(${rotation},0,0)`
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
        { ang: rnd(0, 50) },
        { gen: gen + 1 },
        { key: rnd(0, 1110004239042390482034820480293429034) }
      ),
      //each group has a path to scale
      React.createElement("path", {
        d: "M0,0 v-30 l3,-3 l3,3 v30 z",
        id: "path" + gen,

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
        { ang: rnd(0, -50) },
        { gen: gen + 1 },
        { key: rnd(0, 1110004239042390482034820480293429034) }
      ),
      //each group has a path to scale
      React.createElement("path", {
        d: "M0,0 v-30 l3,-3 l3,3 v30 z",
        id: "path" + gen,

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
      id: "path" + gen,
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
  componentDidMount() {
    var test = Elastic.easeOut.config(1, 0.3);
    gsap.timeline().from("#gen0", {
      duration: 2,
      transformOrigin: "50% bottom",
      scaleY: 0,
      ease: test,
    });
    gsap.timeline().from("#gen0 #path0", {
      duration: 0.1,
      transformOrigin: "50% bottom",
      scaleY: 0,
    });
    for (let i = 1; i < totalLevel + 1; i++) {
      gsap
        .timeline()
        .timeScale(10)
        .from("#gen" + i, {
          delay: 0.4,
          duration: 0.6,
          transformOrigin: "50% bottom",
          scaleY: 0.5,
          ease: test,
        });
      gsap
        .timeline()
        .timeScale(15)
        .from("#gen" + i + " #path" + i, {
          delay: 0.4 + i,
          duration: 0.6,
          transformOrigin: "50% bottom",
          scaleY: 0,
        });
    }
  }

  componentDidUpdate() {
    var test = Elastic.easeOut.config(1, 0.3);
    gsap.timeline().from("#gen0", {
      duration: 2,
      transformOrigin: "50% bottom",
      scaleY: 0,
      ease: test,
    });
    gsap.timeline().from("#gen0 #path0", {
      duration: 0.1,
      transformOrigin: "50% bottom",
      scaleY: 0,
    });
    for (let i = 1; i < totalLevel + 1; i++) {
      gsap
        .timeline()
        .timeScale(10)
        .from("#gen" + i, {
          delay: 0.4,
          duration: 0.6,
          transformOrigin: "50% bottom",
          scaleY: 0.5,
          ease: test,
        });
      gsap
        .timeline()
        .timeScale(15)
        .from("#gen" + i + " #path" + i, {
          delay: 0.4 + i,
          duration: 0.6,
          transformOrigin: "50% bottom",
          scaleY: 0,
        });
    }
  }

  render() {
    return (
      <svg
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="-400,-550,800,650"
        onClick={() => this.forceUpdate()}
      >
        <Branch len={80} ang={0} gen={0} />
      </svg>
    );
  }
}

export default Tree;
