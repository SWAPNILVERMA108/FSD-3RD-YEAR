
import React from 'react';
import Student1 from './components/student1.jsx';

function App() {
  return (
    <>
    <h1 style={{ textAlign: 'center' }}>Student Details</h1>
    <div
      style={{
         display: 'flex',
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '20px',
      }}
    >
     
      <Student1 />
      <br />

      <Student1 />
      <br />

      <Student1 />
      <br />

    </div>  
    </>
    
  );
}

export default App;