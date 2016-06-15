var React = require('react');
var Alert = require('react-bootstrap/lib/Alert');
var Button = require('react-bootstrap/lib/Button');
var Nav = require('react-bootstrap/lib/Nav');
var NavItem = require('react-bootstrap/lib/NavItem');

var ipsumText = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.';

module.exports = React.createClass({
    getInitialState: function() {
        return ({ activeKey: 1 });
    },
    handleSelect: function(selectedKey) {
        alert("you clicked." + selectedKey);
        this.setState({activeKey: selectedKey});
    },
    render: function() {
        return (
            <Nav bsStyle="pills" activeKey={this.state.activeKey} onSelect={this.handleSelect}>
                <NavItem eventKey={1} href="/home" title="Home">Home</NavItem>
                <NavItem eventKey={2} href="/patents" title="Patients">Patient</NavItem>
                <NavItem eventKey={4} href="/tests" title="Tests">Tests</NavItem>
            </Nav>
        )
    }
});

