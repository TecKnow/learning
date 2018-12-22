import React from "react";
import ReactJson from "react-json-view";

export const customInputField = props => {
  const { label, input, type, meta }  = props;
  return (
    <div>
      <label>{props.label}</label>
      <input {...props.input} type={props.type} />
      {(meta.error && meta.touched) && (
        <div style ={{color: 'red'}}>{meta.error}</div>
        )}
      {/*<ReactJson src={props.meta} />*/}
    </div>
  );
};

export const customSelect = props => {
  return (
    <div>
      <label>{props.label}</label>
      <select {...props.input}>
        <option value="tabs">Tabs</option>
        <option value="spaces">Spaces</option>
      </select>
      {/*<ReactJson src={props.meta} />*/}
    </div>
  );
};
