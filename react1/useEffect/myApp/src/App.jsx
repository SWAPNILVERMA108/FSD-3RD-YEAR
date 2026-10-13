import React from "react";

const App = () => {
  const [formData , setformData] = React.useState(
    {
      name : "",
      email : "",
      password : ""
    }
  );

  React.useEffect(() => {
    console.log("Form Data Updated:", formData);
  }, [formData]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setformData((previousData) => ({ ...previousData, [name]: value }));
  };

const handleSubmit = (e)=> {
  e.preventDefault();
  alert("registration successful");
  console.log(formData);
}

  return (

    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Enter your name"
          value={formData.name}
          onChange={handleChange}
        />
        <br />
        <input
          type="email"
          name="email"
          placeholder="Enter your email"
          value={formData.email}
          onChange={handleChange}
        />
        <br />
        <input
          type="password"
          name="password"
          placeholder="Enter your password"
          value={formData.password}
          onChange={handleChange}
        />
        <br />
        <button type = "submit">Register</button>
      </form>
    </div>
  );
};

export default App;