exports.createHtmlStringFromJson = function (html_content, retrievedData) {
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
};

exports.createHtmlStringFromCsv = function (html_content, retrievedData) {
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
};
