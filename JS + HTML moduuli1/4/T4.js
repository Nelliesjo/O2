'use strict';

const name = prompt('What is your name? ');

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

const number = getRandomInt(4);
let house = ('house');

if (number === 0) {
  house = 'Gryffindor';
} else if (number === 1) {
  house = 'Slytherin';
} else if (number === 2) {
  house = 'Hufflepuff';
} else if (number === 3) {
  house = 'Ravenclaw';
}

document.querySelector('#target').innerHTML = name + ', you belong to ' + house + '!';
