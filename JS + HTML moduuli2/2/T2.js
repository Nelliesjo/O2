'use strict';

const names = [];
const num_of_par = parseInt(prompt("How many people will be participating?"))


for (let i=1; i <= num_of_par; i++) {
  let name = prompt("Enter their names." + i)
  names.push(name)
}

const html_list = document.querySelector('#List');

names.sort()


for (let i = 0; i < num_of_par; i++) {
  html_list.innerHTML += `<li> ${names[i]}</li>`;
}
