var React = require('react');
var ReactDOM = require('react-dom');
var App = require('./app');
var App2 = require('./app2');

ReactDOM.render(<App/>, document.getElementById('content'));
ReactDOM.render(<App2/>, document.getElementById('navbar'));
