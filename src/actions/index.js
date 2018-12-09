import {normalize} from 'normalizr';
import * as schema from "./schema";
import { getIsFetching } from "../reducers";
import * as api from "../api";

export const addTodo = text => dispatch => {
  api
    .addTodo(text)
    .then(response => {
      dispatch({ type: "ADD_TODO_SUCCESS", response: normalize(response, schema.todo) })});
};
export const toggleTodo = id => ({
  type: "TOGGLE_TODO",
  id
});

export const fetchTodos = filter => (dispatch, getState) => {
  if (getIsFetching(getState(), filter)) {
    return Promise.resolve();
  }
  dispatch({
    type: "FETCH_TODOS_REQUEST",
    filter
  });

  return api.fetchTodos(filter).then(
    response => {
      dispatch({
        type: "FETCH_TODOS_SUCCESS",
        filter,
        response: normalize(response, schema.ArrayOfTodos)
      });
    },
    error => {
      dispatch({
        type: "FETCH_TODOS_FAILURE",
        error: true,
        filter,
        message: error.message || "Something went wrong."
      });
    }
  );
};
