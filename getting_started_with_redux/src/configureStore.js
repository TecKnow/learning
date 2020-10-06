import { applyMiddleware, createStore } from "redux";
import logger from "redux-logger";
import todoApp from "./reducers";
import thunk from "redux-thunk";

const configureStore = () => {
  const middlewares = [thunk];

  if (process.env.NODE_ENV !== "production") {
    middlewares.push(logger);
  }

  return createStore(todoApp, applyMiddleware(...middlewares));
};

export default configureStore;
