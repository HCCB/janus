var React = require('react');
var ReactDOM = require('react-dom');
var App = require('./app');
var App2 = require('./app2');

require("../css/style.css");

//require("bootstrap/dist/css/bootstrap.css");

var Alert = require('react-bootstrap/lib/Alert');

ReactDOM.render(<App/>, document.getElementById('content'));
ReactDOM.render(<App2/>, document.getElementById('navbar'));
