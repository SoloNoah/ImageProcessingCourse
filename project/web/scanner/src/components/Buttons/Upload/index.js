import React from 'react';
import "../style.css";

const Button = ({ value, style, OnClickHandler }) => {
  return (
    <input
      type="submit"
      className="button"
      value={value}
      onClick={(event) => OnClickHandler(event)}
    />
  );
};

export default Button;