// const express = require('express')
// const app = express()
// const excelToJson = require('convert-excel-to-json');
// var cors = require('cors')
// const fs = require('fs');

// app.use(cors())

// app.get('/', function (req, res) {
//   res.send('Hello World')
// })

// app.get('/services', function (req, res) {
    // data = ['service01','service02','service03',]

    // res.send(data)

  //   const result = excelToJson({
  //     source: fs.readFileSync('./CV_Data.xlsx')
  //   });

  //     res.send(result)

  // })
  
  // app.listen(process.env.PORT || 3000, 
  //   () => console.log("Server is running..."));

// const express = require("express");
// const cors = require("cors");
// const bodyparser = require("body-parser");
// const XLSX = require("xlsx");

// const app = express();
// var PORT = process.env.port || 3000;

// var people = [];

// app.use(bodyparser.json());
// app.use(
//   cors({
//     //http://127.0.0.1:5500
//     //http://localhost:3000/services
//     origin: "http://127.0.0.1:5500",
//   })
// );

// app.get("/Data", function (req, res) {
//   var dataPathExcel = "Table.xlsx";
//   var wb = XLSX.readFile(dataPathExcel);
//   var sheetName = wb.SheetNames[0];
//   var sheetValue = wb.Sheets[sheetName];
//   var excelData = XLSX.utils.sheet_to_json(sheetValue);

//   res.send(excelData);
// });


  
// app.listen(PORT);

const express = require("express");
const cors = require("cors");
const bodyparser = require("body-parser");
const XLSX = require("xlsx");




const app = express();
var PORT = process.env.port || 3000;

var people = [];

app.use(bodyparser.json());
app.use(
  cors({
    origin: "http://127.0.0.1:5500",
  })
);

app.get("/Data", function (req, res) {
  var dataPathExcel = "Table.xlsx";
  var wb = XLSX.readFile(dataPathExcel);
  var sheetName = wb.SheetNames[0];
  var sheetValue = wb.Sheets[sheetName];
  var excelData = XLSX.utils.sheet_to_json(sheetValue);

  res.send(excelData);
});

app.post("/AddPeople", (req, res) => {
  people.push(req.body);
  const workSheet = XLSX.utils.json_to_sheet(people);
  const workBook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workBook, workSheet, "R_Data");
  XLSX.writeFile(workBook, "Table.xlsx");

  res.send(people);
});

app.listen(PORT);
