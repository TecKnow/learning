// import React from "react";
// import ReactDOM from "react-dom";
import "./index.css";
// import { createStore } from "redux";
import expect from "expect";
import deepFreeze from "deep-freeze";
// import App from './App';
// import * as serviceWorker from './serviceWorker';

// ReactDOM.render(<App />, document.getElementById('root'));

// // If you want your app to work offline and load faster, you can change
// // unregister() to register() below. Note this comes with some pitfalls.
// // Learn more about service workers: http://bit.ly/CRA-PWA
// serviceWorker.unregister();

const toggleTodo = todo => {
  return { ...todo, completed: !todo.completed };
};

const testToggleTodo = () => {
  const todoBefore = {
    id: 0,
    text: "Learn Redux",
    completed: false
  };
  const todoAfter = {
    id: 0,
    text: "Learn Redux",
    completed: true
  };

  deepFreeze(todoBefore);
  expect(toggleTodo(todoBefore)).toEqual(todoAfter);
};

testToggleTodo();
console.log("All tests passed.");
