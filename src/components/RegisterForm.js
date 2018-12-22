import React, { Component } from "react";
import { Field, reduxForm } from "redux-form";
import { customInputField, customSelect } from "./fields";
import { validate } from "../validation"; 

class RegisterForm extends Component {
  render() {
    const { handleSubmit } = this.props;
    return (
      <form onSubmit={handleSubmit}>
        <Field
          name="firstname"
          component={customInputField}
          type="text"
          label="First Name"
        />
        <Field
          name="surname"
          component={customInputField}
          type="text"
          label="Surname"
        />
        <Field
          name="username"
          component={customInputField}
          type="text"
          label="Username"
        />
        <Field
          name="preference"
          component={customSelect}
          label="Preferred Formatting"
        />
        <Field
          name="newsletter"
          component={customInputField}
          type="checkbox"
          label="Sign up to newsletter?"
        />
        <button type="submit">Submit</button>
      </form>
    );
  }
}

RegisterForm = reduxForm({ form: "register", validate })(RegisterForm);

export default RegisterForm;
