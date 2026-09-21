import React from "react";

const Student1 = () => {
    return (
        <div>
            <div style={{
                border: '2px solid red',
                width: '300px',
                height: '300px',
                padding: '20px',
                paddingLeft:'100px',
            }}>
                <h1>TOM and JERRY</h1>

                <img
                    src="https://s.yimg.com/fz/api/res/1.2/.Q3RvNm6W1bWEkyR7VIX4A--~C/YXBwaWQ9c3JjaGRkO2ZpPWZpbGw7aD00MTI7cHhvZmY9NTA7cHlvZmY9MTAwO3E9ODA7c3M9MTt3PTM4OA--/https://i.pinimg.com/736x/c2/f0/97/c2f0975cc0cb2985e359abce2461e986.jpg"
                    alt=""
                    height="100px"
                    width="100px"
                    
                />

                <h3>Class : B.Tech</h3>
                <h3>Roll No : 12345</h3>
                <h3>Address : Delhi</h3>
            </div>
        </div>
    );
};

export default Student1;