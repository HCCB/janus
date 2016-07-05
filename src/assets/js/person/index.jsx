var React = require('react');
var ReactDOM = require('react-dom');
var App = require('./person');

require("bootstrap/dist/css/bootstrap.min.css");
require("bootstrap/dist/css/bootstrap-theme.min.css");

ReactDOM.render(<App/>, document.getElementById('content'));
