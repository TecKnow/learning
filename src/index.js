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

const todos = (state = [], action) => {
  switch (action.type) {
    default:
      return state;
    case "ADD_TODO":
      return [...state, { id: action.id, text: action.text, completed: false }];
  }
};

const testAddTodo = () => {
  const stateBefore = [];
  const action = {
    type: "ADD_TODO",
    id: 0,
    text: "Learn Redux"
  };
  const stateAfter = [{ id: 0, text: "Learn Redux", completed: false }];

  deepFreeze(stateBefore);
  deepFreeze(action);

  expect(todos(stateBefore, action)).toEqual(stateAfter);
};

testAddTodo();
console.log("All tests passed");
