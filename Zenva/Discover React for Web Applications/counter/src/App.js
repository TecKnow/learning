import React from "react";
import logo from "./logo.svg";
import "./App.css";

function handleAction(event) {
  console.log("Child did:", event);
}

// function Parent() {
//   return <Child onAction={handleAction} />;
// }

class Parent extends React.Component{
  state = {actionCount: 0}

  handleAction = (action) =>{
    console.log("Child says: ", action);
    this.setState({actionCount: this.state.actionCount +1});
  }
  render(){return (<div>
    <Child onAction={this.handleAction}/>
    <p>Clicked {this.state.actionCount} times</p>
  </div>)}
}

function Child({ onAction }) {
  return <button onClick={onAction}>Click Me!</button>;
}

function App() {
  return <Parent />;
}

export default App;
