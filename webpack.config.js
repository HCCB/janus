var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,

  entry: [
      // './src/assets/js/index', // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
      './src/assets/js/index'
  ],

  output: {
      path: path.resolve('./src/assets/bundles/'),
      filename: "[name]-[hash].js",
      publicPath: 'http://localhost:3000/assets/bundles/', // tell django to use thisURL to load packages and not use STATIC_URL + bundle_name
          
  },

  resolveLoader: {
      root: path.join(__dirname, "node_modules")
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(), // don't reload if there is an error
    new BundleTracker({filename: './webpack-stats.json'}),
  ],

  module: {
    loaders: [
      { 
          test: /\.jsx?$/, 
          exclude: /node_modules/, 
          loaders: [
              'react-hot', 
              'babel-loader?presets[]=react'
              ],
      }, // to transform JSX into JS
    ],
  },

  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  },
}
