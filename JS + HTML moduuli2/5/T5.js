'use strict';

let nrs = []

while (true){
   const nr = parseInt(prompt("Enter a number."))

   if (nrs.includes(nr)) break; {
      nrs.push(nr)
  }
}

alert("You have already entered that number.")
nrs.sort((a,b) => a-b)

for (let i = 0; i < nrs.length; i++) {
  console.log(nrs[i])
}