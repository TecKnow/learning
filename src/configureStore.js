import { applyMiddleware, createStore } from "redux";
import promise from "redux-promise";
import logger from "redux-logger";
import todoApp from "./reducers";

const thunk = store => next => action =>
  typeof action === "function" ? action(store.dispatch) : next(action);

const configureStore = () => {
  const middlewares = [thunk, promise];

  if (process.env.NODE_ENV !== "production") {
    middlewares.push(logger);
  }

  return createStore(todoApp, applyMiddleware(...middlewares));
};

export default configureStore;
