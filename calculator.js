const prompt = require("prompt-sync")({sigint:true})
const number1 = parseFloat(prompt("Enter first Number: "));
const operator = prompt("Enter operator:  ");
const number2 = parseFloat(prompt("ENter second number: "));
let result;

if (operator == '+'){
    result = number1 + number2
} else if (operator == '-'){
    result = number1 - number2
} else if (operator == '*'){
    result = number1 * number2
} else if (operator == '/'){
    result = number1 / number2
} else{
    console.log("pleasr give correct input")
}
console.log("Total result is", result)

const percentage = parseFloat(prompt("Enter your Marks"))

let grade = (40<= percentage<50) ? "pass grade 'C'" : (50<= percentage<60) ? "Pass 'C+'": (60<=percentage<70) ? "pass 'B" : (70<=percentage<80)  ? "pass 'B+'": (80<=percentage<90) ? "pass 'A'" : (90<= percentage<=100) ? " pass 'A+'" :'enter number less than 100'
console.log(grade)

if (50 <= percentage < 55){
    console.log("=====keii vayo haii")
} else {
    console.log("keii vayooo")
}