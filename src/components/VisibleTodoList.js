import React, { Component } from "react";
import { connect } from "react-redux";
import * as actions from "../actions";
import TodoList from "./TodoList";
import { withRouter } from "react-router-dom";
import { getVisibleTodos, getIsFetching } from "../reducers";

class VisibleTodoList extends Component {
  componentDidMount() {
    this.fetchData();
  }

  render() {
    const { toggleTodo, todos, isFetching } = this.props;
    if (isFetching && !todos.length) {
      return <p>Loading...</p>;
    }
    return <TodoList todos={todos} onTodoClick={toggleTodo} />;
  }
  componentDidUpdate(prevProps) {
    if (this.props.filter !== prevProps.filter) {
      this.fetchData();
    }
  }

  fetchData() {
    const { filter, fetchTodos } = this.props;
    fetchTodos(filter).then(()=>console.log("done!"));
  }
}

const mapStateToProps = (state, { match }) => {
  const filter = match.params.filter || "all";
  return {
    todos: getVisibleTodos(state, filter),
    isFetching: getIsFetching(state, filter),
    filter
  };
};

VisibleTodoList = withRouter(
  connect(
    mapStateToProps,
    actions
  )(VisibleTodoList)
);

export default VisibleTodoList;
