// fileManager.js

const fs = require('fs');
const path = require('path');

// Function to read a file
function readFile(filename) {
  try {
    const filePath = path.join(__dirname, filename);
    const data = fs.readFileSync(filePath, 'utf-8');
    console.log(`Content of ${filename}:`);
    console.log(data);
    return data;
  } catch (err) {
    console.error(`Error reading file ${filename}:`, err.message);
  }
}

// Function to write to a file
function writeFile(filename, content) {
  try {
    const filePath = path.join(__dirname, filename);
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`Content written to ${filename} successfully.`);
  } catch (err) {
    console.error(`Error writing file ${filename}:`, err.message);
  }
}

// Export the functions
module.exports = {
  readFile,
  writeFile
};
