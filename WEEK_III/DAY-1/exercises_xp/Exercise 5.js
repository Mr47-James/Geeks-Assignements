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
