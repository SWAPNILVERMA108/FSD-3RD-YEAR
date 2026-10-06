import React, { useState } from 'react';

const CounterApp = () => {
    const [count, setCount] = useState(0);

    return (
        <div
            style={{
                border: '3px solid orange',
                padding: '10px',
                width: '500px',
                alignItems: 'center',
                display: 'flex',
                flexDirection: 'column',
                backgroundColor: '#D9BC93',
            }}
        >
            <h1 style={{ color: "#24241a" }}>CounterApp</h1>

            <button  style={{ color: "lightpink" }} onClick={() => setCount(count + 1)}>
                ADD +
            </button>

            <span style={{ margin: '10px 10px' , color: "white" }}>
                Count: {count}
            </span>

            <button style={{ color: "lightpink" }} onClick={() => setCount(count - 1)}>
                SUB -
            </button>
        </div>
    );
};

export default CounterApp;