
//image change
let myImage = document.querySelector('#titleImg');

myImage.onclick = function () {
    let mysrc = myImage.getAttribute('src');
    if (mysrc === '/static/Transactions/images/vin icon.png') {
        myImage.setAttribute('src', '/static/Transactions/images/VinAlt.png');
    } else {
        myImage.setAttribute('src', '/static/Transactions/images/vin icon.png');
    }
}

//button to change user name and dynamic welcome message
let myButton = document.querySelector('#changeUserButton');
let myHeading = document.querySelector('h1');

function setUserName() {
    let myName = prompt('Please enter your name.');
    if (!myName) {
        setUserName();
    } else {
        localStorage.setItem('name', myName);
        myHeading.textContent = 'Welcome back, ' + myName;
    }
}

if (!localStorage.getItem('name')) {
    setUserName();
} else {
    let storedName = localStorage.getItem('name');
    myHeading.textContent = 'Welcome back, ' + storedName;
}

myButton.onclick = function () {
    setUserName();
}

//click to edit amount in detail screen
let amount = document.querySelector('#detailAmount');
let amountInput = document.querySelector('#amountInput');
amount.onclick = function () {
    amount = amountInput;
}
