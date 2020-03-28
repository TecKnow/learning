const express = require("express");
const router = express.Router();

router.get("/", (req, res, next) => {
  const data = { name: "Home" };
  res.render("index", data);
});

router.get("/json", (req, res, next) => {
  const data = {
    name: "David",
    Location: "Chicago",
  };
  res.json(data);
});

router.get("/html", (req, res, next) => {
  const html =
    "<!DOCTYPE html><html><body><h1 style='color:red'>This is an HTML response</h1></body></html>";
  res.send(html);
});

router.get("/query", (req, res, next) => {
  const query = req.query;
  res.json(query);
});

router.get("/params/:name/:location/:occupation", (req, res, next) => {
  const params = req.params;
  res.json({ params });
});

module.exports = router;
