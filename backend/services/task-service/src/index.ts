import express from 'express';
const app = express();
app.get('/health', (req, res) => res.json({ status: 'ok' }));
app.listen(3005, () => console.log('Task service on 3005'));