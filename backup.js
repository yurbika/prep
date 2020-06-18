import React from "react";

function rnd(min, max) {
  return Math.random() * (max - min) + min;
}

var limb = [];
var sway = 0;
var mult = rnd(0.01, 0.1);
var spawn = 0;
var vel = 0;

const posOfG = ({ gen, ang }) => {
  sway++;
  vel *= 0.9;
  var dif = 1 - spawn;
  vel += dif * 0.1;
  spawn += vel;
  const scale = Math.random() * 0.5 + 0.6;
  const rotation =
    ((ang + (Math.sin(sway * mult) * Math.PI) / 128) * 180) / Math.PI;

  //request for growing influence scale per frame
  const style = {
    transform:
      gen === 0
        ? `${
            spawn < 0.6 ? "scale(" + scale * spawn + ")" : ""
          } rotate(${rotation},0,0)`
        : `translate(0,-30) ${
            spawn < 0.6 ? "scale(" + scale * spawn + ")" : ""
          } rotate(${rotation},0,0)`,
  };

  return style;
};

const Branch = ({ len, ang, gen }) => {
  const style = posOfG({ len, ang, gen });

  if (spawn > 0.6) {
    spawn = 0;
    const left =
      gen < 7 &&
      React.createElement(
        Branch,
        Object.assign(
          { len: len * rnd(0.8, 0.99) },
          { ang: rnd(0, Math.PI / 6) },
          { gen: gen + 1 },
          { key: rnd(0, 1110004239042390482034820480293429034) }
        ),
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
      gen < 7 &&
      React.createElement(
        Branch,
        Object.assign(
          { len: len * rnd(0.8, 0.99) },
          { ang: rnd(0, -Math.PI / 6) },
          { gen: gen + 1 },
          { key: rnd(0, 1110004239042390482034820480293429034) }
        ),
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
      //style belongs here
      style,
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
  }
  return React.createElement(
    "g",
    //style belongs here
    style,
    React.createElement("path", {
      d: "M0,0 v-30 l3,-3 l3,3 v30 z",
      style: {
        strokeWidth: 0.1,
        fill: "#939ca7",
      },
      key: rnd(0, 1110004239042390482034820480293429034),
    })
  );
};

class Test22 extends React.Component {
  constructor(props) {
    super(props);

    this.lastFrameTime = new Date().getTime();
    this.state = {
      time: 0,
    };
  }

  scheduleFrame() {
    this.nextFrame = window.requestAnimationFrame(() => {
      const now = new Date().getTime();
      const delta = now - this.lastFrameTime;
      if (delta > 1000) {
        // Max out at 40fps to conserve CPU cycles
        this.lastFrameTime = now;
        this.setState(({ time }) => ({ time: time + delta / 25 }));
      } else {
        this.scheduleFrame();
      }
    });
  }

  componentDidMount() {
    this.scheduleFrame();
  }

  componentDidUpdate() {
    this.scheduleFrame();
  }

  componentWillUnmount() {
    if (this.nextFrame) {
      window.cancelAnimationFrame(this.nextFrame);
      this.nextFrame = null;
    }
  }

  render() {
    return (
      <svg
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="-400,-650,800,650"
      >
        <Branch len={80} ang={0} gen={0} />
      </svg>
    );
  }
}

export default Test22;
