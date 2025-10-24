const letters = ['x', 'y', 'z', 'z'];

// 1️⃣ Using a for loop
const countForLoop = {};
for (let i = 0; i < letters.length; i++) {
  const letter = letters[i];
  countForLoop[letter] = (countForLoop[letter] || 0) + 1;
}
console.log(countForLoop); // { x: 1, y: 1, z: 2 }

// 2️⃣ Using reduce()
const countReduce = letters.reduce((acc, letter) => {
  acc[letter] = (acc[letter] || 0) + 1;
  return acc;
}, {});
console.log(countReduce); // { x: 1, y: 1, z: 2 }
