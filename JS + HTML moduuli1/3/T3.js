'use strict';

let nr1 = parseInt(prompt('Choose your first number'));
let nr2 = parseInt(prompt('Choose another number'));
let nr3 = parseInt(prompt('Choose your last number'));

const sum = nr1 + nr2 + nr3;
const prd = nr1 * nr2 * nr3;
const avr = sum / 3;

document.querySelector('#Sum').innerHTML = 'The sum of the numbers is: ' + sum + '.';
document.querySelector('#Prd').innerHTML = 'The multiplication of the numbers is: ' + prd + '.';
document.querySelector('#Avr').innerHTML = 'The average of the numbers  is: ' + avr + '.';
