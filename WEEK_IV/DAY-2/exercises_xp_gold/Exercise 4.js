// Part 1: Flatten array to [1,2,3,[4],[5]]
const array = [[1],[2],[3],[[[4]]],[[[5]]]];
const flattenedArray = array.flat(2); // depth of 2 to flatten one level inside nested arrays
console.log(flattenedArray); // [1, 2, 3, [4], [5]]

// Part 2: Flatten greeting array to ["Hello young grasshopper!", "you are", "learning fast!"]
const greeting = [["Hello", "young", "grasshopper!"], ["you", "are"], ["learning", "fast!"]];
const flattenedGreeting = greeting.map(subArr => subArr.join(" "));
console.log(flattenedGreeting); // ["Hello young grasshopper!", "you are", "learning fast!"]

// Part 3: Turn greeting array into a single string
const greetingString = flattenedGreeting.join(" ");
console.log(greetingString); // "Hello young grasshopper! you are learning fast!"

// Part 4: Turn the trapped number into [3]
const trapped = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]];
const untrapped = trapped.flat(Infinity);
console.log(untrapped); // [3]
