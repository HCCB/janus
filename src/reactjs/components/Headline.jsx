import React from "react"

export default class Headline extend React.Component {
    render() {
        return (
                <h1>{ this.props.children }</h1>
               )
    }
}

