import React, { Component } from 'react';
import { withRouter } from 'react-router';

import logo from '../styles/images/Logo.png';
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import NavDropdown from 'react-bootstrap/NavDropdown'

class About extends Component {
    render() {

        return (
            <div>This is the about page</div>
        )
    }
}

export default withRouter(About)