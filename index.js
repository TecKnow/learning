let http = require("http");
let request = require("request");
let fs = require("fs");

let request_body = undefined;
let html_content = undefined;

function createHtmlStringFromJson(retrievedData) {
  let body_begin_index = html_content.indexOf("<body>");
  let body_end_index = html_content.indexOf("</body>");

  let string_until_body =
    html_content.slice(0, body_begin_index) + "<body>".length;
  let string_from_body = html_content.slice(body_end_index);

  let html_string = "<table><tr>";
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

  html_string += "</table>";

  return string_until_body + html_string + string_from_body;
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
    if (request_body && html_content) {
      res.writeHead(200, { "content-type": "text/html" });
      res.end(createHtmlStringFromJson(JSON.parse(request_body)));
    } else {
      res.writeHead(200, { "content-type": "text/plain" });
      res.end("Nothing retrieved yet");
    }
  })
  .listen(8080);

fs.readFile("./index.html", function (err, html) {
  if (err) {
    throw err;
  } else {
    html_content = html;
  }
});
