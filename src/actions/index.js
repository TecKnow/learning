import uuidv4 from "uuid/v4";
import { getIsFetching } from "../reducers";
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

export const fetchTodos = filter => (dispatch, getState) => {
  if (getIsFetching(getState(), filter)) {
    return Promise.resolve();
  }
  dispatch({
    type: "FETCH_TODOS_REQUEST",
    filter
  });

  return api.fetchTodos(filter).then(response => {
    dispatch({
      type: "FETCH_TODOS_SUCCESS",
      filter,
      response
    });
  }, error =>{
    dispatch({type: "FETCH_TODOS_FAILURE",
    error: true,
    filter,
    message: error.message  || "Something went wrong."
  });

  });
};
