import React from "react";
import ReactDom from "react-dom";

function HelloWorld() {
  let isHello = false;
  return (
    <div>
      <span>{(isHello ? "Hello" : "Goodbye") + " World!"}</span>
    </div>
  );
}

// function Hello() {
//   const name = "World!"
//   return <span>Hello {name}</span>;
// }

// function World() {
//   return <span>world</span>;
// }

ReactDom.render(<HelloWorld />, document.querySelector("#root"));
