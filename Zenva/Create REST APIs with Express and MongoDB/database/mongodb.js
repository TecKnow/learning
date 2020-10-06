import mongoose from "mongoose";

mongoose.connect(
  "mongodb+srv://tutorial_user:L5PFftSGykgmbAgs@node-express-jwt-test-awwma.gcp.mongodb.net/test?retryWrites=true&w=majority",
  {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  }
);

export default mongoose;
