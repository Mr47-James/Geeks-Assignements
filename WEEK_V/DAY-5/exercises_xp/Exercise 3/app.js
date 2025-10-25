const express = require('express');
const app = express();
const port = 5000;

// Import the data module
const { fetchPosts } = require('./data/dataService');

// Middleware to parse JSON
app.use(express.json());

// GET /posts - retrieve posts from JSONPlaceholder
app.get('/posts', async (req, res) => {
  try {
    const posts = await fetchPosts();
    console.log('Data successfully retrieved from JSONPlaceholder');
    res.json(posts);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: 'Failed to fetch posts' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`CRUD API is running at http://localhost:${port}`);
});
