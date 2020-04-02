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

router.get("/:id", (req, res, next) => {
  City.findById(req.params.id)
    .then((city) => {
      res.json({
        confirmation: "success",
        data: city,
      });
    })
    .catch((err) => {
      res.json({
        confirmation: "fail",
        message: "City " + req.params.id + " not found",
      });
    });
});

module.exports = router;
