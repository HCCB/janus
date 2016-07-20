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
        if (selectedKey == 4) {
            this.testPDF();
        }
        if (selectedKey == 5) {
            this.fbShare()
        }

    },
    testPDF: function() {
        window.location = '/dt/testpdf/';
    },
    fbShare: function() {
        window.open('http://www.facebook.com/sharer.php?s=100&p[title]=Fb Share&p[summary]=Facebook share popup&p[url]=javascript:fbShare("http://jsfiddle.net/stichoza/EYxTJ/")&p[images][0]="http://goo.gl/dS52U"', 'sharer', 'toolbar=0,status=0,width=548,height=325');
    },
    render: function() {
        return (
            <Nav bsStyle="pills" activeKey={this.state.activeKey} onSelect={this.handleSelect}>
                <NavItem eventKey={1} href="/home" title="Home">Home</NavItem>
                <NavItem eventKey={2} href="/patents" title="Patients">Patient</NavItem>
                <NavItem eventKey={4} href="/tests" title="Tests">Tests</NavItem>
                <NavItem eventKey={5} href="#" title="Share in Facebook">Share</NavItem>
            </Nav>
        )
    }
});

