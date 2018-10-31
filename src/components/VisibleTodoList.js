import React, { Component } from "react";
import { connect } from "react-redux";
import * as actions from "../actions";
import TodoList from "./TodoList";
import { withRouter } from "react-router-dom";
import { getVisibleTodos } from "../reducers";
import { fetchTodos } from "../api";

class VisibleTodoList extends Component {
  componentDidMount() {
    this.fetchData();
  }

  render() {
    const { toggleTodo, ...rest } = this.props;
    return <TodoList {...rest} onTodoClick={toggleTodo} />;
  }
  componentDidUpdate(prevProps) {
    if (this.props.filter !== prevProps.filter) {
      this.fetchData();
    }
  }

  fetchData() {
    const { filter, receiveTodos } = this.props;
    fetchTodos(filter).then(todos => receiveTodos(filter, todos));
  }
}

const mapStateToProps = (state, { match }) => {
  const filter = match.params.filter || "all";
  return { todos: getVisibleTodos(state, filter), filter: filter };
};

VisibleTodoList = withRouter(
  connect(
    mapStateToProps,
    actions
  )(VisibleTodoList)
);

export default VisibleTodoList;
