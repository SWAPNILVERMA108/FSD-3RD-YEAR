const num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evenNum = num.filter((n) => n % 2 === 0);
const squareNum = num.map((n) => n * n);
console.log("array : ",num)
console.log("even num : ",evenNum);
console.log("square num : ",squareNum);