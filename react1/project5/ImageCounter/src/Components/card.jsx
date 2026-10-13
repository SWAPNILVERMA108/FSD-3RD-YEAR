
import React, { useState } from "react";

const Card = () => {

  const [width, setWidth] = useState(300);
  const [height, setHeight] = useState(200);

  
  const rowPlus = () => {
    setWidth(width + 2);
  };


  const rowMinus = () => {
    if (width > 2) {
      setWidth(width - 2);
    }
  };

  const colPlus = () => {
    setHeight(height + 2);
  };

  const colMinus = () => {
    if (height > 2) {
      setHeight(height - 2);
    }
  };

  return (
    <div className="card">

      <img
        src="https://s.yimg.com/fz/api/res/1.2/8maW26kANVJNQXtMAOe0YQ--~C/YXBwaWQ9c3JjaGRkO2ZpPWZpbGw7aD00MTI7cHhvZmY9NTA7cHlvZmY9MTAwO3E9ODA7c3M9MTt3PTM4OA--/https://i.pinimg.com/736x/53/0d/7d/530d7de578fe11925677ee115bfbf210.jpg"
        alt="Tom"
        style={{
          width: `${width}px`,
          height: `${height}px`
        }}
      />

      <div className="buttons" >

        <button onClick={rowPlus} >
          Row +
        </button>
       

        <button onClick={rowMinus}>
          Row -
        </button>

        <button onClick={colPlus}>
          Col +
        </button>

        <button onClick={colMinus}>
          Col -
        </button>

      </div>

      <p>
        Width: {width}px
      </p>

      <p>
        Height: {height}px
      </p>

    </div>
  );
};

export default Card;