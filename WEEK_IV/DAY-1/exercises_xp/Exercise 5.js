// Function declaration
function kgToGrams1(kg) {
    return kg * 1000;
}
console.log(kgToGrams1(5)); // 5000

// Function expression
const kgToGrams2 = function(kg) {
    return kg * 1000;
};
console.log(kgToGrams2(3)); // 3000

// Function declaration vs expression: Declarations are hoisted and can be called before they are defined, expressions are not hoisted.

// One-line arrow function
const kgToGrams3 = kg => kg * 1000;
console.log(kgToGrams3(2.5)); // 2500
