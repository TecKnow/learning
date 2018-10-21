import uuidv4 from "uuid/v4";

export const addTodo = text => ({
  type: "ADD_TODO",
  text: text,
  id: uuidv4()
});
export const setVisibilityFilter = filter => ({
  type: "SET_VISIBILITY_FILTER",
  filter: filter
});
export const toggleTodo = id => ({
  type: "TOGGLE_TODO",
  id
});
