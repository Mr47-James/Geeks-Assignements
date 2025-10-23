// ==========================
// PART I - ARRAYS
// ==========================

// Initial array
let people = ["Mary", "Devon", "James", "Greg"];

// 1. Remove "Greg"
people.splice(people.indexOf("Greg"), 1);

// 2. Replace "James" with "Jason"
people[people.indexOf("James")] = "Jason";

// 3. Add your name to the end
people.push("Latros");

// 4. Log Mary's index
console.log("Mary's index:", people.indexOf("Mary"));

// 5. Make a copy without "Mary" and your name
let copyPeople = people.slice(1, people.length - 1);
console.log("Copy of people:", copyPeople);

// 6. Index of "Foo"
console.log("Index of Foo:", people.indexOf("Foo")); // returns -1 because "Foo" is not in the array

// 7. Last element
let last = people[people.length - 1];
console.log("Last element:", last);

// ==========================
// PART II - LOOPS
// ==========================

// 1. Iterate through people array and log each person
for (let person of people) {
    console.log(person);
}

// 2. Iterate and exit loop after logging "Devon"
for (let person of people) {
    console.log(person);
    if (person === "Devon") break;
}
