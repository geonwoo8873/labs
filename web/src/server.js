const express = require('express');
const app = express();

const host = process.env.HOST || 'localhost';
const port = process.env.PORT || 3000;

app.get('/index.html', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.listen(port, host, () => {
    console.log(`Server running at http://${host}:${port}/`);
});