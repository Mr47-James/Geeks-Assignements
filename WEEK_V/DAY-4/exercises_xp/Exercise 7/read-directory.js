// read-directory.js
const fs = require('fs');
const path = require('path');

const directoryPath = __dirname; // current directory

fs.readdir(directoryPath, (err, files) => {
  if (err) {
    console.error('Unable to read directory:', err);
    return;
  }

  console.log('Files in directory:');
  files.forEach(file => {
    console.log(file);
  });
});
