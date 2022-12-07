// connect to mqtt broker and export client
const mqtt = require("mqtt");
const client = mqtt.connect("mqtt://industrial.api.ubidots.com", {
  username: "BBFF-PnWgejj7elVnQbQUGcBT0CM6nINcOd",
  password: "",
});

module.exports = client;
