let http = require("http");
let request = require("request");

let request_body = undefined;

request("https://www.bnefoodtrucks.com.au/api/1/trucks", function (
  err,
  request_res,
  body
) {
  request_body = body;
});

http.createServer(function (req, res) {
  if (request_body) {
    res.writeHead(200, { "content-type": "text/html" });
    res.end(request_body);
  } else {
    res.writeHead(200, { "content-type": "text/plain" });
    res.end("Nothing retrieved yet");
  }
}).listen(8080);
