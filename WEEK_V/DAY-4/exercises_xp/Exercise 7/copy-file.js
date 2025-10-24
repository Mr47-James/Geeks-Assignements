// copy-file.js
const fs = require('fs');

// Read the content of source.txt
fs.readFile('source.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading source.txt:', err);
    return;
  }

  // Write the content to destination.txt
  fs.writeFile('destination.txt', data, 'utf8', (err) => {
    if (err) {
      console.error('Error writing destination.txt:', err);
      return;
    }
    console.log('File successfully copied to destination.txt');
  });
});
