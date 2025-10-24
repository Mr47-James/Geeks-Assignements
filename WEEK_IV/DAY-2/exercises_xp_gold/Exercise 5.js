const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

// Use reduce to combine all elements into a single string
const sentence = epic.reduce((acc, word) => acc + ' ' + word);
console.log(sentence);
