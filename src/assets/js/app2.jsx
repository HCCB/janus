var React = require('react');
var Alert = require('react-bootstrap/lib/Alert');
var Button = require('react-bootstrap/lib/Button');

var ipsumText = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.';

module.exports = React.createClass({
    doClick: function() {
        alert("you clicked.");
    },
    render: function() {
        return (
            <div>
                <h3>Another react component -- realtime</h3>
                <Button bsStyle="primary" onClick={this.doClick}>
                    Button
                </Button><br/>
                <div>{ ipsumText }</div>
            </div>
        )
    }
});

