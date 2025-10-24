// Exercise 5 : Star Wars

const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

// Use reduce() to combine into a single string
const sentence = epic.reduce((acc, word) => acc + ' ' + word);

console.log(sentence);
