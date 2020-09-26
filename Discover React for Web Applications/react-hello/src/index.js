import React from "react";
import ReactDom from "react-dom";

function HelloWorld() {
  return (
    <div>
      <Hello />
    </div>
  );
}

function Hello() {
  const name = "World!"
  return <span>Hello {name}</span>;
}

// function World() {
//   return <span>world</span>;
// }

ReactDom.render(<HelloWorld />, document.querySelector("#root"));
