import React, { useState } from "react";
import Nav from "./Nav";
import "./App.css";
import ItemPage from "./ItemPage";
import {items} from "./static-data";

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
      return <ItemPage items={items}/>;
    case "cart":
      return <span>The cart</span>;
  }
};

export default App;
