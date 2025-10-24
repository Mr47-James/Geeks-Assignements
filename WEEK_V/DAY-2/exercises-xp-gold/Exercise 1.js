<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Giphy Fetch Example</title>
</head>
<body>
  <h1>Random Giphy GIF</h1>
  <div id="gif-container"></div>

  <script>
    async function fetchRandomGif() {
      const apiKey = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My';
      const searchTerm = 'funny'; // change the search term if you want
      const limit = 10; // fetch multiple gifs to choose randomly
      const url = `https://api.giphy.com/v1/gifs/search?q=${searchTerm}&limit=${limit}&api_key=${apiKey}`;

      try {
        const response = await fetch(url);

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data); // log the whole response object

        // pick a random GIF from the array
        const gifsArray = data.data;
        const randomIndex = Math.floor(Math.random() * gifsArray.length);
        const gifUrl = gifsArray[randomIndex].images.original.url;

        // create an image element and append to the DOM
        const img = document.createElement('img');
        img.src = gifUrl;
        img.alt = 'Random Giphy GIF';
        img.style.maxWidth = '500px';

        document.getElementById('gif-container').appendChild(img);

      } catch (error) {
        console.error('Error fetching GIF:', error);
      }
    }

    fetchRandomGif();
  </script>
</body>
</html>
