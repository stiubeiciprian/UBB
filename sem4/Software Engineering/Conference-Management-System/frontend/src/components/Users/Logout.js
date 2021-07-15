import React, { Component } from 'react'

export default class Logout extends Component {

    componentDidMount() {
        localStorage.removeItem('AUTH_TOKEN');
        this.props.history.push(`/login`)
    }

    render() {
        return (<div>s</div>
        )
    }
}