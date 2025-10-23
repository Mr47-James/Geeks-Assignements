// ==========================
// EXERCISE 2 - ABBREV_NAME
// ==========================
function abbrevName(name) {
    const parts = name.split(" ");
    if (parts.length < 2) return name;
    return `${parts[0]} ${parts[1][0]}.`;
}

// Test case
console.log(abbrevName("Robin Singh")); // "Robin S."
