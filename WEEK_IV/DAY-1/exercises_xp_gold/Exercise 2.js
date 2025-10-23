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
