const logModel = require('../models/logModel');

const createLog = async (message, level) => {
  await logModel.createLog(message, level);
};

module.exports = {
  createLog,
};
