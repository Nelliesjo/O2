'use strict';

let nr = 1
let list = []

while (nr !== 0) {
  nr = parseInt(prompt("Which number, enter 0 once you're done"))
  list.push(nr)
}


list.sort((b,a) => b-a);
list.reverse()

for (let i = 0; i <list.length; i++ ) {
  console.log(list[i])
}