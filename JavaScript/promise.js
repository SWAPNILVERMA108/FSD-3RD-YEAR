function f1() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("hi !!");
            resolve();
        }, 4000);
    });
}

function f2() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("ABES college");
            resolve();
        }, 2000);
    });
}

f1()
    .then(f2)
    .catch((err) => {
        console.log("Error:", err);
    });