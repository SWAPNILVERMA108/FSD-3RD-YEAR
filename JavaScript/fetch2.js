fetch("https://jsonplaceholder.typicode.com/posts", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    food: "Burger",
    quantity: 2
  })
})
.then((response) => response.json())
.then((data) => {
  console.log("Order Confirmed:", data);
})
.catch((error) => {
  console.log("Error:", error);
});