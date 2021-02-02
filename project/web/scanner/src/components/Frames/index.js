import React from 'react';
import './style.css' ;

const Frame = ({ style, alt }) => {
  return (
    <img
        className='frame'
        alt = {alt}
   />
  )
};

export default Frame;