const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static('public')); // serve static files

// Emoji dataset
const emojis = [
    { emoji: '😀', name: 'Smile' },
    { emoji: '🐶', name: 'Dog' },
    { emoji: '🌮', name: 'Taco' },
    { emoji: '🍎', name: 'Apple' },
    { emoji: '🚗', name: 'Car' },
    { emoji: '🏀', name: 'Basketball' },
    { emoji: '🐱', name: 'Cat' },
    { emoji: '🍕', name: 'Pizza' }
];

// Leaderboard
let leaderboard = [];

// Helper: Get random emoji with options
function getRandomEmoji() {
    const correctIndex = Math.floor(Math.random() * emojis.length);
    const correct = emojis[correctIndex];

    // pick 3 random wrong options
    let options = [correct.name];
    while (options.length < 4) {
        const randomOption = emojis[Math.floor(Math.random() * emojis.length)].name;
        if (!options.includes(randomOption)) options.push(randomOption);
    }

    // shuffle options
    options = options.sort(() => Math.random() - 0.5);

    return { emoji: correct.emoji, options, correctAnswer: correct.name };
}

// GET: serve a random emoji with options
app.get('/emoji', (req, res) => {
    const emojiObj = getRandomEmoji();
    res.json(emojiObj);
});

// POST: submit a guess
app.post('/guess', (req, res) => {
    const { emoji, guess, player } = req.body;

    const correctEmoji = emojis.find(e => e.emoji === emoji);
    const isCorrect = correctEmoji && correctEmoji.name === guess;

    // Update leaderboard
    if (!leaderboard.find(p => p.name === player)) {
        leaderboard.push({ name: player, score: 0 });
    }

    const playerObj = leaderboard.find(p => p.name === player);
    if (isCorrect) playerObj.score++;

    res.json({ isCorrect, correctAnswer: correctEmoji.name, score: playerObj.score });
});

// GET: leaderboard
app.get('/leaderboard', (req, res) => {
    const sortedLeaderboard = leaderboard.sort((a, b) => b.score - a.score);
    res.json(sortedLeaderboard);
});

app.listen(port, () => {
    console.log(`Emoji game running at http://localhost:${port}`);
});

