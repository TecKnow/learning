import uuidv4 from "uuid/v4";
import * as api from "../api";

export const addTodo = text => ({
  type: "ADD_TODO",
  text: text,
  id: uuidv4()
});
export const toggleTodo = id => ({
  type: "TOGGLE_TODO",
  id
});

export const receiveTodos = (filter, response) => ({
	type: "RECEIVE_TODOS",
	filter,
	response
})

export const requestTodos = (filter) => ({
	type: "REQUEST_TODOS",
	filter
})

export const fetchTodos = (filter) =>
	Promise.resolve(api.fetchTodos(filter)).then(response => receiveTodos(filter, response));