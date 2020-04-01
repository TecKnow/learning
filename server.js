const express = require("express");
const mongoose = require("mongoose");

const app = express();

app.use("/", (req, res, next) => {
  res.json({
    confirmation: "success",
    data: "this is the mongo project!",
  });
});

app.listen(5000);
console.log("App running http://localhost:5000");
