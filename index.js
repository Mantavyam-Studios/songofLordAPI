const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Bhagavad Gita API is working!');
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});