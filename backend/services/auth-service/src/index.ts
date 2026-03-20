import express from 'express';
import cors from 'cors';
import { Pool } from 'pg';

const app = express();
const port = 3001;

app.use(cors());
app.use(express.json());

app.get('/health', (req, res) => {
  res.json({ status: 'ok', service: 'auth-service' });
});

app.listen(port, () => {
  console.log(`Auth service running on port ${port}`);
});