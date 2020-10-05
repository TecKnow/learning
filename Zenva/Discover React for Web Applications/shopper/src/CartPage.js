import React from 'react';
import './CartPage.css';
import Item from './Item';
 
const CartPage = ({items, onAddOne, onRemoveOne}) => (
  <ul className="CartPage-items">
    {items.map((item) => (
      <li key={item.id}>
        <Item item={item}>
          <div className="CartItem-controls">
            <button
              className="CartItem-removeOne"
              onClick={() => onRemoveOne(item)}>
              -
            </button>
            <span className="CartItem-count">{item.count}</span>
            <button className="CartItem-addOne" onClick={() => onAddOne(item)}>
              +
            </button>
          </div>
        </Item>
      </li>
    ))}
  </ul>
);
 
export default CartPage;