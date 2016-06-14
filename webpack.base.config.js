var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var srcPath = path.resolve('./src/assets/');
var cssPath = path.resolve('./src/assets/css/');

var ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
  context: __dirname,
  root: srcPath,
  entry: './src/assets/js/index',

  output: {
      path: path.resolve('./src/assets/bundles/'),
      filename: "[name]-[hash].js"
  },

  plugins: [
      new ExtractTextPlugin("style.css", {
          allChunks: true
      })
  ], // add all common plugins here

  module: {
    loaders: [
        { 
            test: /\.css$/, 
            loader: ExtractTextPlugin.extract("style", "css")
        }
    ] // add all common loaders here
  },

  resolve: {
    modulesDirectories: [
        'node_modules', 
        'bower_components', 
        srcPath,
        cssPath
    ],
    extensions: ['', '.js', '.jsx', 'css']
  },
  debug: true
}
