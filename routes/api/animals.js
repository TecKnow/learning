import { Router } from "express";
import { auth } from "../../config/passport";
import Animal from "../../models/Animals";
import User from "../../models/User";

const router = Router();

router.get("/", auth, (req, res) => {
  Animal.find({}, function (err, animalModels) {
    if (err) {
      return res.status(500).send({ err });
    }
    res.send(animalModels);
  });
});

router.post("/", auth, (req, res) => {
  const { type, name } = req.body;
  if (!type || !name) {
    return res.status(400).send("Type and Name are required");
  }
  const newAnimal = new Animal({
    name,
    type,
    owner: req.user._id,
  });

  newAnimal.save(function (err, savedAnimal) {
    if (err) {
      return res.status(400).send({ err });
    }
    User.findByIdAndUpdate(
      req.user._id,
      { $push: { animals: savedAnimal._id } },
      function (err) {
        if (err) {
          return res.status(400).send({ err });
        }
        return res.send(savedAnimal);
      }
    );
  });
});

router.delete("/:id", auth, (req, res) => {
  const { id } = req.params;
  Animal.remove({ _id: id }, function (err) {
    if (err) {
      return res.status(400).send({ err });
    }
    return res.status(204).send();
  });
});

export default router;
