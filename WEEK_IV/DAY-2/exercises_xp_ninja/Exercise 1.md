
[1, 2, 3].map(num => {
  if (typeof num === 'number') return num * 2;
  return;
});


map() creates a new array by applying the callback function to each element of the original array.

The callback checks if the type of num is "number". Since all elements are numbers, it returns num * 2.

There’s no else branch that executes for numbers (all are numbers), so return; is never used.

Output:

[2, 4, 6]


Each number is multiplied by 2 and returned in a new array.
