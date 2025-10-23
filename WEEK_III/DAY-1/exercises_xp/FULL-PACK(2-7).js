// ==========================
// COLORS ARRAY
// ==========================
const colors = ["blue", "red", "green", "yellow", "purple"];

// Loop and log with numbers
for (let i = 0; i < colors.length; i++) {
    console.log(`My #${i + 1} choice is ${colors[i]}`);
}

// Bonus: correct suffixes
const suffixes = ["st", "nd", "rd", "th", "th"];

for (let i = 0; i < colors.length; i++) {
    console.log(`My ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
}

---
---
// ==========================
// EXERCISE 3 - REPEAT THE QUESTION
// ==========================

// Prompt the user for a number
let userInput = Number(prompt("Enter a number:"));

// Keep asking while the number is smaller than 10
while (userInput < 10) {
    userInput = Number(prompt("The number is smaller than 10. Enter a new number:"));
}

console.log("You entered:", userInput);
---
---
// ==========================
// BUILDING OBJECT
// ==========================
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2
    },
    tenants: ["Sarah", "Dan", "David"],
    tenantsInfo: {
        Sarah: { rooms: 3, rent: 1200 },
        Dan: { rooms: 4, rent: 1000 },
        David: { rooms: 1, rent: 1000 }
    }
};

// 1. Number of floors
console.log("Number of floors:", building.numberOfFloors);

// 2. Apartments on floors 1 and 3
console.log("Apartments on floor 1:", building.numberOfAptByFloor.firstFloor);
console.log("Apartments on floor 3:", building.numberOfAptByFloor.thirdFloor);

// 3. Second tenant and number of rooms
const secondTenant = building.tenants[1];
console.log("Second tenant:", secondTenant);
console.log("Number of rooms:", building.tenantsInfo[secondTenant].rooms);

// 4. Check rent and update Dan's rent if needed
const sarahRent = building.tenantsInfo.Sarah.rent;
const davidRent = building.tenantsInfo.David.rent;
const danRent = building.tenantsInfo.Dan.rent;

if (sarahRent + davidRent > danRent) {
    building.tenantsInfo.Dan.rent = 1200;
}

console.log("Dan's updated rent:", building.tenantsInfo.Dan.rent);

---
---

// ==========================
// EXERCISE 5 - FAMILY OBJECT
// ==========================
const family = {
    father: "John",
    mother: "Mary",
    son: "Alex",
    daughter: "Sophia"
};

// Log keys
for (let key in family) {
    console.log("Key:", key);
}

// Log values
for (let key in family) {
    console.log("Value:", family[key]);
}

---
---

// ==========================
// EXERCISE 6 - RUDOLF
// ==========================
const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
};

let sentence = "";
for (let key in details) {
    sentence += key + " " + details[key] + " ";
}

console.log(sentence.trim());

---
---

// ==========================
// EXERCISE 7 - SECRET GROUP
// ==========================
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// Extract first letters, sort, and join
const secretSociety = names
  .map(name => name[0])
  .sort()
  .join("");

console.log(secretSociety); // Output: ABJKPS
