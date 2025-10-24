<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Morse Code Translator</title>
</head>
<body>
  <h1>Morse Code Translator</h1>
  <div id="output"></div>
  <script>
    const morse = `{
      "0": "-----",
      "1": ".----",
      "2": "..---",
      "3": "...--",
      "4": "....-",
      "5": ".....",
      "6": "-....",
      "7": "--...",
      "8": "---..",
      "9": "----.",
      "a": ".-",
      "b": "-...",
      "c": "-.-.",
      "d": "-..",
      "e": ".",
      "f": "..-.",
      "g": "--.",
      "h": "....",
      "i": "..",
      "j": ".---",
      "k": "-.-",
      "l": ".-..",
      "m": "--",
      "n": "-.",
      "o": "---",
      "p": ".--.",
      "q": "--.-",
      "r": ".-.",
      "s": "...",
      "t": "-",
      "u": "..-",
      "v": "...-",
      "w": ".--",
      "x": "-..-",
      "y": "-.--",
      "z": "--..",
      ".": ".-.-.-",
      ",": "--..--",
      "?": "..--..",
      "!": "-.-.--",
      "-": "-....-",
      "/": "-..-.",
      "@": ".--.-.",
      "(": "-.--.",
      ")": "-.--.-"
    }`;

    // Function 1: Convert JSON string to JS object
    function toJs() {
      return new Promise((resolve, reject) => {
        const morseJS = JSON.parse(morse);
        if (Object.keys(morseJS).length === 0) {
          reject("Error: Morse object is empty!");
        } else {
          resolve(morseJS);
        }
      });
    }

    // Function 2: Translate user input to Morse
    function toMorse(morseJS) {
      return new Promise((resolve, reject) => {
        const input = prompt("Enter a word or sentence:").toLowerCase();
        const morseArray = [];
        for (let char of input) {
          if (char === " ") continue; 
          if (!morseJS[char]) {
            reject(`Error: Character "${char}" does not exist in Morse code!`);
            return;
          }
          morseArray.push(morseJS[char]);
        }
        resolve(morseArray);
      });
    }

    // Function 3: Display Morse code on the page
    function joinWords(morseTranslation) {
      const outputDiv = document.getElementById("output");
      outputDiv.innerHTML = morseTranslation.join("<br>");
    }

    toJs()
      .then(morseJS => toMorse(morseJS))
      .then(morseTranslation => joinWords(morseTranslation))
      .catch(error => alert(error));
  </script>
</body>
</html>
