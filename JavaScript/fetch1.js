fetch('https://jsonplaceholder.typicode.com/users')
.then((Response)=>Response.json())
.then((data)=>{
    console.log("Restaurant List : ",data)
})

.catch((error)=>{
    console.log("error :",error);
})


fetch('https://jsonplaceholder.typicode.com/posts')

