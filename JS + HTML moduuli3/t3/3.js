'use strict';

const names = ['John', 'Paul', 'Jones'];
const list = document.querySelector("#target")

let listnames = ''


for (let i of names) {
  listnames += `<li>${i}</li>`
}
list.innerHTML = listnames