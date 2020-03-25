let http = require("http");
let request = require("request");
let fs = require("fs");
let csv = require("csv");
let url = require("url");
let create_html = require("./create_html.js");

let json_request_body = undefined;
let cvs_request_body = undefined;
let html_content = undefined;


setInterval(function () {
  request("https://www.bnefoodtrucks.com.au/api/1/trucks", function (
    err,
    request_res,
    body
  ) {
    json_request_body = body;
  });
}, 2000);
setInterval(function () {
  request(
    "https://www.data.brisbane.qld.gov.au/data/dataset/1e11bcdd-fab1-4ec5-b671-396fd1e6dd70/resource/3c972b8e-9340-4b6d-8c7b-2ed988aa3343/download/public-art-open-data-2020-01-09.csv",
    function (err, request_res, body) {
      csv.parse(body, function (err, data) {
        cvs_request_body = data;
      });
    }
  );
}, 2000);

request(
  "https://www.data.brisbane.qld.gov.au/data/dataset/1e11bcdd-fab1-4ec5-b671-396fd1e6dd70/resource/3c972b8e-9340-4b6d-8c7b-2ed988aa3343/download/public-art-open-data-2020-01-09.csv",
  function (err, request_res, body) {
    csv.parse(body, function (err, data) {
      cvs_request_body = data;
    });
  }
);

http
  .createServer(function (req, res) {
    if (json_request_body && cvs_request_body && html_content) {
      res.writeHead(200, { "content-type": "text/html" });
      let request_url = url.parse(req.url);
      switch (request_url.path) {
        case "/json":
          res.end(create_html.createHtmlStringFromJson(html_content, JSON.parse(json_request_body)));
          break;
        case "/csv":
          res.end(create_html.createHtmlStringFromCsv(html_content, cvs_request_body));
      }
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
