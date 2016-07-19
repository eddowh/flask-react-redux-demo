const webpack = require('webpack');
const path    = require('path');

// Path variables
const ROOT_PATH = path.resolve(__dirname)
const PATHS = {
  root    : ROOT_PATH,
  src     : path.join(ROOT_PATH, 'client'),
  modules : path.join(ROOT_PATH, 'node_modules'),
  dest    : path.join(ROOT_PATH, 'dist'),
}

const GLOBALS = {
  'process.env.NODE_ENV': JSON.stringify('production'),
};


module.exports = {
  debug: false,
  devtool: 'source-map',
  target: 'web',
  noInfo: false,

  resolve: {
    modulesDirectories: [
      PATHS.modules,
      PATHS.src,
    ],
  },

  entry: [
    path.join(PATHS.src, 'index.js'),
  ],

  output: {
    path: PATHS.dest,
    filename: 'bundle.js',
    publicPath: PATHS.dest,
  },

  plugins: [
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.DefinePlugin(GLOBALS),
    new webpack.optimize.DedupePlugin(),
    new webpack.optimize.UglifyJsPlugin(),
  ],

  module: {
    loaders: [
      {
        test: /\.js$/,
        include: PATHS.src,
        loaders: ['babel'],
      },
    ]
  }
};
