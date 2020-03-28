const express = require("express");

const app = express();
app.get("/", (req, res, next) => {
  res.send("My First Express App!");
});

app.get("/json", (req, res, next) => {
  const data = {
    name: "David",
    Location: "Chicago",
  };
  res.json(data);
});

app.get("/html", (req, res, next) => {
  const html =
    "<!DOCTYPE html><html><body><h1 style='color:red'>This is an HTML response</h1></body></html>";
  res.send(html);
});

app.get("/query", (req, res, next) => {
  const query = req.query;
  res.json(query);
});

app.get("/params/:name/:location/:occupation", (req, res, next) => {
  const params = req.params;
  res.json({ params });
});

app.listen(5000);
console.log("Server running on localhost:5000");
