import express from 'express';
const app = express();
app.get('/health', (req, res) => res.json({ status: 'ok' }));
app.listen(3003, () => console.log('Flight service on 3003'));