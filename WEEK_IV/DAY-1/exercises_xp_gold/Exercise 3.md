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

