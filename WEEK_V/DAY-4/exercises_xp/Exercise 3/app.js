// app.js

const { readFile, writeFile } = require('./fileManager');

// Read content of "Hello World.txt"
const content = readFile('Hello World.txt');

// Write new content to "Bye World.txt"
writeFile('Bye World.txt', 'Writing to the file');
