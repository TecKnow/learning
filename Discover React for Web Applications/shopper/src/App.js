import React, { useState } from "react";
import Nav from "./Nav";
import "./App.css";

const App = () => {
  const [activeTab, setActiveTab] = useState("items");
  return (
    <div className="App">
      <Nav activeTab={activeTab} onTabChange={setActiveTab}/>
      <main className="app-content">
        <Content tab={activeTab} />
      </main>
    </div>
  );
};

const Content = ({ tab }) => {
  switch (tab) {
    default:
    case "items":
      return <span>The items</span>;
    case "cart":
      return <span>The cart</span>;
  }
};

export default App;
