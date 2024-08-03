const functions = require("firebase-functions");
const express = require("express");
const { exec } = require("child_process");
const path = require("path");

const app = express();

// Serve static files from the React app
app.use(express.static(path.join(__dirname, "client/build")));

// Start Streamlit server
exec("streamlit run ../app.py --server.port=8501 --server.enableCORS false", (err, stdout, stderr) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(stdout);
  console.error(stderr);
});

// The "catchall" handler: for any request that doesn't match a static file, send back the React app
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname + "/client/build/index.html"));
});

exports.app = functions.https.onRequest(app);
