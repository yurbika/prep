import React from "react";
import gsap from "gsap";
import { Elastic } from "gsap/gsap-core";

import { ReactComponent as Html5 } from "./svg/html5.svg";
import { ReactComponent as ReactSvg } from "./svg/react.svg";
import { ReactComponent as Css } from "./svg/css.svg";
import { ReactComponent as Npm } from "./svg/npm.svg";
import { ReactComponent as Redux } from "./svg/redux.svg";
import { ReactComponent as Rr } from "./svg/rr.svg";
import { ReactComponent as Sass } from "./svg/sass.svg";
import { ReactComponent as Js } from "./svg/js.svg";
import { ReactComponent as Git } from "./svg/git.svg";
import { ReactComponent as Sc } from "./svg/sc.svg";

const rnd = (min, max) => {
  return Math.random() * (max - min) + min;
};

const mult = rnd(-31, 31);
const totalLevel = 7;
let sway = 0;
let logoArr = [Html5, ReactSvg, Css, Npm, Redux, Rr, Sass, Js, Git, Sc];

//creates position of every group which stacks on eachother
const posOfG = ({ len, ang, gen }) => {
  //rotation in deg
  sway++;
  const rotation =
    ang + (((Math.sin(sway * mult) * Math.PI) / 128) * 180) / Math.PI;
  const style = {
    id: "gen" + gen,
    //bad practices but i am lazy
    key: rnd(0, 1110004239042390482034820480293429034),
    transform:
      gen === 0
        ? `
        ${"scale(" + 3 + ")"} rotate(${rotation},0,0)`
        : //translate values are depending on the path values
        gen === totalLevel
        ? `translate(-22,-65) ${"scale(0.5)"} rotate(0,0,0)`
        : `translate(0.35,-28.8) ${
            "scale(" + len + ")"
          } rotate(${rotation},0,0)`,
  };

  return style;
};

const Branch = ({ len, ang, gen }) => {
  const style = posOfG({ len, ang, gen });
  //each branch has a left and right child except the last gen because of the logos
  const left =
    gen < totalLevel &&
    React.createElement(
      Branch,
      Object.assign(
        { len: rnd(0.8, 0.9) },
        { ang: rnd(0, 50) },
        { gen: gen + 1 },
        { key: rnd(0, 1110004239042390482034820480293429034) }
      )
    );

  const right =
    gen < totalLevel - 1 &&
    React.createElement(
      Branch,
      Object.assign(
        { len: rnd(0.8, 0.9) },
        { ang: rnd(0, -50) },
        { gen: gen + 1 },
        { key: rnd(0, 1110004239042390482034820480293429034) }
      )
    );

  return React.createElement(
    "g",
    style,
    //each group has a path to scale
    //last branch should be a logo
    gen === totalLevel
      ? React.createElement(logoArr[Math.round(rnd(0, logoArr.length - 1))], {
          id: "path" + gen,
        })
      : React.createElement("path", {
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
  animation = () => {
    //grow animation and slowy drawing animation
    //g needs to be scaled while path needs to be drawn
    var test = Elastic.easeOut.config(1, 0.3);
    gsap.timeline().from("#gen0", {
      duration: 2,
      transformOrigin: "bottom 50%",

      scaleY: 0,
      ease: test,
    });
    gsap.timeline().from("#gen0 #path0", {
      duration: 0.1,
      transformOrigin: "50% bottom",
      scaleY: 0,
    });
    for (let i = 1; i < totalLevel + 1; i++) {
      if (totalLevel > i) {
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
          .timeScale(10)
          .from("#gen" + i + " #path" + i, {
            delay: 0.4 + i,
            duration: 0.6,
            transformOrigin: "50% bottom",
            scaleY: 0,
          });
      } else {
        //logo animation
        gsap
          .timeline()
          .timeScale(10)
          .from(`#gen${totalLevel} #path${totalLevel} g`, {
            delay: 0.4 + i,
            duration: 4,
            transformOrigin: "50% bottom",
            scale: 0,
          });
      }
    }
  };

  componentDidMount() {
    this.animation();
  }

  componentDidUpdate() {
    this.animation();
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
