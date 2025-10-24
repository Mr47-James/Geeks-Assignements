[[0, 1], [2, 3]].reduce(
  (acc, cur) => {
    return acc.concat(cur);
  },
  [1, 2],
);
reduce() takes a callback (acc, cur) => ... and an initial value [1, 2] for acc.

The array is [[0,1], [2,3]].

Step by step:

Initial accumulator (acc): [1,2]

First iteration (cur): [0,1]

acc.concat(cur) → [1,2].concat([0,1]) → [1,2,0,1]

Second iteration (cur): [2,3]

acc.concat(cur) → [1,2,0,1].concat([2,3]) → [1,2,0,1,2,3]

Output:

js
Copy code
[1, 2, 0, 1, 2, 3]
It flattens one level of the nested arrays and includes the initial accumulator.
