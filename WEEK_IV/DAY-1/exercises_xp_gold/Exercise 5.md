const compose = (f, g) => (a) => f(g(a));
const add1 = (num) => num + 1;
const add5 = (num) => num + 5;

console.log(compose(add1, add5)(10));
Explanation / Prediction:

compose(f, g) returns a function that takes an argument a and computes f(g(a)).

compose(add1, add5)(10)

g(a) → add5(10) → 10 + 5 = 15

f(...) → add1(15) → 15 + 1 = 16

Final output:

Copy code
16
