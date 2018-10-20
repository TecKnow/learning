import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { connect, Provider } from "react-redux";
import "./index.css";
import { combineReducers, createStore } from "redux";
import { loadState, saveState } from "./localStorage";
import uuidv4 from "uuid/v4";
import throttle from "lodash/throttle";
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

const Link = ({ active, children, onClick }) => {
  if (active) {
    return <span>{children}</span>;
  }
  return (
    <a
      href={"#" + children}
      onClick={e => {
        e.preventDefault();
        onClick();
      }}
    >
      {children}
    </a>
  );
};

const mapStateToLinkProps = (state, ownProps) => ({
  active: ownProps.filter === state.visibilityFilter
});
const mapDispatchToLinkProps = (dispatch, ownProps) => ({
  onClick() {
    dispatch(setVisibilityFilter(ownProps.filter));
  }
});
const FilterLink = connect(
  mapStateToLinkProps,
  mapDispatchToLinkProps
)(Link);

const Footer = (props, { store }) => {
  return (
    <p>
      {" "}
      <FilterLink filter="SHOW_ALL" store={store}>
        All
      </FilterLink>{" "}
      <FilterLink filter="SHOW_ACTIVE" store={store}>
        Active
      </FilterLink>{" "}
      <FilterLink filter="SHOW_COMPLETED" store={store}>
        Completed
      </FilterLink>
    </p>
  );
};
Footer.contextTypes = { store: PropTypes.object };

const Todo = ({ onClick, completed, text }) => (
  <li
    onClick={onClick}
    style={{
      textDecoration: completed ? "line-through" : "none"
    }}
  >
    {text}
  </li>
);

const TodoList = ({ todos, onTodoClick }) => (
  <ul>
    {todos.map(todo => (
      <Todo key={todo.id} {...todo} onClick={() => onTodoClick(todo.id)} />
    ))}
  </ul>
);

let AddTodo = ({ dispatch }) => {
  let input;
  return (
    <div>
      {" "}
      <input
        ref={node => {
          input = node;
        }}
      />
      <button
        onClick={() => {
          dispatch(addTodo(input.value));
          input.value = "";
        }}
      >
        Add Todo
      </button>
    </div>
  );
};
AddTodo = connect()(AddTodo);

const getVisibleTodos = (todos, filter) => {
  switch (filter) {
    case "SHOW_ALL":
      return todos;
    case "SHOW_COMPLETED":
      return todos.filter(t => t.completed);
    case "SHOW_ACTIVE":
      return todos.filter(t => !t.completed);
    default:
      return todos;
  }
};

const mapStateToTodoListProps = state => ({
  todos: getVisibleTodos(state.todos, state.visibilityFilter)
});

const mapDispatchToTodoListProps = dispatch => ({
  onTodoClick(id) {
    dispatch(toggleTodo(id));
  }
});

const VisibleTodoList = connect(
  mapStateToTodoListProps,
  mapDispatchToTodoListProps
)(TodoList);

const addTodo = text => ({
  type: "ADD_TODO",
  text: text,
  id: uuidv4()
});
const setVisibilityFilter = filter => ({
  type: "SET_VISIBILITY_FILTER",
  filter: filter
});
const toggleTodo = id => ({
  type: "TOGGLE_TODO",
  id
});

const TodoApp = (props, { store }) => (
  <div>
    <AddTodo />
    <VisibleTodoList />
    <Footer />
  </div>
);

const persistedState = loadState();
const store = createStore(todoApp, persistedState);
store.subscribe(throttle(() => {
  saveState({ todos: store.getState().todos });
}, 1000));

ReactDOM.render(
  <Provider store={store}>
    <TodoApp />
  </Provider>,
  document.getElementById("root")
);
