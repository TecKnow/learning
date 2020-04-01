const express = require("express");
const mongoose = require("mongoose");
const City = require("./models/City");
const Country = require("./models/Country");

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

app.get("/", (req, res, next) => {
  res.json({
    confirmation: "success",
    data: "this is the mongoose project!",
  });
});

app.get("/cities", (req, res, next) => {
  City.find(null)
    .then((cities) => {
      res.json({
        confirmation: "success",
        data: cities,
      });
    })
    .catch((err) => {
      res.json({
        confirmation: "fail",
        message: err.message,
      });
    });
});

app.get("/countries", (req, res, next) => {
  Country.find(null)
    .then((countries) => {
      res.json({
        confirmation: "success",
        data: countries,
      });
    })
    .catch((err) => {
      res.json({
        confirmation: "fail",
        message: err.message,
      });
    });
});

app.listen(5000);
console.log("App running http://localhost:5000");
