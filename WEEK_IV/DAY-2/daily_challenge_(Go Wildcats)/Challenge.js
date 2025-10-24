const gameInfo = [
  { username: "john", team: "red", score: 5, items: ["ball", "book", "pen"] },
  { username: "becky", team: "blue", score: 10, items: ["tape", "backpack", "pen"] },
  { username: "susy", team: "red", score: 55, items: ["ball", "eraser", "pen"] },
  { username: "tyson", team: "green", score: 1, items: ["book", "pen"] },
];

// Usernames with exclamation mark
const usernames = [];
gameInfo.forEach(user => {
  usernames.push(user.username + "!");
});
console.log(usernames); 

// Usernames of players with score > 5
const winners = [];
gameInfo.forEach(user => {
  if (user.score > 5) {
    winners.push(user.username);
  }
});
console.log(winners); 
// Total score of all users
const totalScore = gameInfo.reduce((acc, user) => acc + user.score, 0);
console.log(totalScore); 
