import express from "express";
import parser from "body-parser";
import mongoose, { Schema } from "mongoose";

mongoose.connect(
  "mongodb+srv://tutorial_user:L5PFftSGykgmbAgs@node-express-jwt-test-awwma.gcp.mongodb.net/test?retryWrites=true&w=majority",
  {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  }
);

const userSchema = new Schema({
  username: { type: String, required: true, index: { unique: true } },
});

const User = mongoose.model("user", userSchema);

const app = new express();
app.use(parser.urlencoded({ extended: false }));

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.get("/users", (req, res) => {
  User.find({}, function (err, users) {
    res.send(users);
  });
});

app.post("/", (req, res) => {
  const { username } = req.body;
  const newUser = new User({
    username,
  });
  newUser.save(function (err, model) {
    res.send(model);
  });
});
app.listen(process.env.PORT || 3000);
console.log("Listening");
