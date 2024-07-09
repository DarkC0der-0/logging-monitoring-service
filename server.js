const express = require('express');
const morgan = require('morgan');
const { Pool } = require('pg');
const logRoutes = require('./src/routes/logRoutes');
const net = require('net');

const app = express();
const port = 3000;

// PostgreSQL pool
const pool = new Pool(require('./src/config/db'));

// Log to PostgreSQL
const logToPostgres = (message, level) => {
  pool.query('INSERT INTO logs (message, level) VALUES ($1, $2)', [message, level], (err, res) => {
    if (err) {
      console.error('Error saving log to database:', err);
    }
  });
};

// Log to Logstash
const logToLogstash = (message) => {
  const client = new net.Socket();
  client.connect(5044, 'localhost', () => {
    client.write(JSON.stringify(message));
    client.end();
  });
};

// Middleware
app.use(morgan('combined', {
  stream: {
    write: (message) => {
      logToPostgres(message, 'info');
      logToLogstash({ message: message.trim(), level: 'info' });
    },
  },
}));

app.use('/logs', logRoutes);

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
