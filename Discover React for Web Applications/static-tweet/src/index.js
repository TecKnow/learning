import React from "react";
import ReactDom from "react-dom";
import "./index.css";

function Tweet() {
  return <div className="tweet"><Avatar/>Tweet</div>;
}

function Avatar() {
  return (
    <img
      src="https://www.gravatar.com/avatar/nothing"
      className="avatar"
      alt="avatar"
    />
  );
}

ReactDom.render(<Tweet />, document.querySelector("#root"));
