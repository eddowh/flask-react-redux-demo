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

const PORT = 3000;


module.exports = {
  debug: true,
  devtool: 'cheap-module-eval-source-map',
  target: 'web',
  noInfo: false,

  resolve: {
    modulesDirectories: [
      PATHS.modules,
      PATHS.src,
    ],
  },

  entry: [
    `webpack-dev-server/client?http://localhost:${PORT}`,
    'webpack/hot/only-dev-server',
    path.join(PATHS.src, 'index.js'),
  ],

  output: {
    path: PATHS.dest,
    filename: 'bundle.js',
    publicPath: '/static/',
  },

  devServer: {
    colors: true,
    publicPath: '/static/',
    historyApiFallback: true,
    hot: true,
    port: PORT,
  },

  plugins: [
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(),
  ],

  module: {
    loaders: [
      {
        test: /\.js$/,
        include: PATHS.src,
        loaders: ['react-hot', 'babel'],
      },
    ]
  }
};
