const express = require("express");
const app = express();
const port = 3000;
const mongoose = require("./Models/db");

app.use(function (req, res, next) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  res.setHeader("Access-Control-Allow-Credentials", true);
  next();
});

app.get("/api", (req, res) => {
  // get data from database MongoDB
  const db = mongoose.connection;
  db.collection("currentstatuses")
    .find({})
    .sort({ timestamp: -1 })
    .limit(10)
    .skip(parseInt(req.query.page ?? 0) * 10)
    .toArray(function (err, result) {
      if (err) throw err;
      res.send(result);
    });
});

app.listen(port, () => {
  console.log(`Smart Garden app listening on port ${port}`);
});
