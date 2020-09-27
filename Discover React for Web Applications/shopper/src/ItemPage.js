import React from "react";
import "./ItemPage.css";

const ItemPage = ({ items }) => {
  return (
    <ul className="ItemPage-items">
      {items.map((item) => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
};

export default ItemPage;
