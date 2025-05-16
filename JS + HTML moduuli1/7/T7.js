'use strict';

let dr = parseInt(prompt('How many dice do you want to roll?'));

function getRandomInt(max) {
  return Math.floor(Math.random() * max) + 1;
}

let start = 0;
let sum = 0;

while (start < dr) {
  let roll = getRandomInt(6);
  sum += roll;
  start++;
}

document.querySelector('#Dice').innerHTML = 'Sum: ' + sum;

console.log('Sum: ' + sum);
