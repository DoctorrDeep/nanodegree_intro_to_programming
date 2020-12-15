const myDiv = document.querySelector("div");
const myP = document.querySelector("p");
const myButton = document.querySelector("button");


const myDivConsoleLogger = function() {
    console.log("I saw a div click happen. You wanna fight?!");
};

const myPConsoleLogger = function() {
    console.log("I saw a para click happen. You wanna fight?!");
}

const myButtonConsoleLogger = function(mySpecialDevent) {
    console.log("I saw a button click happen. You wanna fight?!");
    console.log(mySpecialDevent);
}

myDiv.addEventListener('click', myDivConsoleLogger, false)
myP.addEventListener('click', myPConsoleLogger, true)
myButton.addEventListener('click', myButtonConsoleLogger, false)


const myCustomDiv = document.createElement('div');
const respondToTheClick = function(evt) {
    console.log('A paragraph was clicked. clientX value = ' + evt.clientX + ', clientY value = ' + evt.clientY + ', pageY value = ' + evt.pageY + " and event target \n\n\n" + evt.target.textContent);
}
myCustomDiv.addEventListener('click', respondToTheClick);


for (let i = 1; i <= 200; i++) {
    const newElement = document.createElement('p');
    newElement.textContent = 'This is paragraph number ' + i + '\n';
    myCustomDiv.appendChild(newElement);
}


document.body.appendChild(myCustomDiv);