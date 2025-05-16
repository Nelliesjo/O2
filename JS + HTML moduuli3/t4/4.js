'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const select = document.querySelector('#target');

for (let s of students) {
  const o = document.createElement('option');
  o.value = s.id;
  o.textContent = s.name;
  select.appendChild(o);
}
