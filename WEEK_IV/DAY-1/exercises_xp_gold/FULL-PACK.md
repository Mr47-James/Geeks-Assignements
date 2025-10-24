 # Exercise 1
 const landscape = () => {
  let result = "";

  const flat = (x) => {
    for (let count = 0; count < x; count++) {
      result += "_";
    }
  };

  const mountain = (x) => {
    result += "/";
    for (let counter = 0; counter < x; counter++) {
      result += "'";
    }
    result += "\\";
  };

  flat(4);
  mountain(4);
  flat(4);

  return result;
};

console.log(landscape());

# Exercise 2
const addTo = x => y => x + y;
const addToTen = addTo(10);
console.log(addToTen(3));

---

Explanation / Prediction:

addTo is a closure: it returns a function that remembers x.

x is passed to addTo when called.

The returned function takes y and returns x + y.

const addToTen = addTo(10);

Calls addTo with x = 10.

addToTen now holds the inner function y => 10 + y.

addToTen(3)

Calls the inner function with y = 3.

Returns 10 + 3 = 13.

Final output:

13

# Exercise 3 

Explanation / Prediction:

curriedSum is a curried function:

The first function takes a and returns another function that takes b.

The inner function returns a + b.

curriedSum(30)

Calls the outer function with a = 30.

Returns the inner function: b => 30 + b.

curriedSum(30)(1)

Calls the inner function with b = 1.

Returns 30 + 1 = 31.

Final output:

31

# Exercise 4

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

# Exercise 5

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
