'use strict';

let dogs = []

for (let i=0; i < 6; i++){
    let names = prompt("Please enter the name of a dog.")
    dogs.push(names)

}
dogs.sort()
dogs.reverse()

const html_list = document.querySelector('#Dogs');

for (let i = 0; i < 6; i++) {
  html_list.innerHTML += `<li> ${dogs[i]}</li>`;
}
