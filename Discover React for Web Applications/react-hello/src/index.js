import React from "react";
import ReactDom from "react-dom";

function HelloWorld() {
  return <div>Hello World!</div>;
}

ReactDom.render(<HelloWorld />, document.querySelector("#root"));
