const logService = require('../services/logService');

exports.createLog = async (req, res) => {
    try {
        const { message, level } = req.body;
        await logService.createLog(message, level);
        res.status(201).send('Log created');
    } catch (error) {
        res.status(500).send('Error creating log');
    }
};