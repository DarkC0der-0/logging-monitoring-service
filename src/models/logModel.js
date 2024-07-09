const { Pool } = require('pg');
const pool = new Pool(require('../config/db'));

const creatLog = async (message, level) => {
    await pool.query('INSERT INTO logs (message, level) VALUES ($1, $2)', [message, level]); 
};

module.exports = {
    creatLog,
};