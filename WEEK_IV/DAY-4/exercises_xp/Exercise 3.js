const marioGame = {
  detail : "An amazing game!",
  characters : {
      mario : {
        description:"Small and jumpy. Likes princesses.",
        height: 10,
        weight: 3,
        speed: 12,
      },
      bowser : {
        description: "Big and green, Hates princesses.",
        height: 16,
        weight: 6,
        speed: 4,
      },
      princessPeach : {
        description: "Beautiful princess.",
        height: 12,
        weight: 2,
        speed: 2,
      }
  },
}

// Convert JS object to JSON string
const jsonString = JSON.stringify(marioGame);
console.log("JSON string:", jsonString);

// Convert and pretty print with 2-space indentation
const prettyJson = JSON.stringify(marioGame, null, 2);
console.log("Pretty JSON:\n", prettyJson);

// Use a breakpoint in the debugger here
debugger;

// You can inspect `prettyJson` in the console or debugger
