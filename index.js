let http = require("http");
let request = require("request");

let request_body = undefined;

function createHtmlStringFromJson(retrievedData) {
  let html_string =
    "<html><header><title>Data aggregator</title></header></html><body><table>";
  html_string += "<tr>";
  for (let attribute in retrievedData[0]) {
    if (typeof retrievedData[0][attribute] !== "object") {
      html_string += "<th>" + attribute + "</th>";
    }
  }
  html_string += "</tr>";

  retrievedData.forEach(function (obj) {
    html_string += "<tr>";
    for (let attr in obj) {
      if (typeof obj[attr] !== "object") {
        html_string += "<td>" + obj[attr] + "</td>";
      }
    }
    html_string += "</tr>";
  });

  html_string += "</table></body></html>";

  return html_string;
}

request("https://www.bnefoodtrucks.com.au/api/1/trucks", function (
  err,
  request_res,
  body
) {
  request_body = body;
});

http
  .createServer(function (req, res) {
    if (request_body) {
      res.writeHead(200, { "content-type": "text/html" });
      res.end(createHtmlStringFromJson(JSON.parse(request_body)));
    } else {
      res.writeHead(200, { "content-type": "text/plain" });
      res.end("Nothing retrieved yet");
    }
  })
  .listen(8080);
