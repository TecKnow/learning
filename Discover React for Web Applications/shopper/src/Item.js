import React from "react";
import "./Item.css";

const Item = ({ item }) => {
  return (
    <div className="Item">
      <div className="Item-left">
        <div className="Item-image">
          <div className="Item-title">{item.name}</div>
          <div className="Item-description">{item.description}</div>
        </div>
      </div>
      <div className="Item-right">
        <div className="Item-price">${item.price}</div>
        <button className="Item-addToCart">Add To Cart</button>
      </div>
    </div>
  );
};

export default Item;
