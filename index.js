import express from "express";
import parser from "body-parser";

const app = new express();
app.use(parser.urlencoded({ extended: false }));

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.get("/world", (req, res) => {
  res.send("World!");
});

app.post("/", (req, res) => {
  res.send(req.body);
});
app.listen(process.env.PORT || 3000);
console.log("Listening");
