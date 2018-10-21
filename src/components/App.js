import React from "react";
import Footer from "./Footer";
import AddTodo from "./AddTodo";
import VisibleTodoList from "./VisibleTodoList";

const App = (props, { store }) => (
  <div>
    <AddTodo />
    <VisibleTodoList />
    <Footer />
  </div>
);

export default App