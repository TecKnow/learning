import React from "react";

const Nav = () => {
  return (
    <nav className="App-nav">
      <ul>
        <li className="App-nav-item">
          {/* use <a> instead of <button> tags used in video
           to align with styling in course download file: App.css */}
          <a href="items">Items</a>
        </li>
        <li className="App-nav-item">
          <a href="cart">Cart</a>
        </li>
      </ul>
    </nav>
  );
};

export default Nav;
