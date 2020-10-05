import React from "react";
import "./index.css";

const validEmailRegex = RegExp(
  /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
);

const validateForm = (errors) => {
  let valid = true;
  // This will set valid to false if any error string is non-empty.
  // Does JS have an any() function that can shorten this?
  Object.values(errors).forEach((val) => val.length > 0 && (valid = false));
  return valid;
}

class PizzaApp extends React.Component {
  state = {
    size: "medium",
    glutenFree: false,
    toppings: "",
    instructions: "",
    pizzaName: null,
    email: null,
    password: null,
    errors: { pizzaName: "", email: "", password: "" },
  };

  handleSubmit = (event) => {
    event.preventDefault();
    const { size, glutenFree, toppings, instructions } = this.state;

    if (validateForm(this.state.errors)) {
      console.info("Valid form");
      alert(`Your order: 
      size: ${size}
      Gluten Free: ${glutenFree ? "yes" : "no"}
      Toppings: ${toppings || "none"}
      instructions: ${instructions || "none"}`);
    } else {
      console.error("Invalid Form");
    }
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

  handleChange = (event) => {
    event.preventDefault();
    const { name, value } = event.target;
    let errors = this.state.errors;

    switch (name) {
      case "pizzaName":
        errors.pizzaName =
          value.length < 5
            ? "Pizza name must be at least 5 characters long!"
            : "";
        break;
      case "email":
        errors.email = validEmailRegex.test(value) ? "" : "email is not valid";
        break;
      case "password":
        errors.password =
          value.length < 8
            ? "Password must be at least 8 characters long!"
            : "";
        break;
      default:
        break;
    }
    this.setState({ errors, [name]: value });
  };
  render() {
    const { size, glutenFree, toppings, instructions, errors} = this.state;
    return (
      <div className="wrapper">
        <div className="form-wrapper">
          <h1>Order Your Pizza</h1>
          <form onSubmit={this.handleSubmit}>
            <div className="pizzaName">
              <label>Pizza Name</label>
              <input
                type="text"
                name="pizzaName"
                onChange={this.handleChange}
              />
              {errors.pizzaName.length > 0 && 
                                <span className="error"> {errors.pizzaName}</span>}
            </div>
            <div className="email">
              <label>email</label>
              <input type="email" name="email" onChange={this.handleChange} />
              {errors.email.length > 0 && 
                                <span className="error"> {errors.email}</span>}
            </div>
            <label>Size</label>
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
            <div className="topping">
              <label>
                Topping
                <select onChange={this.setToppings} value={toppings}>
                  <option value="">- Pick a topping -</option>
                  <option value="pepperoni">pepperoni</option>
                  <option value="pepers+onions">peppers and onions</option>
                  <option value="pineapple">pineapple</option>
                </select>
              </label>
            </div>
            <label>
              <input
                type="checkbox"
                checked={glutenFree}
                onChange={this.setGlutenFree}
              />
              gluten free
            </label>
            <div className="instructions">
              <label>
                Special Instructions{" "}
                <textarea
                  value={instructions}
                  onChange={this.setInstructions}
                />
              </label>
            </div>
            <div className="password">
              <label>password</label>
              <input
                type="password"
                name="password"
                onChange={this.handleChange}
              />
               {errors.password.length > 0 && 
                                <span className="error"> {errors.password}</span>}
            </div>
            <button type="submit">Send Order</button>
          </form>
        </div>
      </div>
    );
  }
}

export default PizzaApp;
