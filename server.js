const express = require("express");
const mongoose = require("mongoose");
const cities = require("./routes/cities");
const countries = require("./routes/countries");

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
app.use("/cities", cities);
app.use("/countries", countries);

app.get("/", (req, res, next) => {
  res.json({
    confirmation: "success",
    data: "this is the mongoose project!",
  });
});

app.listen(5000);
console.log("App running http://localhost:5000");
