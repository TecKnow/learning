import React, { Component } from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { combineReducers, createStore } from "redux";
import expect from "expect";
import deepFreeze from "deep-freeze";
// import App from './App';
// import * as serviceWorker from './serviceWorker';

// ReactDOM.render(<App />, document.getElementById('root'));

// // If you want your app to work offline and load faster, you can change
// // unregister() to register() below. Note this comes with some pitfalls.
// // Learn more about service workers: http://bit.ly/CRA-PWA
// serviceWorker.unregister();

/*
 * Open the console
 * to see the state log.
 */

const todo = (state, action) => {
  switch (action.type) {
    case "ADD_TODO":
      return {
        id: action.id,
        text: action.text,
        completed: false
      };
    case "TOGGLE_TODO":
      if (state.id !== action.id) {
        return state;
      }

      return {
        ...state,
        completed: !state.completed
      };
    default:
      return state;
  }
};

const todos = (state = [], action) => {
  switch (action.type) {
    case "ADD_TODO":
      return [...state, todo(undefined, action)];
    case "TOGGLE_TODO":
      return state.map(t => todo(t, action));
    default:
      return state;
  }
};

const visibilityFilter = (state = "SHOW_ALL", action) => {
  switch (action.type) {
    case "SET_VISIBILITY_FILTER":
      return action.filter;
    default:
      return state;
  }
};

const todoApp = combineReducers({
  todos,
  visibilityFilter
});

const store = createStore(todoApp);

let nextTodoID = 0;
class TodoApp extends Component {
	render() {
		return (
			<div>
			<input ref={node => {
				this.input = node;
			}}/>
				<button onClick = {()=>{
					store.dispatch({type: 'ADD_TODO', text: this.input.value, id: nextTodoID++});
					this.input.value='';
				}}>
				Add Todo
				</button>
				<ul>
				{this.props.todos.map(todo => <li key={todo.id}
					onClick={()=>{
						store.dispatch({type: "TOGGLE_TODO", id: todo.id})
					}}
					style={{
						textDecoration: todo.completed? "line-through": 'none'
					}}>{todo.text}</li>)}
				</ul>
			</div>
			);
	}
}

const render = () => {
  ReactDOM.render(<TodoApp 
  	todos={store.getState().todos}/>, document.getElementById("root"));
};

store.subscribe(render);
render();

console.log("Initial state:");
console.log(store.getState());
console.log("--------------");

console.log("Dispatching ADD_TODO.");
store.dispatch({
  type: "ADD_TODO",
  id: nextTodoID++,
  text: "Learn Redux"
});
console.log("Current state:");
console.log(store.getState());
console.log("--------------");

console.log("Dispatching ADD_TODO.");
store.dispatch({
  type: "ADD_TODO",
  id: nextTodoID++,
  text: "Go shopping"
});
console.log("Current state:");
console.log(store.getState());
console.log("--------------");

console.log("Dispatching TOGGLE_TODO.");
store.dispatch({
  type: "TOGGLE_TODO",
  id: 0
});
console.log("Current state:");
console.log(store.getState());
console.log("--------------");

console.log("Dispatching SET_VISIBILITY_FILTER");
store.dispatch({
  type: "SET_VISIBILITY_FILTER",
  filter: "SHOW_COMPLETED"
});
console.log("Current state:");
console.log(store.getState());
console.log("--------------");

const testAddTodo = () => {
  const stateBefore = [];
  const action = {
    type: "ADD_TODO",
    id: 0,
    text: "Learn Redux"
  };
  const stateAfter = [
    {
      id: 0,
      text: "Learn Redux",
      completed: false
    }
  ];

  deepFreeze(stateBefore);
  deepFreeze(action);

  expect(todos(stateBefore, action)).toEqual(stateAfter);
};

const testToggleTodo = () => {
  const stateBefore = [
    {
      id: 0,
      text: "Learn Redux",
      completed: false
    },
    {
      id: 1,
      text: "Go shopping",
      completed: false
    }
  ];
  const action = {
    type: "TOGGLE_TODO",
    id: 1
  };
  const stateAfter = [
    {
      id: 0,
      text: "Learn Redux",
      completed: false
    },
    {
      id: 1,
      text: "Go shopping",
      completed: true
    }
  ];

  deepFreeze(stateBefore);
  deepFreeze(action);

  expect(todos(stateBefore, action)).toEqual(stateAfter);
};

testAddTodo();
testToggleTodo();
console.log("All tests passed.");
