const myDiv = document.querySelector("div");
const myP = document.querySelector("p");
const myButton = document.querySelector("button");


const myDivConsoleLogger = function(){
    console.log("I saw a div click happen. You wanna fight?!");
};

const myPConsoleLogger = function(){
    console.log("I saw a para click happen. You wanna fight?!");
}

const myButtonConsoleLogger = function(mySpecialDevent){
    console.log("I saw a button click happen. You wanna fight?!");
    console.log(mySpecialDevent);
}

myDiv.addEventListener('click', myDivConsoleLogger, false)
myP.addEventListener('click', myPConsoleLogger, true)
myButton.addEventListener('click', myButtonConsoleLogger, false)