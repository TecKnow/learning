import React from "react";
import "./index.css";

class PizzaApp extends React.Component {
  state = {
    size: "medium",
    glutenFree: false,
    toppings: "",
    instructions: "",
  };

  handleSubmit = (event) => {
    event.preventDefault();
    console.log(this.setState.toppings)
    const { size, glutenFree, toppings, instructions } = this.state;
    alert(`Your order: 
    size: ${size}
    Gluten Free: ${glutenFree ? "yes" : "no"}
    Toppings: ${toppings || "none"}
    instructions: ${instructions || "none"}`);
  };

  setSize = (event) => {
    this.setState({ size: event.target.value });
  };

  setGlutenFree = (event) => {
    this.setState({ glutenFree: event.target.value });
  };

  setInstructions = (event) => {
    this.setState({ instructions: event.target.value });
  };

  setToppings = (event) => {
    this.setState({ toppings: event.target.value });
  };

  render() {
    const { size, glutenFree, toppings, instructions } = this.state;
    return (
      <form onSubmit={this.handleSubmit}>
        <h1>Order Your Pizza</h1>
        <label>
          <input
            type="radio"
            value="small"
            checked={size === "small"}
            onChange={this.setSize}
          />
          small
        </label>
        <label>
          <input
            type="radio"
            value="medium"
            checked={size === "medium"}
            onChange={this.setSize}
          />
          medium
        </label>
        <label>
          <input
            type="radio"
            value="large"
            checked={size === "large"}
            onChange={this.setSize}
          />
          large
        </label>
        <br/>
        <label>
          Topping
          <select onChange={this.setToppings} value={toppings}>
            <option value="">- Pick a topping -</option>
            <option value="pepperoni">pepperoni</option>
            <option value="pepers+onions">peppers and onions</option>
            <option value="pineapple">pineapple</option>
          </select>
          <br/>
          <label>
            <input
              type="checkbox"
              checked={glutenFree}
              onChange={this.setGlutenFree}
            />
            gluten free
          </label>
          <br/>
          <label>
            Special Instructions{" "}
            <textarea value={instructions} onChange={this.setInstructions} />
          </label>
          <br/>
          <button type="submit">Send Order</button>
        </label>
      </form>
    );
  }
}

export default PizzaApp;
