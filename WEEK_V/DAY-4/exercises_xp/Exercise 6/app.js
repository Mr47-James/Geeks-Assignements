// app.js

// Import the chalk package
const chalk = require('chalk');

// Example usage: simple colored messages
console.log(chalk.blue('Hello world in blue!'));
console.log(chalk.red.bold('This is bold and red text!'));
console.log(chalk.green.italic('This is italic green text!'));
console.log(chalk.yellow.bgBlack('Yellow text with black background'));

// Combining multiple styles
console.log(chalk.white.bgMagenta.bold('Bold white text on magenta background'));

// Using template literals
const name = 'Elie';
console.log(chalk.cyan(`Hello ${name}, welcome to chalk!`));
