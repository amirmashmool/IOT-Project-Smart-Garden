const mongoose = require("mongoose");
mongoose.connect(
  "mongodb+srv://iotprojectunige:iotprojectunige@cluster0.w6kwgkj.mongodb.net/SmartGarden"
);

module.exports = mongoose;
