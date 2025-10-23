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
