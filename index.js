const express = require("express");

const app = express();
app.get("/", (req, res, next) => {
  res.send("This is the response");
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

app.listen(5000);
console.log("Server running on localhost:5000");
