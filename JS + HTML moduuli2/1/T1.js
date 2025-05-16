'use strict';

const nr = [];
let rep = 0

while (rep<5){
  const number = parseInt(prompt("Which number?"))
  nr.push(number)
  rep ++
}


for (let i = 4; i >= 0; i--) {
        console.log(`number ${i+1}: ${nr[i]}`);
    }
