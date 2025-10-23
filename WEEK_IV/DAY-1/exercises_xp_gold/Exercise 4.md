const curriedSum = (a) => (b) => a + b;
const add5 = curriedSum(5);
console.log(add5(12));
Explanation / Prediction:

curriedSum is a curried function:

The outer function takes a and returns an inner function that takes b.

The inner function returns a + b.

const add5 = curriedSum(5)

Calls the outer function with a = 5.

add5 now refers to the inner function: b => 5 + b.

add5(12)

Calls the inner function with b = 12.

Returns 5 + 12 = 17.

Final output:

Copy code
17
