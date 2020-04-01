const express = require("express");
const router = express.Router();
const City = require("../models/City");

router.get("/", (req, res, next) => {
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

module.exports = router;
