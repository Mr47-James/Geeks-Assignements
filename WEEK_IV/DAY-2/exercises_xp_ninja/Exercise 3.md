**In the map method:**

  arrayNum.map((num, i) => { ... })


num is the current element of the array being processed.

i is the index of that element in the array.

For your array:

  const arrayNum = [1, 2, 4, 5, 8, 9];


i will take the values 0, 1, 2, 3, 4, 5, corresponding to the indices of the elements in the array.

So the first iteration: num = 1, i = 0
Second iteration: num = 2, i = 1
… and so on until the last iteration: num = 9, i = 5.
