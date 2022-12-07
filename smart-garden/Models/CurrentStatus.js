const mongoose = require("./db");

const CurrentStatus = mongoose.model("CurrentStatus", {
  value: Number,
  timestamp: Number,
  context: Object,
  created_at: Date,
});

module.exports = CurrentStatus;
