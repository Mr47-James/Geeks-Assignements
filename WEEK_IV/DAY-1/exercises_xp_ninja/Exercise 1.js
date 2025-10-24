// Exercise 1 : Merge Words

const mergeWords = (word) => 
  (next) => 
    next === undefined ? word : mergeWords(`${word} ${next}`);

console.log(mergeWords('There')('is')('no')('spoon.')());
