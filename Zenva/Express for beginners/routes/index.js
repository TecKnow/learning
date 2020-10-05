const express = require("express");
const router = express.Router();

let user = null;

const profiles = [
  { name: "Adam", city: "Sydney", profession: "doctor" },
  { name: "Bob", city: "Perth", profession: "lawyer" },
  { name: "Charlie", city: "Sydney", profession: "programmer" },
];

router.get("/", (req, res, next) => {
  const data = {
    name: "Home",
    date:
      req.timestamp.getFullYear() +
      "-" +
      (req.timestamp.getMonth() + 1) +
      "-" +
      req.timestamp.getDate(),
    profiles,
    user,
  };
  res.render("index", data);
});

router.get("/login", (req, res, next) => {
  res.render("login", null);
});

router.post("/login", (req, res, next) => {
  const { username, password } = req.body;
  if (password === "123") {
    user = username;
    res.redirect("/");
  } else {
    user = null;
    const data = {
      message: "Please check your password and/or username.",
    };
    res.render("error", data);
  }
});

router.post("/join", (req, res, next) => {
  const body = req.body;
  profiles.push(body);
  res.redirect("/");
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
