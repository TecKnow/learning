let http = require("http");
let moment = require("moment");

function serverCallback(req, res) {
  let begin_time = moment("10:00", "HH:mm");
  let end_time = moment("18:00", "HH :mm");

  let message = "Hello " + process.argv[2] + "!\n";
  message += "Welcome to our page.\n";
  message += "Now, it is " + moment().format("HH:mm") + "\n";
  message +=
    "Our business hours are from " +
    begin_time.format("HH:mm") +
    " to " +
    end_time.format("HH:mm") +
    "\n";

  let begin_difference = begin_time.diff(moment(), "minutes");
  let end_difference = moment().diff(end_time, "minutes");

  if (begin_difference > 0) {
    message += "Please come back in " + begin_difference + " minutes.\n";
  }
  if (end_difference > 0) {
    message += "Please come back tomorrow.\n";
  }

  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end(message);
}

http.createServer(serverCallback).listen(8080);
