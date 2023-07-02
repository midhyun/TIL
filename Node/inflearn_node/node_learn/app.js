const express = require('express');
const path = require('path');
const app = express();

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/restFront.html'));
});

app.listen(3000, () => {
    console.log('익스프레스 서버 실행');
})