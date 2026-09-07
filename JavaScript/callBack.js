function sum (a,b){
    return a+b;
}

function sumWithMsg(clbk, msg){
    const result = clbk(5, 10);
    const fresult = "hi" + msg + "your score is : " + result;
    console.log(fresult);

}

sumWithMsg(sum, " Mr. Tom ");