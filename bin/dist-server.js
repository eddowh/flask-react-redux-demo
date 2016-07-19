const express     = require('express'),
      path        = require('path'),
      open        = require('open'),
      compression = require('compression');

const PORT = 3000;
const app = express();

app.use(compression());  // enable gzip compression
app.use(express.static('dist'));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../index.html'))
});

app.listen(PORT, err => {
  if (err)
    console.log(err);
  else
    open(`http://localhost:${PORT}`);
});
