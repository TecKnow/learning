import { Router } from "express";
import User from "../../models/User";
const router = Router();

router.get("/", (req, res) => {
  User.find({}, function (err, users) {
    res.send(users);
  });
});

router.post("/", (req, res) => {
  const { username } = req.body;
  const newUser = new User({
    username,
  });
  newUser.save(function (err, model) {
    res.send(model);
  });
});
export default router;
