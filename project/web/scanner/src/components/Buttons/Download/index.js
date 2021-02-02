import React from "react";
import "../style.css";

const Button = ({ value, style, OnChangeHandler }) => {
  return (
    <input
      type="submit"
      className="button"
      value={value}
      onClick={(event) => OnChangeHandler(event)}
    />
  );
};

export default Button;
