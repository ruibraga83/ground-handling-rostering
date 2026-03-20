import express from 'express';
const app = express();
app.get('/health', (req, res) => res.json({ status: 'ok' }));
app.listen(3004, () => console.log('Roster service on 3004'));