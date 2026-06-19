require("dotenv").config();

const express = require("express");
const axios = require("axios");
const path = require("path");
const ejsMate = require("ejs-mate");

const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.engine("ejs", ejsMate);
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.render("home");
});

const API_URL = process.env.FLASK_API;

app.get("/diabetes", (req, res) => {
  res.render("diabetes");
});

app.post("/diabetes", async (req, res) => {
  try {
    const response = await axios.post(`${API_URL}/predict/diabetes`, req.body);

    res.render("result", {
      disease: "Diabetes",
      result: response.data.prediction,
      probability: response.data.probability,
    });
  } catch (err) {
    console.log(err);
    res.send("Prediction Error");
  }
});

app.get("/heart", (req, res) => {
  res.render("heart");
});

app.post("/heart", async (req, res) => {
  try {
    const response = await axios.post(`${API_URL}/predict/heart`, req.body);

    res.render("result", {
      disease: "Heart Disease",
      result: response.data.prediction,
      probability: response.data.probability,
    });
  } catch (err) {
    console.log(err);
    res.send("Prediction Error");
  }
});

app.get("/kidney", (req, res) => {
  res.render("kidney");
});

app.post("/kidney", async (req, res) => {
  try {
    const response = await axios.post(`${API_URL}/predict/kidney`, req.body);

    res.render("result", {
      disease: "Kidney Disease",
      result: response.data.prediction,
      probability: response.data.probability,
    });
  } catch (err) {
    console.log(err);
    res.send("Prediction Error");
  }
});

app.get("/liver", (req, res) => {
  res.render("liver");
});

app.post("/liver", async (req, res) => {
  try {
    const response = await axios.post(`${API_URL}/predict/liver`, req.body);

    res.render("result", {
      disease: "Liver Disease",
      result: response.data.prediction,
      probability: response.data.probability,
    });
  } catch (err) {
    console.log(err);
    res.send("Prediction Error");
  }
});

app.get("/thyroid", (req, res) => {
  res.render("thyroid");
});

app.post("/thyroid", async (req, res) => {
  try {
    const response = await axios.post(`${API_URL}/predict/thyroid`, req.body);

    res.render("result", {
      disease: "Thyroid Disease",
      result: response.data.prediction,
      probability: response.data.probability,
    });
  } catch (err) {
    console.log(err);
    res.send("Prediction Error");
  }
});

app.get("/anemia", (req, res) => {
  res.render("anemia");
});

app.post("/anemia", async (req, res) => {
  try {
    const response = await axios.post(`${API_URL}/predict/anemia`, req.body);

    res.render("result", {
      disease: "Anemia",
      result: response.data.prediction,
      probability: response.data.probability,
    });
  } catch (err) {
    console.log(err);
    res.send("Prediction Error");
  }
});

app.get("/stroke", (req, res) => {
  res.render("stroke");
});

app.post("/stroke", async (req, res) => {
  try {
    const response = await axios.post(`${API_URL}/predict/stroke`, req.body);

    res.render("result", {
      disease: "Stroke",
      result: response.data.prediction,
      probability: response.data.probability,
    });
  } catch (err) {
    console.log(err);
    res.send("Prediction Error");
  }
});

app.use((req, res, next) => {
  const err = new Error("Page Not Found");
  err.statusCode = 404;
  next(err);
});

app.use((err, req, res, next) => {
  console.error(err);

  res.status(err.statusCode || 500).render("error", {
    status: err.statusCode || 500,
    message: err.message || "Internal Server Error",
    err,
  });
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server Running On Port ${PORT}`);
});
