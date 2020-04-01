const express = require("express");
const mongoose = require("mongoose");

mongoose
  .connect("mongodb://localhost/world", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then((data) => {
    console.log("Mongo DB connection success");
  })
  .catch((err) => {
    console.log("Mongo DB connection failed" + err.message);
  });

const app = express();

app.use("/", (req, res, next) => {
  res.json({
    confirmation: "success",
    data: "this is the mongo project!",
  });
});

app.listen(5000);
console.log("App running http://localhost:5000");
