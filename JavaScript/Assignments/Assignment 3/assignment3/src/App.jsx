import React from 'react';
import Food from './components/food.jsx';

function App() {
  return (
    <>
      <h1 style={{textAlign:'center'}}>ABES HOTEL</h1>

      <div
        style={{
          display: 'flex',
          flexDirection: 'row',
          alignItems: 'center',
          justifyContent: 'center',
          gap: '20px',
        }}
      >
        <Food />
        <br />

      </div>
    </>
  );
}

export default App;