const client = require("./Mqtt/Mqtt");
const CurrentStatus = require("./Models/CurrentStatus");

client.on("connect", function () {
  client.subscribe("/v1.6/devices/controller/current-status");

  client.on("message", function (topic, message, packet) {
    new CurrentStatus(JSON.parse(message.toString()))
      .save()
      .then(() => console.log("Current status saved"));
  });
});
