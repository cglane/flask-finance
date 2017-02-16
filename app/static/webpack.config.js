var Webpack = require('webpack');
var StatsPlugin = require('stats-webpack-plugin');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var autoprefixer = require('autoprefixer-core');
var csswring = require('csswring');
var path = require('path');
var nodeModulesPath = path.resolve(__dirname, 'node_modules');
var assetsPath = path.resolve(__dirname, 'assets');
var entryPath = path.resolve(__dirname, 'frontend', 'app.js');
var host =  'localhost';

var config = {

  // Makes sure errors in console map to the correct file
  // and line number
  devtool: 'eval',
  entry: [
    entryPath
  ],
  output: {
    path: assetsPath,
    filename: 'bundle.js'
  },
  module: {

    loaders: [
      { test: /\.js$/, exclude: /node_modules/,loader: 'babel-loader' },
      {
        test: /\.css$/,
        loader: 'style!css!postcss'
      },
      {
        test: /\.scss$/,
        exclude: /node_modules/,
        loader: 'style-loader!css-loader!sass-loader'
      },
      {
        test: /\.less$/,
        exclude: /node_modules/,
        loader: 'style!css!postcss!less'
      },
      {
        test: /\.html$/,
        loader: 'html-loader'
      },
      {
        test: /\.(jpe?g|png|gif|svg)$/i,
        loaders: [
          'file?hash=sha512&digest=hex&name=[hash].[ext]',
          'image?bypassOnDebug&optimizationLevel=7&interlaced=false'
        ]
      }

    ]
  },
  postcss: [autoprefixer],

  plugins: [
    // We have to manually add the Hot Replacement plugin when running
    // from Node
    new Webpack.ProvidePlugin({
    $: "jquery",
    jQuery: "jquery",
    "window.jQuery": "jquery"
}),
  new Webpack.ProvidePlugin({
    "_": "underscore"
  })
  ]
};

module.exports = config;
