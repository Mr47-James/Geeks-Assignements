// ==========================
// EXERCISE 1 - NUMBERS DIVISIBLE BY 23
// ==========================

function displayNumbersDivisible(divisor = 23) {
    let sum = 0;
    let divisibleNumbers = [];

    for (let i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
            divisibleNumbers.push(i);
            sum += i;
        }
    }

    console.log(divisibleNumbers.join(" "));
    console.log("Sum:", sum);
}

// Default behavior (divisible by 23)
displayNumbersDivisible();

// Bonus examples
displayNumbersDivisible(3);
displayNumbersDivisible(45);
