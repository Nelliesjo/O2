'use strict';

let nr1 = parseInt(prompt('Please input a number. '));
let nr2 = parseInt(prompt('Please input another number. '));
let nr3 = parseInt(prompt('Please input one final number. '));

const sum = nr1 + nr2 + nr3;
const prd = nr1 * nr2 * nr3;
const avr = sum / 3;


document.querySelector('#Sum').innerHTML = 'The sum of the numbers you entered is: ' + sum + '.';
document.querySelector('#Prd').innerHTML = 'The sum of the multiplication of the numbers you entered is: ' + prd + '.';
document.querySelector('#Avr').innerHTML = 'The sum of the average of the numbers you entered is: ' + avr + '.';
