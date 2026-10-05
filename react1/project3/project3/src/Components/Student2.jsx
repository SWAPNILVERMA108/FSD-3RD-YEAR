import React from 'react'

const Student2 = (props) => {
  return (
    <div>
      <div
        style={{
          border: '2px solid black',
          width: '300px',
          height: '350px',
          textAlign: 'center'
        }}
      >
        <h1>Student</h1>

        <img
          src={props.image}
          alt="student"
          style={{
            width: '150px',
            height: '150px',
            objectFit: 'cover'
          }}
        />

        <h3>Class: B.Tech</h3>
        <h3>Name: {props.name}</h3>
        <h3>Section: {props.section}</h3>
      </div>
    </div>
  )
}

export default Student2