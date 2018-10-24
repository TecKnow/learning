import { combineReducers } from "redux";
import todos from "./todos";
import {getVisibleTodos as oldGetVisibleTodos} from "./todos";

const todoApp = combineReducers({
  todos
});

export const getVisibleTodos = (state, filter) => oldGetVisibleTodos(state.todos, filter);

export default todoApp;
