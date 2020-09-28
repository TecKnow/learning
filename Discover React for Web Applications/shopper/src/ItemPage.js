import React from "react";
import "./ItemPage.css";
import Item from "./Item";

const ItemPage = ({ items, onAddToCart }) => {
  return (
    <ul className="ItemPage-items">
      {items.map((item) => (
        <li key={item.id}>
          <Item item={item}>
            <div className="Item-price">{item.price}</div>
            <button
              className="Item-addToCart"
              onClick={() => onAddToCart(item)}
            >
              Add To Cart
            </button>
          </Item>
        </li>
      ))}
    </ul>
  );
};

export default ItemPage;
