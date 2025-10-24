const data = [
  { name: 'Butters', age: 3, type: 'dog' },
  { name: 'Cuty', age: 5, type: 'rabbit' },
  { name: 'Lizzy', age: 6, type: 'dog' },
  { name: 'Red', age: 1, type: 'cat' },
  { name: 'Joey', age: 3, type: 'dog' },
  { name: 'Rex', age: 10, type: 'dog' },
];

// Part 1: Using a loop
let totalDogYearsLoop = 0;
for (let i = 0; i < data.length; i++) {
  if (data[i].type === 'dog') {
    totalDogYearsLoop += data[i].age * 7;
  }
}
console.log("Total dog years (loop):", totalDogYearsLoop); // 182

// Part 2: Using reduce()
const totalDogYearsReduce = data
  .filter(animal => animal.type === 'dog') // only dogs
  .reduce((sum, dog) => sum + dog.age * 7, 0);

console.log("Total dog years (reduce):", totalDogYearsReduce); // 182
