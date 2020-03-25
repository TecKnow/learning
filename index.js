let http = require("http");
let request = require("request");
let fs = require("fs");
let csv = require("csv");
let url = require('url');

let json_request_body = undefined;
let cvs_request_body = undefined;
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

function createHtmlStringFromCsv(retrievedData) {
  let body_begin_index = html_content.indexOf("<body>");
  let body_end_index = html_content.indexOf("</body>");

  let string_until_body =
    html_content.slice(0, body_begin_index) + "<body>".length;
  let string_from_body = html_content.slice(body_end_index);

  let html_string = "<table><tr>";
  retrievedData[0].forEach(function (attribute) {
    html_string += "<th>" + attribute + "</th>";
  });
  html_string += "</tr>";
  let data = retrievedData.slice(1);

  data.forEach(function (row) {
    html_string += "<tr>";
    row.forEach(function (cell) {
      html_string += "<td>" + cell + "</td>";
    });
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
  json_request_body = body;
});

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
      switch(request_url.path){
        case '/json':
          res.end(createHtmlStringFromJson(JSON.parse(json_request_body)));
          break;
        case '/csv':
          res.end(createHtmlStringFromCsv(cvs_request_body));

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
