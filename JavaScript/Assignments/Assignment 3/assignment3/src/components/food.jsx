import React from "react";

const Food = () => {
    return (
        
        <div style={{ display: "flex", flexDirection: "row", gap: "20px" }}>
           
            <div
                style={{
                    border: "2px solid red",
                    width: "300px",
                    height: "300px",
                    padding: "20px",
                    paddingLeft: "100px",
                }}
            >
                <h1>Pizza</h1>

                <img
                    src="https://s.yimg.com/fz/api/res/1.2/XqA8ohCeF4MRkt010jCvLg--~C/YXBwaWQ9c3JjaGRkO2ZpPWZpbGw7aD00MTI7cHhvZmY9NTA7cHlvZmY9MTAwO3E9ODA7c3M9MTt3PTM4OA--/https://i.pinimg.com/736x/18/ac/f8/18acf8e0154d73400cc8692ab9d0016a.jpg"
                    alt="Pizza"
                    height="150px"
                    width="150px"
                />

                <h3>100$</h3>
            </div>
            <div
                style={{
                    border: "2px solid red",
                    width: "300px",
                    height: "300px",
                    padding: "20px",
                    paddingLeft: "100px",
                }}
            >
                <h1>Burger</h1>

                <img
                    src="https://up.yimg.com/ib/th/id/OIP.KHZYPpmrTaJYGOhR1r_mOAHaEK?pid=Api&rs=1&c=1&qlt=95&w=187&h=105"
                    alt="Burger"
                    height="150px"
                    width="150px"
                />

                <h3>100$</h3>
            </div>
            <div
                style={{
                    border: "2px solid red",
                    width: "300px",
                    height: "300px",
                    padding: "20px",
                    paddingLeft: "100px",
                    
                }}
            >
                <h1>Momos</h1>

                <img
                    src="https://s.yimg.com/fz/api/res/1.2/XgROaZAJ4U_0tDgv5lu.Cw--~C/YXBwaWQ9c3JjaGRkO2ZpPWZpbGw7aD00MTI7cHhvZmY9NTA7cHlvZmY9MTAwO3E9ODA7c3M9MTt3PTM4OA--/https://i.pinimg.com/736x/0c/88/11/0c8811acbb8c8528c452b3e8cdf8e889.jpg"
                    height="150px"
                    width="150px"
                />

                <h3>100$</h3>
            </div>
        </div>
    );
};

export default Food;