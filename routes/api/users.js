import { Router } from "express";
import User from "../../models/User";
const router = Router();

router.get("/", (req, res) => {
  User.find({}, function (err, users) {
    res.send(users);
  });
});

router.post("/password", (req, res) => {
  const { username, password } = req.body;
  if (!username || !password) {
    return res.status(400).send({
      err: `Required fields not found: ${!username ? "username" : ""} ${
        !password ? "password" : ""
      }`,
    });
  }
  User.findOne({ username }, function (err, userModel) {
    if (err) {
      return res.status(400).send(err);
    }
    if (!userModel) {
      return res.status(400).send({ err: "Cannot find user" });
    }
    return userModel.comparePassword(password, function (err, isMatch) {
      if (err) {
        return res.status(400).send(err);
      }
      return res.send({ correct: isMatch });
    });
  });
});

router.post("/", (req, res) => {
  const { username, password } = req.body;
  if (!username || !password) {
    return res.status(400).send({
      err: `Required fields not found: ${!username ? "username" : ""} ${
        !password ? "password" : ""
      }`,
    });
  }

  const newUser = new User({
    username,
    password,
  });
  newUser.save(function (err, model) {
    res.send(model);
  });
});
export default router;
